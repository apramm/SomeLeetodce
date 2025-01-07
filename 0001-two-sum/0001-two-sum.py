class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #basic soln idea
        #do double for loop to add and check if they are equal to target & return

        #time : O(n^2) space : O(1)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

