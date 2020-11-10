#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Base class for any services to provide common functionality
"""

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys

# Libraries
import logging

# Own modules

# Header release information
__author__ = 'Travis Petersheim & Michael Reichenberger'
__copyright__ = 'Copyright 2020, Friar Tuck'
__credits__ = ['']
__license__ = 'MIT'
__version__ = '0.0.0'
__maintainer__ = 'Travis Petersheim'
__email__ = 'travispetersheim@gmail.com'
__status__ = 'prototype'


class BaseService:

    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f'{__name__}.{self.__class__.__name__}',
        )
