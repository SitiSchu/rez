# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Rez Project


"""
unit tests for 'utils.py23' module
"""
import os
import sys

from rez.tests.util import TestBase
from rez.utils import py23


class TestLoadModuleFromFile(TestBase):
    def test_load_module(self):
        """Ensure that the imported module does not show up in sys.modules"""
        include_path = self.data_path('python', 'include')
        # Random chars are used in the module name to ensure that the module name is unique
        # and the test won't fail because some other module with the same name
        # shows up in sys.modules
        module = 'utils_test_7cd3a335'
        py23.load_module_from_file(
            module,
            os.path.join(include_path, '{}.py'.format(module))
        )
        self.assertEqual(sys.modules.get(module), None, msg='Module was found in sys.modules')
