
"""
Linked List explanation:
This file shows a simple linked list implementation.
A linked list stores data as nodes, where each node points to the next node.
It is useful when you want to insert or remove items dynamically without shifting
all elements like in a normal Python list.

The methods in this file allow us to:
- check whether the list is empty,
- add a new value,
- remove a value.
"""


class ListNode:
    def __init__(self, v=None):
        self.value = v
        self.next = None

    def isempty(self):
        # A node is considered empty when it does not hold a value.
        return self.value is None

    def append(self, v):
        # If this node is empty, store the new value here.
        if self.isempty():
            self.value = v
        # If there is no next node yet, create one.
        elif self.next is None:
            self.next = ListNode(v)
        # Otherwise, move to the next node and repeat the process.
        else:
            self.next.append(v)

        return

    def delete(self, v):
        # If the list is empty, there is nothing to remove.
        if self.isempty():
            return

        # If the current node contains the target value, remove it.
        if self.value == v:
            self.value = None
            if self.next is not None:
                self.value = self.next.value
                self.next = self.next.next
            return

        # Otherwise, continue searching in the next node.
        else:
            if self.next is not None:
                self.next.delete(v)
                if self.next.value is None:
                    self.next = None
        return 
    




        
    