"""
Rotated array explanation:
This program finds the largest value in a rotated sorted array.
A rotated sorted array is a sorted list that has been shifted to the left or right.

Example of rotation:
- Original sorted array: [1, 2, 3, 4, 5]
- After rotating once to the left: [2, 3, 4, 5, 1]
- After rotating twice to the left: [3, 4, 5, 1, 2]

The program uses binary search to reduce the number of comparisons and quickly find the maximum.
The key insight is that in a rotated sorted array, one half is always sorted,
and the maximum is always at the point of rotation.
"""


def findLargest(L):
    """
    Find the largest element in a rotated sorted array.
    
    A rotated sorted array is a sorted array that has been rotated at some pivot point.
    The largest element is at the pivot where the rotation occurred.
    
    Args:
        L: A rotated sorted array (sorted in ascending order, then rotated)
        
    Returns:
        The largest element in the array
    """
    low = 0
    high = len(L) - 1

    # Special case: If the array is not rotated or has only one element,
    # the last element is the largest
    # (This handles the case where L[low] <= L[high] means array is sorted, not rotated)
    if L[low] <= L[high]:
        return L[high]

    # Use binary search to find the pivot point (where the maximum is)
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Check if mid is the maximum (mid > next element)
        # This means we've found the pivot point
        if mid < len(L) - 1 and L[mid] > L[mid + 1]:
            return L[mid]

        # Check if the previous element is the maximum (mid < previous element)
        # This means the pivot is at mid-1
        if mid > 0 and L[mid] < L[mid - 1]:
            return L[mid - 1]

        # Decide which half contains the maximum:
        # If the left half is sorted (L[mid] > L[low]), the maximum is in the right half
        if L[mid] > L[low]:
            low = mid + 1
        # Otherwise, the maximum is in the left half
        else:
            high = mid - 1

    # This should never happen if input is valid, but return the element at low as fallback
    return L[low]
