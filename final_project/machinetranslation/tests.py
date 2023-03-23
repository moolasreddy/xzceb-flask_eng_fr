import unittest

from . translator import englishToFrench, frenchToEnglish

class englishToFrenchTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertEqual(englishToFrench("Welcome"),"Bienvenue")
        self.assertEqual(englishToFrench("End"),"Fin")

class frenchToEnglishTest(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertEqual(frenchToEnglish("Bienvenue"),"Welcome")
        self.assertEqual(frenchToEnglish("Fin"),"End")

unittest.main()
