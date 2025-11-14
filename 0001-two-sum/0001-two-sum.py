class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # todo : return indices of two numbers in nums so,  == target 
        # 0-based indexing

        # assumption allowed : 
        # each input has exactly one solution
        # cannot use the same element twice

        #more questions?
        # are numbers non-negative?
        

        # idea : use hashmap to store number itself as key and value as it's index
        # put all numbers and their indices in map 
        # subtract and done
         
        map = {} # {num:i, ...}
        
        # loop over nums
        # if complement in map : return map[complement], i
        # edge: what if same number then; we add stuff only if we dont find complement
        # that way if the same number came we've it's index and initial number's index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
        
        return []
