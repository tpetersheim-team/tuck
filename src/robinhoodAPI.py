#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions using Robinhood
More description here
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys

# Libraries
import robin_stocks as rs
from stockAPI import StockAPILoginException, StockAPI

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
class RobinhoodAPI(StockAPI):

    # Login Function
    # This login function uses the environment variable username and password by default
    # However if a new username and password is passed in it saves it to the environment variable
    def Login(self, username = os.environ.get("robinhood_username"),
                    password = os.environ.get("robinhood_password"),
                    stayLoggedIn = True,
                    mfaCode = 'mfa'):
        
        # Set the username and password envinroment variables as passed in
        os.environ["robinhood_username"] = username
        os.environ["robinhood_password"] = password

        # Grab the username and password environment variables
        robin_user = os.environ.get("robinhood_username")
        robin_pass = os.environ.get("robinhood_password")

        # Try to login
        try:
            rs.login(robin_user, robin_pass, store_session = stayLoggedIn, mfa_code = mfaCode)
            return True
        except Exception as e:
            raise StockAPILoginException(e)

    # Check if the user is currently logged in
    # Credentials don't matter if there is a valid stored session auth_token
    def LoggedIn(self):
        try:
            return self.Login('a', 'b')
        except Exception as e:
            return False

    # Logout Function
    # Logs out of the Robinhood account
    def Logout(self):
        rs.logout()

    # Order by dollar amount
    # These are market orders by default 
    def OrderByDollar(self, symbol, dollars):
        try:
            rs.orders.order_buy_fractional_by_price(symbol, dollars)
            share_price = float(rs.stocks.get_latest_price(symbol)[0])
            shares = str(dollars/share_price)
            result = "Successful order for: {} shares of {} at {}".format(shares, symbol, share_price) 
        except Exception as e:
            result = "Error purchasing ${} of {}./n{}".format(dollars, symbol, e)
        return(result)

    # Order by shares
    # These are market orders but can be fractional
    def OrderByShare(self, symbol, quantity):
        try:
            rs.orders.order_buy_fractional_by_quantity(symbol, quantity)
            share_price = float(rs.stocks.get_latest_price(symbol)[0])
            shares = quantity
            result = "Successful order for: {} shares of {} at {}".format(shares, symbol, share_price)        
        except Exception as e:
            result = "Error purchasing {} shares of {}./n{}".format(quantity, symbol, e)
        return(result)

    # Retrieve the current portfolio
    # More definition
    def RetrievePortfolio(self):
        pass

    # Tretrieve the current portfolio
    # More definition
    def RebalancePortfolio(self):
        pass