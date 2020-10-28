#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Login Window for Tuck
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys
from typing import Text
from PyQt5.QtCore import pyqtSignal

# Libraries
from PyQt5.QtWidgets import (QCheckBox, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QWidget, QLineEdit)

# Own modules
from stockAPI import StockAPI
from screens.utilities.alertUtility import AlertUtility

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'
               
class LoginWindow(QMainWindow):
        loginSuccess = pyqtSignal()
# Functions
        # Initialization
        def __init__(self, parent, stockAPI: StockAPI):
                super(LoginWindow, self).__init__(parent)
                self.stockAPI: StockAPI = stockAPI
                self.setWindowTitle("Login")
                self.main()

        # Main application
        def main(self):
                # Build the window layout
                centralWidget = QWidget(self)
                self.setCentralWidget(centralWidget)

                mainLayout = QVBoxLayout(self)
                centralWidget.setLayout(mainLayout)
                userNameLayout = QHBoxLayout(self)
                mainLayout.addLayout(userNameLayout)
                passwordLayout = QHBoxLayout(self)
                mainLayout.addLayout(passwordLayout)
                mfaLayout = QHBoxLayout(self)
                mainLayout.addLayout(mfaLayout)
                stayLoggedInCheckboxLayout = QHBoxLayout(self)
                mainLayout.addLayout(stayLoggedInCheckboxLayout)
                loginButtonLayout = QHBoxLayout(self)
                mainLayout.addLayout(loginButtonLayout)

                labelWidth: int = 65

                # Add a label for username
                userNameLabel = QLabel("Username: ", self)
                userNameLabel.setFixedWidth(labelWidth)
                userNameLayout.addWidget(userNameLabel)
                userNameLabel.show()

                # Add a text box for username
                self.usernameTextBox = QLineEdit(self)
                userNameLayout.addWidget(self.usernameTextBox)

                # Add a label for password
                passwordLabel = QLabel("Password: ", self)
                passwordLabel.setFixedWidth(labelWidth)
                passwordLayout.addWidget(passwordLabel)
                passwordLabel.show()
                
                # Add a text box for password
                self.passwordTextBox = QLineEdit(self)
                passwordLayout.addWidget(self.passwordTextBox)
                self.passwordTextBox.setEchoMode(QLineEdit.Password)
                
                # Add a label for MFA
                mfaLabel = QLabel("MFA Token: ", self)
                mfaLabel.setFixedWidth(labelWidth)
                mfaLayout.addWidget(mfaLabel)
                mfaLabel.show()

                # Add a text box for MFA
                self.mfaTextBox = QLineEdit(self)
                mfaLayout.addWidget(self.mfaTextBox)

                # Add checkbox to save login
                self.stayLoggedInCheckbox = QCheckBox(self)
                self.stayLoggedInCheckbox.setFixedWidth(15)
                stayLoggedInCheckboxLayout.addWidget(self.stayLoggedInCheckbox)

                # add label for checkbox to save login
                stayLoggedInLabel = QLabel(" Stay Logged In?")
                stayLoggedInCheckboxLayout.addWidget(stayLoggedInLabel)

                # Add a Login button
                loginButton = QPushButton("Login", self)
                loginButtonLayout.addWidget(loginButton)

                # Setup the login button-click action
                loginButton.clicked.connect(self.onLoginButtonClicked)
                loginButton.setDefault(True)

        # Funciton for the button click
        def onLoginButtonClicked(self):
                username = self.usernameTextBox.text()
                password = self.passwordTextBox.text()
                mfa = self.mfaTextBox.text()
                stayLoggedIn = self.stayLoggedInCheckbox.isChecked()

                if not username or not password or not mfa:
                    AlertUtility.ShowAlert("Username, password, and mfa required")
                    return

                try:
                        if self.stockAPI.Login(username, password, stayLoggedIn, mfa):
                            AlertUtility.ShowAlert(f"Successful Login to Robinhood as {username}", self.onAlertButtonClicked)
                except Exception as e:
                        AlertUtility.ShowAlert(f"Login Error: {e}")

        def onAlertButtonClicked(self):
            self.loginSuccess.emit()
            
