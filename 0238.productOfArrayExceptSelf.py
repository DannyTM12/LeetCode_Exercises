class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Efficient approach to calculate the product of all elements except self without using division
        # Initialize variables:
        length = len(nums) # Length of the input array
        pre = 1 # Product of elements to the left of the current element
        post = 1 # Product of elements to the right of the current element
        result = [0] * length # Initialize the result array with zeroes

        # Example array: nums = [1, 2, 3, 4]
        for i in range(length):
            result[i] = pre # Store the product of elements to the left of the current element
            pre *= nums[i] # Update the product of elements to the left for the next iteration
        # After this loop, result will be [1, 1, 2, 6] which represents the product of elements to the left of each index.

        # Now, we will calculate the product of elements to the right of each index and multiply it with the corresponding left product stored in result.
        for i in range(length - 1, -1, -1):
            result[i] *= post # Multiply the current element with the product of elements to its right
            post *= nums[i] # Update the product of elements to the right for the next iteration
        # This is filled like this:
        # For i = 3: result[3] = 6 * 1 = 6, post = 4 | [1, 1, 2, 6]
        # For i = 2: result[2] = 2 * 4 = 8, post = 12 | [1, 1, 8, 6]
        # For i = 1: result[1] = 1 * 12 = 12, post = 24 | [1, 12, 8, 6]
        # For i = 0: result[0] = 1 * 24 = 24, post = 24 | [24, 12, 8, 6]

        return result # Return the final result array which contains the product of all elements except self for each index.