class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce : double iteration to find the two numbers adding to target
        #  O(n^2) not optimal

        # Optimal : O(n) by creating a hashtable with number : target-num and for each
        # number see if target-num in some keys we found both nums
        hash = {} # num : i
        for i,num in enumerate(nums):
            complement = target-num
            if (complement) in hash:
                return [hash[complement], i]
            hash[num] = i

        return []