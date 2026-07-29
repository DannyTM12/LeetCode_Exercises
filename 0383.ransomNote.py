class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magaHash = {} # Hash map to store character frequencies in magazine

        # Count the frequency of each character in the magazine
        for char in magazine:
            if char in magaHash:
                magaHash[char] += 1
            else:
                magaHash[char] = 1

        # Check if each character in the ransom note can be constructed from the magazine
        for char in ransomNote:
            if char not in magaHash or magaHash[char] <= 0:
                return False            
            magaHash[char] -= 1

        # If all characters in the ransom note can be constructed from the magazine, return True
        return True