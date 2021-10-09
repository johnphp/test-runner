import unittest

class TestSatu(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foopaux'.upper(), 'FOOPAUX')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == "__main__":
    unittest.main()


