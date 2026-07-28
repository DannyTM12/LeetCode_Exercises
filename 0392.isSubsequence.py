class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, every chan that t has is subsequence
        if s == '':
            return True

        # If len s y greater tha len t s cannot be subsequence of t 
        if len(s) > len(t):
            return False

        # If s and t are exactly the same s is subsequence
        if s == t:
            return True

        # Initialize i an j to appoint the index 0 of the two strings
        i, j = 0, 0

        # This while function iterates t string and if finds a coincidence in the subsequence moves the pointer of the s string
        # it breaks when we finish one of the strings
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1

        #return the coincidence if j is equal len s
        return j == len(s)