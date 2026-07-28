class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        ans = '' # this will hold the longest common prefix found so far
        strs = sorted(strs)  # we sort the list of strings to bring similar prefixes together, making it easier to find the common prefix
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(last), len(first))):  # we iterate through the characters of the first and last strings in the sorted list, comparing them character by character
            if first[i] == last[i]: # if the characters at the current index are the same, we add that character to our answer
                ans += first[i]
            else: # if the characters differ, we break out of the loop as we have found the longest common prefix
                return ans

        return ans # if we finish the loop without breaking, it means the entire first string is a common prefix, so we return it