import unittest

from main import saberPar

class Test(unittest.TestCase):
    def test_saber_Par(self):
        self.assertEqual(True,saberPar(16))

if __name__== '__main__':
    unittest.main()