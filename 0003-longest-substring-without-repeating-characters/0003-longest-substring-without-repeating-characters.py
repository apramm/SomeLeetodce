class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLength = 0
        n = len(s)

        for right in range(n):
            while s[right] in charSet: #if right already in the set
                charSet.remove(s[left]) 
                # keep removing left until right not in set
                left+=1

            charSet.add(s[right])
            maxLength = max(maxLength, right-left+1)

        return maxLength