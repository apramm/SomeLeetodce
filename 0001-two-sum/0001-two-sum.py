class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BASE CASE len(nums) == 2
        if len(nums) == 2:
            return [0,1] 

        # OPTIMAL IDEATION
        # lets try the set implementation for optimal runtime

        # some issue that arise: 
        # how to not run into the issue of returning the same number in set
        # how to be able to return the index if both same number?

        # to solve both these issues we use hashmap
        # where our runtime of lookup isn't compromised but
        # we create {[num:index],[num:index]} kind of hashmap
        

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
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

