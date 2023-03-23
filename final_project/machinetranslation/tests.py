import unittest

from translator import englishToFrench, frenchToEnglish

class englishToFrenchTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("Welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("End"),"Fin")

class frenchToEnglishTest(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertEqual(frenchtoenglish("Bienvenue"),"Welcome")
        self.assertEqual(frenchtoenglish("Fin"),"End")

unittest.main()
