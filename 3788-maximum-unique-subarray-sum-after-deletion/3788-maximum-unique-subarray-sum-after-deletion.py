class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxSum = 0
        set_nums = set(nums)

        for num in set_nums:
            if num > 0:
                maxSum += num #keep adding the unique positive number

        #SPECIAL CASE HANDLING 
        # WHAT IF NO POSITIVE NUMBER?   
        if maxSum == 0:
            maxSum = max(set_nums)
            
        return maxSum


        

            
