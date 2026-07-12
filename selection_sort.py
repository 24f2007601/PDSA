"""
Selection Sort explanation:
This program repeatedly finds the smallest value in the unsorted part of the list and
places it at the front.

How it works:
1. Assume the first position is the smallest.
2. Compare it with the rest of the list.
3. If a smaller value is found, swap it into place.
4. Repeat until the list is fully sorted.

This algorithm is simple but not the fastest for large lists.
"""


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Go through each position in the list.
        for i in range(n):
            # Assume the current position holds the smallest value for now.
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            # Put the smallest value found into its correct position.
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums


# Example usage:
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]