class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # If the list is empty, return 0
            return 0

        j = 0  # Pointer for the position of the last unique element

        # This compares each element with the last unique element found
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i] # if a new unique element is found, move it to the next position in the array

        return j + 1 #return the count of unique elements, which is j + 1 since j is zero-indexed