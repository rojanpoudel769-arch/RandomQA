import unittest


class MyTestCase(unittest.TestCase):

    def test_first(self):
        print("This is first test method")
        self.assertEqual(1, 1)

    def test_second(self):
        print("This is second test method")
        self.assertEqual(2, 2)

    @classmethod
    def setUpClass(cls):
        print("This is setup method")

    @classmethod
    def tearDownClass(cls):
        print("This is tear down method")

if __name__ == '__main__':
    unittest.main()