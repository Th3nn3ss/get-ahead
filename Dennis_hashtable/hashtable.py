#! /usr/bin/env python3

# Author: Dennis Chukwunta (c) 2021
# Email: chuksmcdennis@yahoo.com
# Gmail: chuksmcdennis11@gmail.com

''' An attempt at a simple Hash Table using only Arrays(lists) '''

from collections import namedtuple
import itertools

Item = namedtuple('Item', ['key', 'value'])


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
        for item_index, item in enumerate(this_slot):
            if item.key == key:
                this_slot[item_index] = item._replace(value=value)
                break
        else:
            item = Item(key, value)
            self._slots[index].append(item)
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
        for item_index, item in enumerate(this_slot):
            if item.key == key:
                del this_slot[item_index]
                break
        else:
            return "'{}' is not a key in this HashTable".format(key)
        self._count = self._count - 1
