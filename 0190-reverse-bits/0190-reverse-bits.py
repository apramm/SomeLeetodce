class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1) 
            # shift result left and add the least significant bit of n
            n >>= 1 # shift n right to process the next bit
        return result
        