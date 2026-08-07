class Solution:
    def hammingWeight(self, n: int) -> int:

        result = 0 # Count the number of 1 bits in the binary representation of n

        for i in range(32): # Iterate through each bit position (0 to 31) for a 32-bit integer
            if (n >> i) & 1:# Check if the i-th bit is set (1) by right-shifting n and performing a bitwise AND with 1
                # How this works: (n >> i) shifts the bits of n to the right by i positions, 
                # effectively moving the i-th bit to the least significant position. The bitwise 
                # AND operation with 1 checks if that least significant bit is 1 (set) or 0 (not set). 
                # If it is 1, it means the i-th bit in n is set, and we increment the result counter.
                result += 1

        return result