"""Python version of Module providingFunction."""
import unittest

from . translator import englishtofrench, frenchtoenglish

class EnglishToFrenchTest(unittest.TestCase):
    """Class representing a TestCase"""
    def test1(self):
        """    Add the values in ``self``"""
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("Welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("End"),"Fin")

class FrenchToEnglishTest(unittest.TestCase):
    """Class representing a TestCase"""
    def test2(self):
        """    Add the values in ``self``"""
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertEqual(frenchtoenglish("Bienvenue"),"Welcome")
        self.assertEqual(frenchtoenglish("Fin"),"End")

unittest.main()
