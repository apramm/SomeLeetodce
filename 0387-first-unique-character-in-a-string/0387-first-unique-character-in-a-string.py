class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_map = {} #string->freq

        for c in s:
            if c in string_map:
                string_map[c] += 1
            else:
                string_map[c] = 1

        for i,c in enumerate(s):
            if string_map[c] == 1:
                return i
            
        return -1
