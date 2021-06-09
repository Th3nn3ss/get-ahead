#! /usr/bin/env python3

''' Test for the Table class using unittest '''


import unittest
from hashtable import Table


class TestTable(unittest.TestCase):

    # Initialize an object name hasher
    def setUp(self):
        self.hasher = Table()

    # Test for Add Item method and Delete method.
    def test_add_item(self):
        self.hasher["one"] = 1
        self.assertEqual(self.hasher["one"], 1)
        self.hasher["one"] = "unos"
        self.assertEqual(self.hasher["one"], "unos")

    # Test for Add Item method and Get Item method
    def test_del(self):
        self.hasher["two"] = 2
        self.hasher["three"] = 3
        del self.hasher["two"]
        with self.assertRaises(KeyError):
            self.hasher["two"]

    # Test for length, Add Item and Delete Item methods

    def test_len(self):
        self.hasher["ten"] = 10
        self.hasher[10] = "ten"
        self.hasher["eleven"] = 11
        self.assertEqual(len(self.hasher), 3)
        del self.hasher[10]
        self.assertEqual(len(self.hasher), 2)

    # Forther tests to check if the resizing is efficient

    def test_resizing_(self):
        array = [1, 2, 3, 4, 5, 5, 2, 3, 2, 3, 2, 3, 2, 3,
                 2, 3, 4, 2, 3, 4, 3, 2, 4, 3, 2, 4, 2, 3, 4, 3]

        for index, value in enumerate(array):
            self.hasher[index] = value

        # Since the initial available slots of the Table is 8
        # Then this test should test if the Table was resized twice
        self.assertEqual(len(self.hasher), 30)

        # To test for every object inserted into the Table
        for index, value in enumerate(array):
            self.assertEqual(self.hasher[index], value)


if __name__ == "__main__":
    unittest.main()
