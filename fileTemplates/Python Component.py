__author__ = "Indika Piyasena"

import logging
import unittest

logger = logging.getLogger(__name__)


class $COMPONENT_NAME:
    def __init__(self):
        pass

    def process(self):
        pass


class ${COMPONENT_NAME}TestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    print "Testing $COMPONENT_NAME in stand-alone-mode"
    unittest.main()

