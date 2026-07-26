"""
In-place merge explanation:
This program merges two sorted lists while keeping the data sorted in both structures.
It compares values from list A with the smallest value in list B and swaps them when needed.

The idea is to keep both lists sorted without creating a completely new merged list.
The algorithm maintains two sorted arrays A and B, inserting the smaller element from B
into A while preserving the sorted order in both arrays.
"""


def mergeInPlace(A, B):
    """
    Merge two sorted lists A and B in place.
    
    After the operation, A will contain the smallest elements from both lists,
    and B will contain the remaining (larger) elements.
    
    Args:
        A: A sorted list (will contain the smallest combined elements)
        B: A sorted list (will contain the largest combined elements)
    """
    n = len(A)  # Number of elements in A
    m = len(B)  # Number of elements in B

    # Iterate through every element of A
    for i in range(n):
        # If the current element in A is greater than the smallest element in B,
        # swap them so the smaller value goes into A
        if A[i] > B[0]:
            # Swap the element at A[i] with the smallest element in B
            A.swap(i, B, 0)

            # Re-sort B so its first element is in the correct position
            # We need to bubble the smaller value we just got from A
            # to its proper position in B
            first = B[0]
            k = 1
            while k < m and B[k] < first:
                # Shift each element left until we find the right spot
                B.swap(k - 1, B, k)
                k += 1
