#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A generic stock API class that encompasses the funcitonality of other APIs
"""

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'


from models.services.stock import Profile, Portfolio

# Generic Stock API class from which specific classes are based
class StockAPI():
    # Initialization
    def __init__(self):
            super().__init__()

    def Login(self, username, password, stayLoggedIn, mfaCode) -> bool:
        pass

    def LoggedIn(self) -> bool:
        pass

    def Logout(self) -> None:
        pass
    
    def OrderByDollar(self, symbol, dollars):
        pass

    def OrderByShare(self, symbol, quantity):
        pass

    def RetrievePortfolio(self) -> Portfolio:
        pass

    def RetrieveProfile(self) -> Profile:
        pass

    # def RebalancePortfolio(self):
    #     pass

class StockAPIException(Exception):
    pass

    percentage: float

