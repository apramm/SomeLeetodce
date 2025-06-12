class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mp=defaultdict(int) #hashmap with int:key and int:value
        result=0

        for num in nums:
            # if num not in the map already then start counting sequence 
            if(not mp[num]):
                #dp kindof functions
                #count the length of sequence in a dynamic programming manner
                mp[num] = mp[num-1]+mp[num+1]+1 
                #extend the value of length to the boundaries
                mp[num-mp[num-1]] = mp[num]
                mp[num+mp[num+1]] = mp[num]

                result = max(result, mp[num])

        return result