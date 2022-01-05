#backend.py

from typing import List


items = list()

def create_items(listOfItems):
    global items
    items.append(listOfItems)

def add_item():
    pass

def print_items():
    global items

