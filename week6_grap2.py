class Tree:
    """
    Binary Tree Node class.
    
    Each node has:
    - A value (the data stored in the node)
    - A left child (smaller values)
    - A right child (larger values)
    
    An empty tree is represented by a node with value None.
    """
    
    # constructor
    def __init__(self, initval=None):
        """
        Initialize a tree node.
        
        Args:
            initval: The value to store in this node. If None, this is an empty node.
        """
        self.value = initval
        
        # If this node has a value, create empty left and right children
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            # Empty nodes have no children
            self.left = self.right = None
        return

    # Only empty node has value None
    def isempty(self):
        """
        Check if this node is empty (has no value).
        
        Returns:
            True if this node has value None, False otherwise.
        """
        return self.value == None

    # Leaf nodes have both children empty
    def isleaf(self):
        """
        Check if this node is a leaf (has a value but no children).
        
        Returns:
            True if this node has a value AND both children are empty.
        """
        return self.value != None and self.left.isempty() and self.right.isempty()


# insert element to BST
def insertToBST(root, x):
    """
    Insert a value x into the Binary Search Tree rooted at 'root'.
    
    In a BST:
    - Values smaller than the current node go to the left subtree
    - Values larger than or equal to the current node go to the right subtree
    
    Args:
        root: The root node of the BST
        x: The value to insert
    """
    # Start from the root node
    temp = root
    
    # Keep moving down the tree until we find an empty spot
    # Continue while current node is not empty
    while not temp.isempty():
        # If x is smaller than current node's value, go left
        if x < temp.value:
            temp = temp.left
        else:
            # Otherwise, go right
            temp = temp.right

    # We've found an empty spot! Set the value and create its children
    temp.value = x
    temp.left = Tree()
    temp.right = Tree()


def maxLessThan(root, K):
    """
    Find the largest value in the BST that is less than or equal to K.
    
    This is like searching for the "next smallest" value when you have a target.
    
    Args:
        root: The root node of the BST
        K: The target value
        
    Returns:
        The largest value <= K, or None if no such value exists.
    """
    # This will store our answer
    ans = None
    
    # Start from the root
    curr = root

    # Keep searching while we haven't reached an empty node
    while not curr.isempty():
        # If current node's value is less than or equal to K
        if curr.value <= K:
            # This is a valid candidate for our answer!
            ans = curr.value
            
            # But maybe there's a larger value that's still <= K?
            # Let's check the right subtree for a bigger valid value
            curr = curr.right
        else:
            # Current value is too big (greater than K)
            # We need a smaller value, so go left
            curr = curr.left

    # Return the largest value we found that is <= K
    return ans