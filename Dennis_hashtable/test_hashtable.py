#! /usr/bin/env python3

''' Test for the HashTable class using unittest '''


import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    # Initialize an object name hasher
    def setUp(self):
        self.hasher = HashTable()

    # Test for Add Item method and Delete method.
    def test_add_item(self):
        self.hasher.add_item("one", 1)
        self.assertEqual(self.hasher.get_item("one"), 1)
        self.hasher.add_item("one", "unos")
        self.assertEqual(self.hasher.get_item("one"), "unos")

    # Test for Add Item method and Get Item method
    def test_del(self):
        self.hasher.add_item("two", 2)
        self.hasher.add_item("three", 3)
        self.hasher.del_item("two")
        self.assertEqual(self.hasher.get_item("two"),
                         "'two' is not a key in this HashTable")

    # Test for length, Add Item and Delete Item methods

    def test_len(self):
        self.hasher.add_item("ten", 10)
        self.hasher.add_item(10, "ten")
        self.hasher.add_item("eleven", 11)
        self.assertEqual(len(self.hasher), 3)
        self.hasher.del_item(10)
        self.assertEqual(len(self.hasher), 2)

    # Test the yeild generator as used in the Items method
    def test_items(self):
        self.hasher.add_item("This ", "is ")
        for key, value in self.hasher.items():
            self.assertEqual(key, "This ")
            self.assertEqual(value, "is ")

    # Forther tests to check if the resizing is efficient
    def test_resizing_(self):
        array = [1, 2, 3, 4, 5, 5, 2, 3, 2, 3, 2, 3, 2, 3,
                 2, 3, 4, 2, 3, 4, 3, 2, 4, 3, 2, 4, 2, 3, 4, 3]
        for index, value in enumerate(array):
            self.hasher.add_item(index, value)
        # Since the initial slots of the slot is 8
        # Then is test should test if the slots was resized twice
        self.assertEqual(len(self.hasher), 30)


if __name__ == "__main__":
    unittest.main()
