import unittest

from main import conocerEdad

class Test(unittest.TestCase):
    def test_conocer_edad(self):
        self.assertEqual(69,conocerEdad(19,2020))

if __name__== '__main__':
    unittest.main()