class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if nums == []: return 0
        # just cover special cases seperately

        # else use greedy
        
        set_nums = set(nums)
        result = 0

        for n in set_nums:
            if n > 0:
                result += n

        if result  == 0: #sepcial case of all negatives
            result = max(set_nums) # return highest unqiue val
        
        return result



        