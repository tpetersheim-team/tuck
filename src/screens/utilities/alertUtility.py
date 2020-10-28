#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility for creating alerts
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys
from typing import Callable, Text

# Libraries
from PyQt5.QtWidgets import (QMessageBox)

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'

class AlertUtility(object):
    @staticmethod
    def ShowAlert(message: Text, onButtonClicked: Callable = None):
            messageBox = QMessageBox()
            not onButtonClicked or messageBox.buttonClicked.connect(onButtonClicked)
            messageBox.setText(message)
            messageBox.exec()