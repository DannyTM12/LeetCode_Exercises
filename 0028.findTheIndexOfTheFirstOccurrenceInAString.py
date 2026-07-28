class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Iterate through the haystack string
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches the needle
            if haystack[i:i + len(needle)] == needle: # It checks from the current index i to the length of the needle if it matches the needle
                # return the index of the first occurrence
                return i
        # If the needle is not found, return -1
        return -1