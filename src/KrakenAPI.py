#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions using the Kraken API for cryptos
More description here
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys

# Libraries
import krakenex
from stockAPI import StockAPIException, StockAPI
from tkinter.filedialog import askopenfilename

# Own modules
# None

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'

# Make into class
class KrakenAPI(StockAPI):

    # Login Function
    # This login function uses the environment variable username and password by default
    # However if a new username and password is passed in it saves it to the environment variable
    def Login(self, username = os.environ.get("kraken_username"),
                    password = os.environ.get("kraken_password"),
                    stayLoggedIn = True,
                    mfaCode = 'mfa'):
        self.k = krakenex.API()
        # Kraken requires an API key to be generated on their website (https://support.kraken.com/hc/en-us/articles/360035317352-Generating-an-API-key-and-QR-code-for-the-Kraken-Pro-mobile-app)
        try:
            # Try to use an exisint login key
            krakenKey = os.environ.get('kraken_key_loc')
            self.k.load_key(krakenKey)
            return True
        except Exception as e:
            # If an existing key has not been saved, find one
            os.environ["kraken_key_loc"] = askopenfilename()
            krakenKey = os.environ.get('kraken_key_loc')
            self.k.load_key(krakenKey)
            raise StockAPIException(e)

    # Check if the user is currently logged in
    # Credentials don't matter if there is a valid stored session auth_token
    def LoggedIn(self):
        try:
            return self.Login('a', 'b')
        except Exception as e:
            raise StockAPIException(e)

    # Logout Function
    # Logs out of the Robinhood account
    def Logout(self):
        try:
            self.k.close()
        except Exception as e:
            raise StockAPIException(e)

    # Retrieve the current portfolio
    def RetrievePortfolio(self):
        try:
            self.balance = self.k.query_private('Balance')['result']
            self.orders = self.k.query_private('OpenOrders')['result']
        except Exception as e:
            raise StockAPIException(e)

    # Setup trading parameters
    def SetupTrading(self):
        try:
            self.purchaseType = 'limit'
            self.price = '1'
            return True
        except Exception as e:
            raise StockAPIException(e)

    # Order by dollar amount
    # These are market orders but can be limit
    def OrderByDollar(self, symbol, dollars):
        try:
            volume = str(dollars/self.price)
            self.k.query_private('AddOrder',
                                {'pair': symbol,
                                 'type': 'buy',
                                 'ordertype': self.purchaseType,
                                 'price': self.price,
                                 'volume': volume})
            result = "Successful order for: {} shares of {} at {}".format(volume, symbol, self.price) 
            return(result)
        except Exception as e:
            raise StockAPIException(e)

    # Order by crypto amount
    # These are market orders but can be limit
    def OrderByShare(self, symbol, quantity):
        try:
            volume = str(quantity)
            self.k.query_private('AddOrder',
                                {'pair': symbol,
                                 'type': 'buy',
                                 'ordertype': self.purchaseType,
                                 'price': self.price,
                                 'volume': volume})
            result = "Successful order for: {} shares of {} at {}".format(volume, symbol, self.price) 
            return(result)    
        except Exception as e:
            raise StockAPIException(e)
