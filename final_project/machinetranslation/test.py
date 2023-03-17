import unittest

from translator import englishtofrench, frenchtoenglish

class EnglishToFrenchTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("Welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("End"),"Fin")

class FrenchToEnglishTest(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertEqual(frenchtoenglish("Bienvenue"),"Welcome")
        self.assertEqual(frenchtoenglish("Fin"),"End")

unittest.main()
