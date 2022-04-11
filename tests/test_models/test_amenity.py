#!/usr/bin/python3
"""unittests for amenity.py.
Unittest classes:
    Test_Amenity_Docs
    Test_Amenity_All
"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class Test_Amenity_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_style_check(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
