#!/usr/bin/python3

import unittest
from unittest.mock import patch
import os
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    ''' Test the console module'''
    @classmethod
    def setUpClass(cls):
        '''setup for the test'''
        cls.consol = HBNBCommand()

    @classmethod
    def tearDown(cls):
        '''at the end of the test this will tear it down'''
        del cls.consol

    def create(self):
        '''creates an instance of HBNBCommand'''
        return HBNBCommand()

    def test_create(self):
        '''tests the create command'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create gggg")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create\
                    Place name="California" house=666.gfd game="666.gfd"')
            output = f.getvalue()
            self.consol.onecmd('show Place {}'.format(output))
            self.assertIn("'name': 'California'", f.getvalue())
            self.assertIn("'game': '666.gfd'", f.getvalue())
            self.assertNotIn("'house': '666.gfd'", f.getvalue())
            self.assertNotIn("'house': '666.gfd'", f.getvalue())
