class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 # Keep track of the longest consecutive sequence
        num_set = set(nums) # Delete duplicates and allow O(1) lookups

        for i in num_set: # Iterate through the set of numbers
            if (i - 1) not in num_set: # If the previous number is not in the set, then this is the start of a sequence
                length = 1 # Initialize the length of the current sequence
                while (i + length) in num_set: # While the next number is in the set, increment the length of the current sequence
                    length += 1
                longest = max(longest, length) # Update the longest sequence if the current sequence is longer

        return longest # Return the length of the longest consecutive sequence found