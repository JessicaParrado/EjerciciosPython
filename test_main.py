import unittest

from main import conocerCaracter

class Test(unittest.TestCase):
    def test_conocer_Caracter(self):
        self.assertEqual("Cr",conocerCaracter("Computador"))

if __name__== '__main__':
    unittest.main()