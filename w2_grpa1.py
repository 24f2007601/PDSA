"""
Combination sort explanation:
This program sorts a list of strings in two different ways.

- L1 sorts items based only on the first letter.
- L2 sorts items by the first letter, and for the same letter, by the number part in reverse.

Example input: ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
- L1 output: sorted alphabetically by first letter
- L2 output: sorted by first letter, then by number (descending) within each letter group
"""


def combinationSort(strList):
    """
    Sort a list of strings in two different ways.
    
    Args:
        strList: A list of strings where each string starts with a letter followed by digits
                 Example: ["d34", "g54", "d12"]
                 
    Returns:
        A tuple (L1, L2) where:
        - L1: Sorted by first letter only (alphabetically)
        - L2: Sorted by first letter (ascending), then by number part (descending)
    """
    # Sort by the first character only.
    # key=lambda x: x[0] means use only the first character for comparison
    L1 = sorted(strList, key=lambda x: x[0])

    # Sort by letter ascending, and by the number part descending.
    # key=lambda x: (x[0], -int(x[1:])) creates a tuple for sorting:
    # - x[0]: first letter, sorted in ascending order (a, b, c...)
    # - -int(x[1:]): negative of the number part, sorted in descending order
    #   The negative sign flips the order so larger numbers come first
    L2 = sorted(strList, key=lambda x: (x[0], -int(x[1:])))

    return L1, L2


# Example Usage:
input_list = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
L1, L2 = combinationSort(input_list)

print("L1:", ", ".join(L1))
print("L2:", ", ".join(L2))
