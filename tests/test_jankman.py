#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jankman
----------------------------------

Tests for `jankman` module.
"""


import sys
import unittest
from contextlib import contextmanager

from click.testing import CliRunner

from jankman import cli


class TestJenkins_manager(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()

        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        self.assertRegex(help_result.output, r'--help.*Show this message and exit.')
