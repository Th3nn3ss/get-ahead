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
    # An init function with an initial size of 8
    # With a load factor of 0.8, which is 80% of the current number of slots

    def __init__(self, size=8, load_factor=0.8):
        self._slots = [[] for i in range(size)]
        self._count = 0  # To keep count of the number of Table items
        self._load_factor = load_factor

    # A method that returns the number of items in the table
    def __len__(self):
        return self._count

    # A method to handle indexing a key using unique hashing

    def _index(self, key):
        return hash(key) % len(self._slots)

    # A method to handle adding new items to the Table
    # It also takes care of handling collisions when two key's are of the same hashed index

    def add_item(self, key, value):
        index = self._index(key)
        this_slot = self._slots[index]
        for item_index, item in enumerate(this_slot):
            if item.key == key:
                this_slot[item_index] = item._replace(value=value)
                break
        # when the for loop is not executed it means this slot is currently empty
        # the else clause appends the (key, value) item to the slot.
        else:
            item = Item(key, value)
            self._slots[index].append(item)
            self._count = self._count + 1  # Count is increased by 1

        # The _resize method is triggered when ever the load factor is reached or passed.
        # This is to create more available slots when the capacity is at 80%
        if len(self)/len(self._slots) >= self._load_factor:
            self._resize()

    # A class method for implementing an insert into the newly resized larger slots.

    @classmethod
    def _insert(cls, slots, key, value):
        index = cls._index(key, slots)
        slots[index] = value

    # A Generator method that generates every item in the Table
    def items(self):
        yield from itertools.chain.from_iterable(self._slots)

    # A method for resizing the Table to 2 times it's original avaliable slots.

    def _resize(self):
        larger_slots = [[] for i in range(len(self._slots)*2)]
        for key, value in self.items():
            HashTable._insert(larger_slots, key, value)
        self._slots = larger_slots

    # A method for getting an item from the table using it's key
    def get_item(self, key):
        index = self._index(key)
        for element in self._slots[index]:
            if element.key == key:
                return element.value

        # If the key is not an item in the Table.
        # A personallized error message is returned.
        return "'{}' is not a key in this HashTable".format(key)

    # A method for handling deleting an Item from the table using it's key

    def del_item(self, key):
        index = self._index(key)
        this_slot = self._slots[index]
        for item_index, item in enumerate(this_slot):
            if item.key == key:
                del this_slot[item_index]
                break
        # If the key is not an item in the Table.
        # A personallized error message is returned.
        else:
            return "'{}' is not a key in this HashTable".format(key)
        self._count = self._count - 1  # Count is decreased by 1.
