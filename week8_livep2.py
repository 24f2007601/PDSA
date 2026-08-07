"""Module to find the K-th element in two sorted lists."""

from typing import Union

Number = Union[int, float]


def KthElement(A: list[Number], B: list[Number], k: int) -> Number:
    """Return the k-th (1-indexed) element in the sorted merged list of A and B.

    Time Complexity: O(log(min(n, m)))
    Space Complexity: O(1)
    """
    n = len(A)
    m = len(B)

    if n > m:
        return KthElement(B, A, k)

    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        count_a = (low + high) // 2
        count_b = k - count_a

        left_a = A[count_a - 1] if count_a > 0 else float("-inf")
        right_a = A[count_a] if count_a < n else float("inf")

        left_b = B[count_b - 1] if count_b > 0 else float("-inf")
        right_b = B[count_b] if count_b < m else float("inf")

        if left_a <= right_b and left_b <= right_a:
            return max(left_a, left_b)

        if left_a > right_b:
            high = count_a - 1
        else:
            low = count_a + 1

    raise ValueError("Input lists or k out of bounds.")
