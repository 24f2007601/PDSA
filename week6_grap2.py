class Tree:
    # constructor
    def __init__(self, initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = self.right = None
        return

    # Only empty node has value None
    def isempty(self):
        return self.value == None

    # Leaf nodes have both children empty
    def isleaf(self):
        return self.value != None and self.left.isempty() and self.right.isempty()


# insert element to BST
def insertToBST(root, x):
    # Tree should have at least one element.
    temp = root
    while not temp.isempty():
        if x < temp.value:
            temp = temp.left
        else:
            temp = temp.right

    temp.value = x
    temp.left = Tree()
    temp.right = Tree()


def maxLessThan(root, K):
    ans = None
    curr = root

    while not curr.isempty():
        if curr.value <= K:
            ans = curr.value  # Found a valid candidate <= K
            curr = curr.right # Look for a larger valid candidate in right subtree
        else:
            curr = curr.left  # Current value is too big, move left

    return ans