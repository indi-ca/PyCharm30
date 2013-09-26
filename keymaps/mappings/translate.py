#!/usr/bin/env python

"""Translate

Supports the creation of Advice Wizards


Usage:
   translate.py xml <xml_file>

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

__author__ = "Indika Piyasena"


import os, sys
import logging
import pickle

from docopt import docopt

import mappings as mappings

logger = logging.getLogger(__name__)


class Translate:
    def __init__(self):
        self.configure_logging()

        self.data = []
        self.cache_file = 'pickled.data'
        self.yaml_file = 'data.yml'

    def process(self):
        self.arguments = docopt(__doc__, version='Translate 0.1')
        logger.info('Translate started...')

        loaded_stream = self.load_yaml(self.yaml_file)
        if loaded_stream is None:
            logger.info('Previous data does not exist')
        else:
            logger.info('Loaded data')
        pass

    def configure_logging(self):
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        pass

    def pickle(self):
        # Simple dump and load paradigm
        file_pi = open(self.cache_file, 'w')
        pickle.dump(self.data, file_pi)

    def revive(self):
        file_pi = open(self.cache_file, 'r')
        self.data = pickle.load(file_pi)


    def log(self):
        pass

def test_something():
    translate = Translate()
    translate.create_record()
    assert(True)


if __name__ == "__main__":
    print "Running Translate in stand-alone-mode"

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    translate = Translate()
    translate.process()

