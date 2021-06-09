#! /usr/bin/env python3

# Author: Dennis Chukwunta (c) 2021
# Email: chuksmcdennis@yahoo.com
# Gmail: chuksmcdennis11@gmail.com

''' Hash Table using only Python lists '''

from collections import namedtuple
import itertools

Entry = namedtuple('Entry', ['key', 'value'])


class Table:
    ''' A Python Hash Table 
    To use
    >>> ht = Table()
    >>> ht["one"] =  1
    >>> ht["one"]
    1
    >>> len(ht)
    1
    >>> del ht["one"]
    >>> len(ht)
    0

    '''

    def __init__(self, size=8, load_factor=0.8):
        ''' Initialize a Hash Table with an initial size of 8, a load factor of 0.8 '''
        self._slots = [[] for _ in range(size)]
        self._size = 0
        self._load_factor = load_factor

    def __len__(self):
        ''' A method that returns the number of items in the table '''
        return self._size

    @staticmethod
    def _index(key, slots):
        ''' A method to handle indexing a key using unique hashing 
        Args:
            key
            slots
        Return:
           Unique hash for key 
        '''
        return hash(key) % len(slots)

    def __setitem__(self, key, value):
        ''' A method to handle adding new items to the Table '''
        index = self._index(key, self._slots)
        slot = self._slots[index]

        for item_index, item in enumerate(slot):
            if item.key == key:
                slot[item_index] = item._replace(value=value)
                break

        # When the for loop is not executed it means this slot is currently empty
        else:
            entry = Entry(key, value)
            self._slots[index].append(entry)
            self._size += 1

        # The _resize method is triggered when ever the load factor is reached to create more available slots
        if len(self)/len(self._slots) >= self._load_factor:
            self._resize()

    @classmethod
    def _insert(cls, slots, key, value):
        ''' A class method for implementing an insert into the newly resized larger slots. '''
        index = cls._index(key, slots)
        entry = Entry(key, value)
        slots[index].append(entry)

    def items(self):
        ''' A method that generates every item in the Table '''
        yield from itertools.chain.from_iterable(self._slots)

    def _resize(self):
        ''' A method for resizing the Table to 2 times it's original avaliable slots. '''
        larger_slots = [[] for i in range(len(self._slots)*2)]

        for key, value in self.items():
            Table._insert(larger_slots, key, value)
        self._slots = larger_slots

    def __getitem__(self, key):
        ''' A method for getting an item from the table using it's key '''
        index = self._index(key, self._slots)

        for element in self._slots[index]:
            if element.key == key:
                return element.value

        # If the key is not an item in the Table.
        raise KeyError(key)

    def __delitem__(self, key):
        ''' A method for handling deleting an Item from the table using it's key '''
        index = self._index(key, self._slots)
        slot = self._slots[index]

        for item_index, item in enumerate(slot):
            if item.key == key:
                del slot[item_index]
                break

        # If the key is not present
        else:
            raise KeyError(key)
        self._size -= 1
