class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the two strings are equal
        if len(s) != len(t):
            return False

        # Create two hash maps to store the frequency of characters in both strings
        sHash = {}
        tHash = {}

        # Iterate through the characters of both strings and populate the hash maps
        for i in range(len(s)):
            # Check if the character is already in the hash map, if not, initialize it with 1
            if s[i] not in sHash:
                sHash[s[i]] = 1

            if t[i] not in tHash:
                tHash[t[i]] = 1

            # If the character is already in the hash map, increment its count
            if s[i] in sHash:
                sHash[s[i]] += 1

            if t[i] in tHash:
                tHash[t[i]] += 1
                
        # Compare the two hash maps to check if they are equal
        return sHash == tHash
        