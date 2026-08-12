class Solution:
    def rotateArray(self, nums: List[int], k: int) -> None:

        k %= len(nums) # Handle cases where k is greater than the length of the array
        # For example, if k is 5 and the length of nums is 3, we only need to rotate by 2 positions (5 % 3 = 2).
        nums.reverse() # Reverse the entire array first. 
        # This will help in placing the last k elements at the beginning of the array.

        nums[:k] = reversed(nums[:k]) # Reverse the first k elements to restore their original order.

        nums[k:] = reversed(nums[k:]) # Reverse the remaining elements (from index k to the end) to restore their original order as well.

        # After these three reversals, the array will be rotated to the right by k steps as required.
        # Example: If nums = [1, 2, 3, 4, 5, 6, 7] and k = 3,
        # After reversing the entire array: [7, 6, 5, 4, 3, 2, 1]
        # After reversing the first k elements: [5, 6, 7, 4, 3, 2, 1]
