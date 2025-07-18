class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {} # str:index
        left = 0
        maxLength = 0
        
        for right,c in enumerate(s):
            if c in charMap and charMap[c] >= left:
                left = charMap[c]+1 #move left to ahead of first repeating char
            
            maxLength = max(maxLength, right-left+1) #find distance
            charMap[c] = right #keep going forward for correct distance

        return maxLength