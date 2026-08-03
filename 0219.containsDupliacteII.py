class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} # Create a dictionary to store the last index of each number

        # Iterate through the list of numbers
        for i in range(len(nums)):
            if nums[i] not in seen: # If the number is not in the dictionary, add it with its index
                seen[nums[i]] = i
            # If the number is already in the dictionary, check if the difference between the current index and the last index is less than or equal to k
            elif nums[i] in seen:
                if abs(i - seen[nums[i]]) <= k: # If the difference is less than or equal to k, return True
                    return True
                else:
                    seen[nums[i]] = i # Update the last index of the number in the dictionary

        return False # If no duplicates are found within the specified range, return False