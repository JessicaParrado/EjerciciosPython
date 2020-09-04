import unittest

from main import conocerCaracter

class Test(unittest.TestCase):
    def test_conocer_Caracter(self):
        self.assertEqual("ba",conocerCaracter("banana"))

if __name__== '__main__':
    unittest.main()