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
        # Create a temporary list to help with merging
        # This list will store the merged results before copying back to nums
        temp = [0] * len(nums)

        def merge_sort(left: int, right: int):
            """
            Recursively sort the portion of nums from index 'left' to 'right'.
            
            Args:
                left: Starting index of the portion to sort
                right: Ending index of the portion to sort
            """
            # Base case: if left >= right, there's only one or zero elements
            if left >= right:
                return

            # Find the middle index
            mid = left + (right - left) // 2

            # Sort the left half (from left to mid)
            merge_sort(left, mid)
            # Sort the right half (from mid+1 to right)
            merge_sort(mid + 1, right)

            # Merge the two sorted halves
            i = left        # Pointer for left half
            j = mid + 1     # Pointer for right half
            k = left        # Pointer for the merged result

            # Compare elements from both halves and place the smaller one first
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            # If there are remaining elements in the left half, copy them
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            # If there are remaining elements in the right half, copy them
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1

            # Copy the merged elements back to the original array
            for idx in range(left, right + 1):
                nums[idx] = temp[idx]

        # Start sorting from the beginning (index 0) to the end (len-1)
        merge_sort(0, len(nums) - 1)
        return nums


# Example usage:
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]