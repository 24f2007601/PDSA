class Stack:
    """A simple stack implementation using a list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []


    def isEmpty(self):
        """Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return (self.stack == [])

    def push(self, val):
        """Add an element to the top of the stack.
        
        Args:
            val: The value to push onto the stack.
        """
        self.stack.append(val)

    def pop(self):
        """Remove and return the top element from the stack.
        
        Returns:
            The value at the top of the stack, or None if stack is empty.
        """
        val = None 
        if not self.isEmpty():
            val = self.stack.pop()
        return val
        

    def __str__(self):
        return (str(self.stack))
S = Stack()
print(S)

S.push(10)
print(S)

S.push(35)
print(S)

S.pop()
print(S)


#S.pop()
#print(S.pop())     