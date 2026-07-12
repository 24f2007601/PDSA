"""
In-place merge explanation:
This program merges two sorted lists while keeping the data sorted in both structures.
It compares values from list A with the smallest value in list B and swaps them when needed.

The idea is to keep both lists sorted without creating a completely new merged list.
"""


def mergeInPlace(A, B):
    n = len(A)
    m = len(B)

    # Iterate through every element of A.
    for i in range(n):
        # If the current element in A is greater than the smallest element in B,
        # swap them so the smaller value goes into A.
        if A[i] > B[0]:
            A.swap(i, B, 0)

            # Re-sort B so its first element is in the correct position.
            first = B[0]
            k = 1
            while k < m and B[k] < first:
                B.swap(k - 1, B, k)
                k += 1
