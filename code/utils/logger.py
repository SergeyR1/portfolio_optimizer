# -*- coding: utf-8 -*-
"""Logger module
"""

import logging
import os
import sys


def get_logger(name=__name__.split(".")[0].upper(),\
 loglevel=getattr(logging, os.environ.get("LOG_LEVEL", "WARNING"))):
    """basic logging function
    """
    logger = logging.getLogger(name=name)
    stream_handler = logging.StreamHandler(sys.stdout)
    json_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(json_formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(loglevel)
    return logger
