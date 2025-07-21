class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # kuch check krke dena arr mei toh map/set try
        complement_map = {} #value->index
        
        for i,num in enumerate(nums):
            if target - num in complement_map:
                return [complement_map[target-num], i]
            complement_map[num] = i

        return []

        