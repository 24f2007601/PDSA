"""
Minimum difference explanation:
This program finds the smallest difference between the largest and smallest values
when choosing P elements from a list.

It works by sorting the list and then checking every possible group of P elements
using a sliding window.
"""


def find_Min_Difference(L, P):
    # If there are not enough elements, we cannot choose P elements.
    if len(L) < P or P <= 0:
        return 0

    # Sort the list so the window can be checked easily.
    L.sort()

    # Start with a very large value so any real difference will replace it.
    min_diff = float('inf')

    # Slide a window of size P across the sorted list.
    for i in range(len(L) - P + 1):
        current_diff = L[i + P - 1] - L[i]

        # Keep the smallest difference found so far.
        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff


# --- Example Testing ---
L = [3, 4, 1, 9, 56, 7, 9, 12, 13]
P = 5
print("Output:", find_Min_Difference(L, P))  # Expected Output: 6