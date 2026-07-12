"""
Combination sort explanation:
This program sorts a list of strings in two different ways.

- L1 sorts items based only on the first letter.
- L2 sorts items by the first letter, and for the same letter, by the number part in reverse.
"""


def combinationSort(strList):
    # Sort by the first character only.
    L1 = sorted(strList, key=lambda x: x[0])

    # Sort by letter ascending, and by the number part descending.
    L2 = sorted(strList, key=lambda x: (x[0], -int(x[1:])))

    return L1, L2


# Example Usage:
input_list = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
L1, L2 = combinationSort(input_list)

print("L1:", ", ".join(L1))
print("L2:", ", ".join(L2))
