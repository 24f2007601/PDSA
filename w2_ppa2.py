"""
Counting Sort explanation:
This program sorts numbers that are in a small known range, such as 0 to r-1.
It counts how many times each value appears and then rebuilds the list in sorted order.

This is faster than comparison-based sorting when the range is small.
"""


def sortInRange(L, r):
    """
    Sorts a list L of integers in place, where all elements are in the range [0, r).
    Achieves O(n + r) time complexity using Counting Sort logic.
    """

    count = [0] * r

    # Count how many times each value appears.
    for num in L:
        count[num] += 1

    # Rebuild the list in sorted order.
    insert_idx = 0
    for i in range(r):
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