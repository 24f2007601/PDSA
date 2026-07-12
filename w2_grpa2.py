"""
Rotated array explanation:
This program finds the largest value in a rotated sorted array.
A rotated sorted array is a sorted list that has been shifted to the left or right.

The program uses binary search to reduce the number of comparisons and quickly find the maximum.
"""


def findLargest(L):
    low = 0
    high = len(L) - 1

    # If the list is not rotated or has only one element, the last element is the largest.
    if L[low] <= L[high]:
        return L[high]

    while low <= high:
        mid = (low + high) // 2

        # If the middle element is larger than the next one, mid is the maximum.
        if mid < len(L) - 1 and L[mid] > L[mid + 1]:
            return L[mid]

        # If the middle element is smaller than the previous one, the previous one is the maximum.
        if mid > 0 and L[mid] < L[mid - 1]:
            return L[mid - 1]

        # Decide which half still contains the maximum.
        if L[mid] > L[low]:
            low = mid + 1
        else:
            high = mid - 1

    return L[low]
