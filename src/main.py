#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GUI for Tuck
More description here
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys

# Libraries
from PyQt5.QtWidgets import (QAction, QApplication, QLabel, QMainWindow, QVBoxLayout)
# from dependency_injector.wiring import Provide

# Own modules
# from src.containers import Container
# from screens.loginWindow import LoginWindow
from screens.loginWindow import LoginWindow
from services.portfolioManager import PortfolioManager
from services.stock.robinhoodAPI import RobinhoodAPI
from services.stock.stockAPI import StockAPI

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'

class App(QMainWindow):
# Functions
        # Initialization
        # def __init__(self, portfolioManager: PortfolioManager = Provide[Container.portfolioManager]):
        def __init__(self, portfolioManager: PortfolioManager = None):
                super().__init__()
                self.setWindowTitle("Tuck")
                self.resize(640, 400)

                # TODO: Make this handle multiple stock providers
                self.apiName = "robinhood" 
                stockAPI: StockAPI = StockAPI()
                if (self.apiName == "robinhood"):
                        stockAPI = RobinhoodAPI()
                self.portfolioManager = portfolioManager or PortfolioManager(stockAPI)

                self.setupMenuBar()
                self.main()

        apiName: str
        portfolioManager: PortfolioManager

        def setupMenuBar(self):
                # Build the menu bar
                mainMenu = self.menuBar()
                fileMenu = mainMenu.addMenu('&File')
                
                # Logout menu bar action
                self.logoutAction = QAction('&Logout', self)
                self.logoutAction.setShortcut("Ctrl+O")
                self.logoutAction.setStatusTip("Logout")
                self.logoutAction.triggered.connect(self.logout)
                self.logoutAction.setVisible(False)
                fileMenu.addAction(self.logoutAction)
                
                # Login menu bar action
                self.loginAction = QAction('&Login', self)
                self.loginAction.setShortcut("Ctrl+L")
                self.loginAction.setStatusTip("Login")
                self.loginAction.triggered.connect(self.showLoginWindow)
                fileMenu.addAction(self.loginAction)
                
                self.statusBar()

        # Main application
        def main(self):
                # Build the window layout
                mainLayout = QVBoxLayout(self)
                self.setLayout(mainLayout)

                self.loginLabel = QLabel("Login required", self)
                self.loginLabel.move(20, 20)
                self.loginLabel.setFixedWidth(200)
                mainLayout.addWidget(self.loginLabel)

                # Show layout
                self.show()

                self.promptLoginIfNeeded()
        
        def logout(self):
                self.portfolioManager.Logout()
                self.toggleLogin(False)

        def promptLoginIfNeeded(self):
                if self.portfolioManager.LoggedIn():
                        self.toggleLogin(True)
                else:
                        self.showLoginWindow()
        
        def showLoginWindow(self):
                self.loginWindow = LoginWindow(self, self.portfolioManager)
                self.loginWindow.loginSuccess.connect(self.onLoginSuccessful)
                self.loginWindow.show()

        def onLoginSuccessful(self):
                self.toggleLogin(True)
                self.loginWindow.close()

        def toggleLogin(self, loggedIn: bool):
                self.loginLabel.setText("You are logged in!" if loggedIn else "You are logged out!")
                self.logoutAction.setVisible(loggedIn)
                self.loginAction.setVisible(not loggedIn)
                



 
if __name__ == '__main__':
    # Setup dependency injection with config
#     container = Container()
#     container.init_resources()
#     container.config.from_ini('config/config.ini')
#     container.wire(modules=[sys.modules[__name__]])

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())