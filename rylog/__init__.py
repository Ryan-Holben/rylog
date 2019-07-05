"""
  rylog

  Logging happening in a 3-dimensional Cartesian product of:
    1. The logging level: [debug, info, warn, error]
    2. The logging category: e.g. software event, action, output
    3. The detected function/method: e.g. my_class.class_method or foo
"""

from .misc import *
from .server import *
from .client import *
