#! /usr/bin/env python3

# Author: Dennis Chukwunta (c) 2021
# Email: chuksmcdennis@yahoo.com

''' An attempt at a simple Hash Table using only Arrays(lists) '''

from collections import namedtuple
import itertools

Entry = namedtuple('Entry', ['key', 'value'])


class HashTable:
    ''' A HashTable implementation the handles collision and dynamic resizing
    '''

    def __init__(self, size=8, load_factor=0.8):
        self._slots = [[] for i in range(size)]
        self._count = 0
        self._load_factor = load_factor

    def __len__(self):
        return self._count

    def _index(self, key):
        return hash(key) % len(self._slots)

    def add_item(self, key, value):
        index = self._index(key)
        this_slot = self._slots[index]
        for entry_index, entry in enumerate(this_slot):
            if entry.key == key:
                this_slot[entry_index] = entry._replace(value=value)
                break
        else:
            entry = Entry(key, value)
            self._slots[index].append(entry)
            self._count = self._count + 1
        if len(self)/len(self._slots) >= self._load_factor:
            self._resize()

    @classmethod
    def _insert(cls, slots, key, value):
        index = cls._index(key, slots)
        slots[index] = value

    def _resize(self):
        larger_slots = [[] for i in range(len(self._slots)*2)]
        for key, value in self.items():
            HashTable._insert(larger_slots, key, value)
        self._slots = larger_slots

    def get_item(self, key):
        index = self._index(key)
        for element in self._slots[index]:
            if element.key == key:
                return element.value
        return "'{}' is not a key in this HashTable".format(key)

    def del_item(self, key):
        index = self._index(key)
        this_slot = self._slots[index]
        for entry_index, entry in enumerate(this_slot):
            if entry.key == key:
                del this_slot[entry_index]
                break
        else:
            return "'{}' is not a key in this HashTable".format(key)
        self._count = self._count - 1


hasher = HashTable()
hasher.add_item("one", 1)
hasher.add_item("two", 2)
hasher.add_item("one", 3)
print(len(hasher))
print(hasher._slots)
