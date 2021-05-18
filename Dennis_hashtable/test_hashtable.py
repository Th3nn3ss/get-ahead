#! /usr/bin/env python3

''' Test for the HashTable class using unittest '''


import unittest
from dictionary import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hasher = HashTable()

    def test_add_item(self):
        self.hasher.add_item("one", 1)
        self.assertEqual(self.hasher.get_item("one"), 1)

    def test_del(self):
        self.hasher.add_item("two", 2)
        self.hasher.add_item("three", 3)
        self.hasher.del_item("two")
        self.assertEqual(self.hasher.get_item("two"),
                         "'two' is not a key in this HashTable")

    def test_len(self):
        self.hasher.add_item("ten", 10)
        self.hasher.add_item(10, "ten")
        self.hasher.add_item("eleven", 11)
        self.assertEqual(len(self.hasher), 3)
        self.hasher.del_item(10)
        self.assertEqual(len(self.hasher), 2)


if __name__ == "__main__":
    unittest.main()
