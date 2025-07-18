class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # reach the min value in nums_set and then do stuff
            if num-1 not in nums_set:
                current = num
                streak = 1

                while current+1 in nums_set:
                    current+=1
                    streak+=1

                longest = max(longest,streak)

        return longest