"""
Counting Sort explanation:
This program sorts numbers that are in a small known range, such as 0 to r-1.
It counts how many times each value appears and then rebuilds the list in sorted order.

This is faster than comparison-based sorting when the range is small.
"""


def sortInRange(L, r):
    """
    Sorts a list L of integers in place, where all elements are in the range [0, r).
    Uses Counting Sort algorithm which achieves O(n + r) time complexity.
    
    Args:
        L: List of integers to sort (all values must be in range [0, r))
        r: The upper bound of the range (exclusive), so valid values are 0 to r-1
    """

    # Create a count array of size r, initialized with zeros
    # count[i] will store how many times the value i appears in L
    count = [0] * r

    # Count how many times each value appears
    for num in L:
        count[num] += 1

    # Rebuild the list in sorted order
    # We iterate through all possible values from 0 to r-1
    insert_idx = 0  # Current position to insert in L
    for i in range(r):
        # For each value i, if it appeared count[i] times in L,
        # place it count[i] times in L starting at insert_idx
        while count[i] > 0:
            L[insert_idx] = i
            insert_idx += 1
            count[i] -= 1


if __name__ == "__main__":
    L = [2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2]
    r = 4

    print(f"Original L: {L}")

    sortInRange(L, r)

    print(f"Sorted L:   {L}")