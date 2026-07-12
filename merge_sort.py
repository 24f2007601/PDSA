"""
Merge Sort explanation:
This program uses the divide-and-conquer strategy.
It splits the list into smaller halves, sorts each half, and then merges them back
into one sorted list.

Why this is useful:
- Very efficient for large lists.
- Works well for both small and large datasets.
- Has predictable performance of O(n log n).
"""


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        temp = [0] * len(nums)

        def merge_sort(left: int, right: int):
            if left >= right:
                return

            mid = left + (right - left) // 2

            # Sort the left half.
            merge_sort(left, mid)
            # Sort the right half.
            merge_sort(mid + 1, right)

            i = left
            j = mid + 1
            k = left

            # Merge the two sorted halves into one sorted section.
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            # Copy the remaining values from the left half.
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            # Copy the remaining values from the right half.
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1

            # Write the merged values back into the original list.
            for idx in range(left, right + 1):
                nums[idx] = temp[idx]

        merge_sort(0, len(nums) - 1)
        return nums


# Example usage:
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]