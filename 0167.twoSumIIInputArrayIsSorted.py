class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This is the same code that I used in Two Sum I, but I only change to a 1-based index instead of a 0-based index.
        hashTable = {}

        for i in range(len(numbers)):
            
            complement = target - numbers[i]

            if complement in hashTable:

                return [hashTable[complement], i + 1] # Return the indices of the two numbers that add up to the target, using 1-based indexing.
            # line 12 and 14 are the same as line 12 and 14 in Two Sum I, but I only change to a 1-based index instead of a 0-based index.
            hashTable[numbers[i]] = i + 1

        return []