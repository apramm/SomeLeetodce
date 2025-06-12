class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        result = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1]+mp[num+1]+1
                #update ends
                mp[num-mp[num-1]] = mp[num]
                mp[num+mp[num+1]] = mp[num]

                result = max(result,mp[num])
        return result