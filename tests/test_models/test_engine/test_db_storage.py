#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from models.engine.db_storage import DBStorage
import pep8
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "skip to make this test only works on DBStorage")
class Test_DB_Storage(unittest.TestCase):
    """ Class to test the DBStorage"""


class Test_DB_Storage_Docs(unittest.TestCase):
    """Test documentation"""

    def test_doc_DB(self):
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def test_style_check_DB(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUp(cls):
        """ Set up test environment """
        cls.user = User()
        pass

    @classmethod
    def tearDown(cls):
        """ Remove storage file at end of tests """
        del cls.user


if __name__ == "__main__":
    unittest.main()
