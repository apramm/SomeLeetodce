class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for num in nums: 
            result ^= num 
            # we know XOR of same number is 0
            # and XOR of 0 with any number is that number itself
            # also important tot note XOR is comutative and associative, so order of operations does not matter
        return result
        