#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand

    def get_size(self):
        return self._size

    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        if condition in ("New", "Used"):
            self._condition = condition
        else:
            print("The condition must be either new or used.")

    condition = property(get_condition, set_condition)

    def cobble(self):
        self.set_condition("New")
        print("Your shoe is as good as new!")