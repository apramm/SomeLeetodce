class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #iterate through str1 and 
        # check if the substring of str1 with the same length as str2 is equal to str2
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1
        