class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip().split() # Split the string into words

        s.reverse() # Reverse the list of words

        new_s = '' # Initialize an empty string to store the reversed words

        for i in range(len(s)): # Loop through the reversed list of words

            new_s += (' ' + s[i]) # Concatenate each word to the new string with a space

        return new_s.strip() # Return the new string with leading and trailing spaces removed