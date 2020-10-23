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
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QGridLayout,
                             QHBoxLayout, QLabel, QMessageBox, QPushButton,
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

# Create the main window
app = QApplication([])
window = QWidget()

# Build the window layout
mainLayout = QGridLayout()
window.setLayout(mainLayout)
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

# Show layout
window.resize(640, 480)
window.show()

# Run the application
app.exec_()
