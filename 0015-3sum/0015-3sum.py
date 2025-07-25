class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # from an arr
        # return triplet s.t. sum == 0

        result = []
        nums.sort() #to easily find the numbers

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue #to skip duplicate valued duplicate

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0: # if total too much then check smaller val
                    k -= 1
                elif total < 0: #if total too less check bigger val
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    #move ahead from both sides to check for new triplets
                    j += 1
                    k -= 1
                    # check for duplication
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result
        