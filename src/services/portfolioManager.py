#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Portfolio Manager. Logic pertaining to portfolio manipulations
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys
from typing import Container

# Libraries
# from dependency_injector.wiring import Provide

# Own modules
from services.stock.stockAPI import StockAPI
from models.services.stock import Profile, Portfolio
from services.baseService import BaseService
# from containers import Container

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'



class TargetDistribution(object):
    def __init__(self, percentage: float) -> None:
        super().__init__()
        self.percentage = percentage

    percentage: float

class PortfolioManager(BaseService):
    # def __init__(self, stockApi: StockAPI = Provide[Container.stockApi] ) -> None:
    def __init__(self, stockAPI: StockAPI) -> None:
        self.stockApi = stockAPI
        super().__init__()

    apiName: str = "robinhood"
    stockApi: StockAPI

    profile: Profile
    portfolio: Portfolio

    def Login(self, username = None,
                    password = None,
                    stayLoggedIn = True,
                    mfaCode = 'mfa'):
        
        username = username or os.environ.get(f"{self.apiName}_username")
        password = password or os.environ.get(f"{self.apiName}_password")

        # Set the username and password envinroment variables as passed in
        os.environ[f"{self.apiName}_username"] = username
        os.environ[f"{self.apiName}_password"] = password

        # Grab the username and password environment variables
        apiUser = os.environ.get(f"{self.apiName}_username")
        apiPass = os.environ.get(f"{self.apiName}_password")

        # Try to login
        return self.stockApi.Login(apiUser, apiPass, store_session = stayLoggedIn, mfa_code = mfaCode)

    def LoggedIn(self):
        return self.stockApi.LoggedIn()

    def Logout(self):
        return self.stockApi.Logout()

    # Retrieve the current portfolio
    def RetrievePortfolio(self) -> None:
        try:
            # Pull down an update of the current holdings
            self.portfolio = self.stockApi.RetrievePortfolio()
        except Exception as e:
            raise PortfolioManagerException(e)

    # Retrieve the current profile
    def RetrieveProfile(self):
        try:
            # Update the user profile
            self.profile = self.stockApi.RetrieveProfile()
        except Exception as e:
            raise PortfolioManagerException(e)


    # Retrieve the current portfolio
    # target_distribution must be provided as a dictionary of stocks with percentages
    def RebalancePortfolio(self, target_distribution: dict[str, TargetDistribution]):
        try:
            orders: dict[str, float] = {}
            # Get current portfolio and profile data
            self.RetrievePortfolio()
            self.RetrieveProfile()

            # Determine the present distributions
            # Robin Stocks is supposed to have determined the % of your portfolio but the number is wrong so we fix it :)
            for stock in self.portfolio.holdings:
                name: str = stock.name
                stock.percentage = float(stock.equity)/float(self.profile.equity)

                # Positive differences = you have too much
                # Negative differences = you need more
                # All of this math is based on a percentage of your portfolio and will be multiplied out just as the
                #   orders go through to avoid momentary fluctuations
                # Assuming this stock is in the target distribution, this will work
                try:
                    difference = target_distribution[name].percentage - stock.percentage
                # Otherwise set the difference to be the entire amount
                except:
                    difference = stock.percentage
                orders[name] = difference

            for name, stock in target_distribution.items():
                if stock.has_key(name):
                    pass
                else:
                    orders[name] = -stock.percentage

            # Execute sells
            for name, sell in orders.items():
                if sell[''] > 0:
                    self.stockApi.OrderByDollar(name, sell*self.profile.equity)
                else:
                    pass

            # Execute buys
            for name, buy in orders.items():
                if buy < 0:
                    self.stockApi.OrderByDollar(name, buy*self.profile.equity)
                else:
                    pass

            # Get the updated portfolio and profile data
            self.RetrievePortfolio()
        except Exception as e:
            raise PortfolioManagerException(e)


class PortfolioManagerException(Exception):
    pass

