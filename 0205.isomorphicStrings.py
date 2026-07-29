class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        
        # Quick check: if the lengths of the two strings are not equal, they cannot be isomorphic
        if len(s) != len(t):
            return False

        # Create two dictionaries to store the mapping of characters from s to t and vice versa
        charIndexS = {}
        charIndexT = {}

        # Iterate through the characters of both strings simultaneously
        for i in range(len(s)):
            if s[i] not in charIndexS: # If the character from s is not in the dictionary, add it with its index
                charIndexS[s[i]] = i

            if t[i] not in charIndexT: # If the character from t is not in the dictionary, add it with its index
                charIndexT[t[i]] = i

            if charIndexT[t[i]] != charIndexS[s[i]]:
                return False # If the indices of the characters in the two dictionaries do not match, the strings are not isomorphic

        return True # If the cycle completes without returning False, the strings are isomorphic