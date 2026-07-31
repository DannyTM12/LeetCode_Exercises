class Solution:
    def wordPattern(self, s: str, pattern: str) -> bool:
        # Split the string into words
        s = s.split()

        # Check if the lengths of the string and pattern are equal
        if len(s) != len(pattern):
            return False

        # Create hash maps to store the indices of each word and pattern character
        sHash = {}
        patternHash = {}


        for i in range(len(s)): # Iterate through each character in the pattern and each word in the string
            if s[i] not in sHash: # If the word is not in the hash map, add it with its index
                sHash[s[i]] = i

            if pattern[i] not in patternHash: # If the character is not in the hash map, add it with its index
                patternHash[pattern[i]] = i

            if patternHash[pattern[i]] != sHash[s[i]]: # If the indices of the character and word do not match, return False
                return False

        return True # If all characters and words match their respective indices, return True