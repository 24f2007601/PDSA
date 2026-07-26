
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
        """
        Create a new node for the linked list.
        
        Args:
            v: The value to store in this node. If None, this is an empty node.
        """
        self.value = v
        self.next = None

    def isempty(self):
        """
        Check if this node is empty.
        
        A node is considered empty when it does not hold a value (value is None).
        
        Returns:
            True if this node's value is None, False otherwise.
        """
        return self.value is None

    def append(self, v):
        """
        Add a new value to the end of the linked list.
        
        Args:
            v: The value to add to the list
        """
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
        """
        Remove a value from the linked list.
        
        Args:
            v: The value to remove from the list
        """
        # If the list is empty, there is nothing to remove.
        if self.isempty():
            return

        # If the current node contains the target value, remove it.
        if self.value == v:
            self.value = None
            # If there's a next node, copy its value and link to its next
            # This effectively removes the current node by skipping over it
            if self.next is not None:
                self.value = self.next.value
                self.next = self.next.next
            return

        # Otherwise, continue searching in the next node.
        else:
            if self.next is not None:
                self.next.delete(v)
                # After deletion, if the next node became empty, remove it
                if self.next.value is None:
                    self.next = None
        return 
    




        
    