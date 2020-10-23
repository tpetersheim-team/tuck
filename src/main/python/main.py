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
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QGridLayout,
                             QHBoxLayout, QLabel, QMainWindow, QMessageBox, QPushButton,
                             QWidget)

# Own modules
# We'll need to include the other modules

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'

# Functions
# Funciton for the button click
def on_button_clicked():
        alert = QMessageBox()
        alert.setText("Dumb tucker!")
        alert.exec_()

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()

    window.layout

    # Build the window layout
    # window < centralWidget < mainLayout < topLayout
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    mainLayout = QGridLayout()
    centralWidget.setLayout(mainLayout)
    topLayout = QHBoxLayout()
    mainLayout.addLayout(topLayout, 0, 0, 1, 2)
    
    # Add a label for Hello Tuck
    label = QLabel("Hello Tuck!")
    topLayout.addWidget(label)
    label.show()
    
    # Add a button with a pop-up message
    button = QPushButton("Show me the tuck")
    topLayout.addWidget(button)
    
    # Setup the button-click action
    button.clicked.connect(on_button_clicked)
    button.setDefault(True)
    
    window.resize(640, 480)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)