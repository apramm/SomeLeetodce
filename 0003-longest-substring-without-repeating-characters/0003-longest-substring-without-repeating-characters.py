class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        maxLength = 0
        lastSeen = {}

        for right,c in enumerate(s):
            if c in lastSeen and lastSeen[c] >= left:
                # if char is already seen and it's within the current substring route
                left = lastSeen[c] + 1 # move left one ahead of the lastSeen repeating char
            maxLength = max(maxLength, right-left+1)    
            lastSeen[c] = right 

        return maxLength