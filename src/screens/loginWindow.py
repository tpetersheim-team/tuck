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
from PyQt5.QtCore import pyqtSignal

# Libraries
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, 
                             QMessageBox, QPushButton, QWidget, QLineEdit)

# Own modules
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
               
class LoginWindow(QMainWindow):
        loginSuccess = pyqtSignal()
# Functions
        # Initialization
        def __init__(self, parent, stockAPI: StockAPI):
                super(LoginWindow, self).__init__(parent)
                self.stockAPI: StockAPI = stockAPI
                self.successfulLogin: bool = False
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
                loginLayout = QHBoxLayout(self)
                mainLayout.addLayout(loginLayout)

                # Add a label for username
                usernameLabel = QLabel("Username: ", self)
                userNameLayout.addWidget(usernameLabel)
                usernameLabel.show()

                # Add a text box for username
                self.usernameTextBox = QLineEdit(self)
                userNameLayout.addWidget(self.usernameTextBox)

                # Add a label for password
                passwordLabel = QLabel("Password: ", self)
                passwordLayout.addWidget(passwordLabel)
                passwordLabel.show()
                
                # Add a text box for password
                self.passwordTextBox = QLineEdit(self)
                passwordLayout.addWidget(self.passwordTextBox)
                self.passwordTextBox.setEchoMode(QLineEdit.Password)
                
                # Add a label for MFA
                mfaLabel = QLabel("MFA Token: ", self)
                mfaLayout.addWidget(mfaLabel)
                mfaLabel.show()

                # Add a text box for MFA
                self.mfaTextBox = QLineEdit(self)
                mfaLayout.addWidget(self.mfaTextBox)

                # Add a Login button
                loginButton = QPushButton("Login", self)
                loginLayout.addWidget(loginButton)

                # Setup the login button-click action
                loginButton.clicked.connect(self.on_login_button_clicked)
                loginButton.setDefault(True)

                # Show layout
                # self.show()
                
        # Funciton for the button click
        def on_login_button_clicked(self):
                username = self.usernameTextBox.text()
                password = self.passwordTextBox.text()
                mfa = self.mfaTextBox.text()

                self.successfulLogin: bool = False
                message: Text = "Something weird happened. This text should never get used."
                try:
                        if self.stockAPI.Login(username, password, mfa):
                                message = f"Successful Login to Robinhood as {username}"
                                self.successfulLogin = True
                except Exception as e:
                        message = f"Login Error: {e}"

                alert = QMessageBox()
                if self.successfulLogin:
                        alert.buttonClicked.connect(self.on_alert_button_clicked)
                alert.setText(message)
                alert.exec_()

        def on_alert_button_clicked(self):
            self.loginSuccess.emit()
            
