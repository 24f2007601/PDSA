"""Module to find the K-th element in two sorted lists."""

from typing import Union

Number = Union[int, float]


def KthElement(A: list[Number], B: list[Number], k: int) -> Number:
    """Return the k-th (1-indexed) element in the sorted merged list of A and B.

    Time Complexity: O(log(min(n, m)))
    Space Complexity: O(1)
    """
    n, m = len(A), len(B)

    # Ensure A is smaller so binary search runs in O(log(min(n, m)))
    if n > m:
        return KthElement(B, A, k)

    # Calculate search range for elements taken from array A
    low = max(0, k - m)  # Minimum elements we must pick from A
    high = min(k, n)     # Maximum elements we can pick from A

    while low <= high:
        count_a = (low + high) // 2  # Elements taken from array A
        count_b = k - count_a        # Remaining elements taken from array B

        # Boundary values for left and right elements around partition
        left_a = A[count_a - 1] if count_a > 0 else float("-inf")
        right_a = A[count_a] if count_a < n else float("inf")

        left_b = B[count_b - 1] if count_b > 0 else float("-inf")
        right_b = B[count_b] if count_b < m else float("inf")

        # Valid partition found: max of left side is the k-th element
        if left_a <= right_b and left_b <= right_a:
            return max(left_a, left_b)

        # Adjust search range based on partition comparison
        if left_a > right_b:
            high = count_a - 1  # Too many elements from A
        else:
            low = count_a + 1   # Too few elements from A

    raise ValueError("Input lists or k out of bounds.")
