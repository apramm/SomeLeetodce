class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #set doesnt contain duplicate
        num_set = set(nums)
        if len(num_set) == len(nums):
            return False
        
        return True

        # slightly faster than len checks 
        #for num in nums:
        #     if num in num_set:
        #         return True
        #     else:
        #         num_set.add(num)
        # return False