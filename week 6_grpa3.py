"""
Max Heap Construction explanation:
This program builds a max heap from an unsorted array.

A max heap is a special binary tree where:
1. Every parent node is larger than or equal to its children
2. The largest element is always at the root (index 0)

The heapify procedure:
1. Start from the last internal node (the parent of the last leaf)
2. Work backwards to the root
3. For each node, ensure it's larger than its children
   If not, swap it with the larger child and continue down the tree

This is called "bottom-up heap construction" and is very efficient!
"""


def min_max(arr):
    """
    Transform the input array into a max heap in place.
    
    Args:
        arr: List of numbers to convert into a max heap
    """
    n = len(arr)
    
    def max_heapify(i):
        """
        Ensure the subtree rooted at index i satisfies the max heap property.
        
        This function assumes the subtrees of node i are already valid max heaps.
        
        Args:
            i: Index of the root of the subtree to heapify
        """
        # Start by assuming the current node (i) is the largest
        largest = i
        
        # Calculate indices of left and right children
        # For a node at index i:
        #   Left child is at index 2*i + 1
        #   Right child is at index 2*i + 2
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if left child exists and is larger than the current largest
        # We need to verify left < n to ensure it's within array bounds
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        # Check if right child exists and is larger than the current largest
        # We need to verify right < n to ensure it's within array bounds
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        # If the largest value is not at the current position, we need to swap
        if largest != i:
            # Swap the current node with the larger child
            arr[i], arr[largest] = arr[largest], arr[i]
            
            # After swapping, the subtree rooted at 'largest' might no longer
            # satisfy the heap property. Recursively heapify that subtree!
            max_heapify(largest)

    # Build a max heap from the bottom-up
    # We start from the last internal node and work backwards to the root
    
    # Last internal node is at index (n // 2) - 1
    # (All nodes after this are leaves and don't need heapifying)
    # Loop backwards from last internal node to index 0
    for i in range((n // 2) - 1, -1, -1):
        # Ensure the subtree rooted at index i is a valid max heap
        max_heapify(i)
