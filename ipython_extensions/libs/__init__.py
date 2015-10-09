#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Empty
"""

#########################################
import logging
LOG_LEVEL = logging.DEBUG
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
logging.getLogger(__name__).addHandler(NullHandler())
FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
logging.basicConfig(format=FORMAT) #, level=logging.INFO)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    return logger
