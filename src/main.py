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
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QGridLayout, QVBoxLayout,
                             QHBoxLayout, QLabel, QMessageBox, QPushButton,
                             QWidget, QLineEdit)

# Own modules
import robinhood_tools

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'

class App(QWidget):
# Functions
        # Initialization
        def __init__(self):
                super().__init__()
                self.setWindowTitle("Tuck")
                self.main()

        # Main application
        def main(self):
                # Build the window layout
                mainLayout = QVBoxLayout()
                self.setLayout(mainLayout)
                userNameLayout = QHBoxLayout()
                mainLayout.addLayout(userNameLayout)
                passwordLayout = QHBoxLayout()
                mainLayout.addLayout(passwordLayout)
                mfaLayout = QHBoxLayout()
                mainLayout.addLayout(mfaLayout)
                loginLayout = QHBoxLayout()
                mainLayout.addLayout(loginLayout)

                # Add a label for username
                usernameLabel = QLabel("Username: ")
                userNameLayout.addWidget(usernameLabel)
                usernameLabel.show()

                # Add a text box for username
                self.usernameTextBox = QLineEdit()
                userNameLayout.addWidget(self.usernameTextBox)

                # Add a label for password
                passwordLabel = QLabel("Password: ")
                passwordLayout.addWidget(passwordLabel)
                passwordLabel.show()
# TODO don't display the password
                # Add a text box for password
                self.passwordTextBox = QLineEdit()
                passwordLayout.addWidget(self.passwordTextBox)
                
                # Add a label for MFA
                mfaLabel = QLabel("MFA Token: ")
                mfaLayout.addWidget(mfaLabel)
                mfaLabel.show()

                # Add a text box for MFA
                self.mfaTextBox = QLineEdit()
                mfaLayout.addWidget(self.mfaTextBox)

                # Add a Login button
                loginButton = QPushButton("Login", self)
                loginLayout.addWidget(loginButton)

                # Setup the login button-click action
                loginButton.clicked.connect(self.on_button_clicked)
                loginButton.setDefault(True)

                # Show layout
                self.show()
                
        # Funciton for the button click
        def on_button_clicked(self):
                username = self.usernameTextBox.text()
                password = self.passwordTextBox.text()
                loginResult = robinhood_tools.RobinhoodLogin(username, password)
                alert = QMessageBox()
                alert.setText(loginResult)
                alert.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())