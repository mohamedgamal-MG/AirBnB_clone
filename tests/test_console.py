#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            self.console.onecmd("EOF")
        except SystemExit:
            pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel 123 name John")
            output = fake_out.getvalue().strip()
            self.assertTrue(output != "")

if __name__ == '__main__':
    unittest.main()
