class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
                
        # time limit exceeds
        # for i in range (1,n//2 + 1,1):
        #     if n == 2**i:
        #         return True

        if n == 0:
            return False

        #works but loop        
        # while(n%2== 0):
        #     n = n/2
        # if n == 1:
        #     return True

        # return False

        #bit manipulation
        return (n & (n-1)) == 0
        # 2^k = 1000 and 2^k - 1 = 01111 
        # i.e., their bitwise and should be 0 if they 2^k