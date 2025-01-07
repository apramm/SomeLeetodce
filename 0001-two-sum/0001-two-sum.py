class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #trival len(nums) == 2
        if len(nums) == 2:
            return [0,1] 

        #better soln ( OPTIMAL ) HASH MAP
        # time : O(n) space: O(n)
        # important thing to understand is to create hashmap on the go 

        nums_hash = {}
        diff = 0

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in nums_hash:
                return [idx, nums_hash[diff]]
            else:
                nums_hash[nums[idx]] = idx
        return
    

        #basic soln idea (NOT OPTIMAL)
        #Double for loop to sum and check if they are equal to target & return

        #time : O(n^2) space : O(1)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

