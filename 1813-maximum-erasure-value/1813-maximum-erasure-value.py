class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen: #if duplicate
                #slide the window
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            current_sum += nums[right]
            seen.add(nums[right])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        