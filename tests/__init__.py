# AI_Executive_Assistant/tests/__init__.py

import unittest

# Import test modules
from .test_main import *

if __name__ == '__main__':
    # Initialize the test runner
    runner = unittest.TextTestRunner()
    
    # Discover and run all tests
    suite = unittest.defaultTestLoader.discover('.')
    runner.run(suite)