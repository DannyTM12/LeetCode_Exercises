class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums.sort() # Sort the list to bring duplicates together

        if len(nums) == 1: # If there's only one element, return it
            return nums[0]

        for i in range(len(nums)): 
            if i == 0: # If it's the first element, check if it's different from the next one
                if nums[i] != nums[i + 1]:
                    return nums[i] # Return the first element if it's unique
                else:
                    continue
            elif nums[i] == nums[-1]: # If it's the last element, check if it's different from the previous one
                if nums[i] != nums[i - 1]:
                    return nums[i] # Return the last element if it's unique
                else:
                    continue
            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]: # Check if the current element is different from both its neighbors
                    return nums[i] # Return the unique element if found