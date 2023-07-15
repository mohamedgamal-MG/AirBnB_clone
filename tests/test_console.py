#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show("BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy("BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all("")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_count("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update("BaseModel 123 name John")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

if __name__ == '__main__':
    unittest.main()
