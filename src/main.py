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
from typing import Text

# Libraries
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget)

# Own modules
from robinhoodAPI import RobinhoodAPI
from screens.loginWindow import LoginWindow
from stockAPI import StockAPI

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
        def __init__(self):
                super().__init__()
                self.setWindowTitle("Tuck")
                self.resize(640, 400)
                self.stockAPI: StockAPI = RobinhoodAPI()
                self.main()

        # Main application
        def main(self):
                # Build the window layout
                mainLayout = QVBoxLayout(self)
                self.setLayout(mainLayout)

                self.loginLabel = QLabel("Login required", self)
                self.width = 200
                mainLayout.addWidget(self.loginLabel)
                self.loginLabel.show()

                # Show layout
                self.show()

                self.promptLoginIfNeeded()

        def promptLoginIfNeeded(self):
                if True: # TODO: Check if not logged in
                        self.loginWindow = LoginWindow(self, self.stockAPI)
                        self.loginWindow.loginSuccess.connect(self.onLoginSuccessful)
                        self.loginWindow.show()
                else:
                        self.showLoginMessage()

        def onLoginSuccessful(self):
                self.showLoginMessage()
                self.loginWindow.close()
        
        def showLoginMessage(self):
                self.loginLabel.setText("You are logged in!")



 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())