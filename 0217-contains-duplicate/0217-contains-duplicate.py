class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        # O(n) time and O(n) space
        # *unordered* SET with more space usage but better time

        #IDEA : no duplicates in set
        for num in nums:
            num_set.add(num)
        if len(nums) == len(num_set):
            return False
        return True
          
        #same idea but faster as no len checks  
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

        # SORTING APPROACH
        # O(nlogn) time O(1) space Balanced approach
        
        nums.sort()
        for idx in range(1,len(nums)):
            if nums[idx] == nums[idx-1]:
                return True
        return False

        #BASE APPROACH
        # O(n^2) time O(1) space 
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
                   
        return False            
