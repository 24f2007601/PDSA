"""
Stack explanation:
A stack is a data structure that follows the Last In, First Out (LIFO) rule.
The last item added is the first one removed.

This file uses a Python list to implement a simple stack with methods to:
- check whether it is empty,
- add an item,
- remove an item.
"""


class Stack:
    """A simple stack implementation using a list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def isEmpty(self):
        """Check if the stack is empty."""
        return self.stack == []

    def push(self, val):
        """Add an element to the top of the stack."""
        self.stack.append(val)

    def pop(self):
        """Remove and return the top element from the stack."""
        val = None
        if not self.isEmpty():
            val = self.stack.pop()
        return val

    def __str__(self):
        return str(self.stack)


S = Stack()
print(S)

S.push(10)
print(S)

S.push(35)
print(S)

S.pop()
print(S)