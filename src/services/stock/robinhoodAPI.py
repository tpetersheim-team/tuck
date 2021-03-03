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

# Own modules
from services.stock.stockAPI import StockAPI, StockAPIException
from models.services.stock import Portfolio, Holding, Profile



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
    def Login(self, username = None,
                    password = None,
                    stayLoggedIn = True,
                    mfaCode = 'mfa'):
        
        # Try to login
        try:
            rs.login(username, password, store_session = stayLoggedIn, mfa_code = mfaCode)
            return True
        except Exception as e:
            raise StockAPIException(e)

    # Check if the user is currently logged in
    # Credentials don't matter if there is a valid stored session auth_token
    def LoggedIn(self):
        try:
            return self.Login('a', 'b')
        except Exception as e:
            False

    # Logout Function
    # Logs out of the Robinhood account
    def Logout(self):
        try:
            rs.logout()
        except Exception as e:
            raise StockAPIException(e)

    # Order by dollar amount
    # These are market orders by default 
    def OrderByDollar(self, symbol, dollars):
        try:
            rs.orders.order_buy_fractional_by_price(symbol, dollars)
            share_price = float(rs.stocks.get_latest_price(symbol)[0])
            shares = str(dollars/share_price)
            result = "Successful order for: {} shares of {} at {}".format(shares, symbol, share_price) 
            return(result)
        except Exception as e:
            raise StockAPIException(e)

    # Order by shares
    # These are market orders but can be fractional
    def OrderByShare(self, symbol, quantity):
        try:
            rs.orders.order_buy_fractional_by_quantity(symbol, quantity)
            share_price = float(rs.stocks.get_latest_price(symbol)[0])
            shares = quantity
            result = "Successful order for: {} shares of {} at {}".format(shares, symbol, share_price) 
            return(result)       
        except Exception as e:
            raise StockAPIException(e)

    # Retrieve the current portfolio
    # The build_holdings function returns a dictionary:
    # Each holding is an item in the holdings dictionary
    # Keys are the individual stocks
    # Each stock is another dictionary with keys: 
    # ['price', 'quantity', 'average_buy_price', 'equity', 'percent_change', 'equity_change', 'type', 'name', 'id', 'pe_ratio', 'percentage']
    def RetrievePortfolio(self) -> Portfolio:
        try:
            # Pull down an update of the current holdings
            holdings: list[Holding] = map(lambda x: Portfolio(x["name"], x["equity"], x["price"], x["percentage"]), rs.build_holdings().items())
            return Portfolio(holdings)
        except Exception as e:
            raise StockAPIException(e)
        
    def RetrieveProfile(self) -> Portfolio:
        try:
            return map(lambda x: Profile(x["equity"], x["cash"]), rs.build_user_profile().items())
        except Exception as e:
            raise StockAPIException(e)

    # Tretrieve the current portfolio
    # target_distribution must be provided as a dictionary of stocks with percentages
    # def RebalancePortfolio(self, target_distribution):
    #     try:
    #         orders = {}
    #         # Get current portfolio and profile data
    #         self.RetrievePortfolio()
    #         # Determine the present distributions
    #         # Robin Stocks is supposed to have determined the % of your portfolio but the number is wrong so we fix it :)
    #         for name, stock in self.portfolio.items():
    #             stock['percentage'] = float(stock['equity'])/float(self.profile['equity'])
    #             # Positive differences = you have too much
    #             # Negative differences = you need more
    #             # All of this math is based on a percentage of your portfolio and will be multiplied out just as the
    #             #   orders go through to avoid momentary fluctuations
    #             # Assuming this stock is in the target distribution, this will work
    #             try:
    #                 difference = target_distribution[name]['percentage'] - stock['percentage']
    #             # Otherwise set the difference to be the entire amount
    #             except:
    #                 difference = stock['percentage']
    #             orders[name] = difference
    #         for name, stock in target_distribution.items():
    #             if stock.has_key(name):
    #                 pass
    #             else:
    #                 orders[name] = -stock['percentage']
    #         # Execute sells
    #         for name, sell in orders.items():
    #             if sell[''] > 0:
    #                 self.OrderByDollar(name, sell*self.profile['equity'])
    #             else:
    #                 pass
    #         # Execute buys
    #         for name, buy in orders.items():
    #             if buy < 0:
    #                 self.OrderByDollar(name, buy*self.profile['equity'])
    #             else:
    #                 pass
    #         # Get the updated portfolio and profile data
    #         self.RetrievePortfolio()
    #     except Exception as e:
    #         raise StockAPIException(e)