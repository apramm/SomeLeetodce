class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #base : nums is empty i.e., no unique elements
        if not nums:
            return 0
        
        # as arr is sorted
        # we'd only need to compare next with curr
        # strat 1: iterate once is just required to as no optimization to know where duplicate will occur

        # have unique num var 
        last_unique_index = 0
        for j in range(1, len(nums),1): #iterate over the entire array starting 1

            if nums[j] != nums[last_unique_index]: # we found new unique number
                last_unique_index += 1 #increment last unique number
                nums[last_unique_index] = nums[j] #put the unique number in that index

        return last_unique_index+1
    