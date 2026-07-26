"""
Binary search explanation:
This program performs binary search on a sorted list.
It repeatedly splits the list in half and checks the middle value to find the target.

This is much faster than checking every item one by one when the list is large.
"""


def binarySearchIndexAndComparisons(L, k):
    """
    Search for value k in a sorted list L using binary search.
    
    Binary search works by:
    1. Looking at the middle element
    2. If it's k, we found it!
    3. If k is smaller, search the left half
    4. If k is larger, search the right half
    5. Repeat until we find k or run out of elements
    
    Args:
        L: A sorted list of elements (must be in ascending order)
        k: The value to search for
        
    Returns:
        A tuple (found, comparisons) where:
        - found: True if k was found, False otherwise
        - comparisons: The number of times we compared elements
    """
    # Set up the search range
    left = 0
    right = len(L) - 1  # Last valid index
    numComparisons = 0

    # Continue searching while there are elements to check
    while left <= right:
        numComparisons += 1  # Count this comparison
        
        # Find the middle element (use integer division)
        mid = (left + right) // 2

        # Check if the middle element is our target
        if L[mid] == k:
            return (True, numComparisons)
        # If target is greater, ignore the left half
        elif L[mid] < k:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # If we exit the loop, k was not found
    return (False, numComparisons)
