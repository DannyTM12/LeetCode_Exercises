class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # The idea is to iterate through the list of numbers and keep track of the start of each range. When we find a number that is not consecutive, we add the current range to the result list and update the start to the current number. Finally, we handle the last range after the loop.
        result = []
        # Check if the input list is empty
        if not nums:
            return result

        # Initialize the start of the first range
        start = nums[0]
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1: # Check if the current number is not consecutive
                if start == nums[i - 1]: # If the start is the same as the previous number, it means we have a single number range
                    result.append(str(start)) # Add the single number to the result list
                else: # If the start is different from the previous number, it means we have a range of numbers
                    result.append(str(start) + '->' + str(nums[i - 1])) # Add the range to the result list
                start = nums[i] # Update the start to the current number

        # Handle the last range after the loop
        if start == nums[-1]: # If the start is the same as the last number, it means we have a single number range
            result.append(str(start))
        else: # If the start is different from the last number, it means we have a range of numbers
            result.append(str(start) + '->' + str(nums[-1]))

        # Return the result list containing all the ranges
        return result