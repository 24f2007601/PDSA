"""
Insertion Sort explanation:
This program sorts a list by building the final sorted list one element at a time.
It starts with the second item and compares it with the items before it.
If the current item is smaller, it shifts the larger items to the right until the
correct position is found.

Why this is useful:
- Easy to understand.
- Good for small lists.
- Works in-place, so it does not need extra memory.
"""


class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Start from the second element because the first element is already considered sorted.
        for i in range(1, n):
            key = nums[i]

            # Compare the current value with the sorted part on the left.
            # Shift larger values to the right so the key can be placed in its correct spot.
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1

            # Insert the key at the correct position.
            nums[j + 1] = key

        return nums


# Example usage:
solution = Solution()
print(solution.insertionSort([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.insertionSort([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]