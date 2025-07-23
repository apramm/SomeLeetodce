class Solution:
    def firstUniqChar(self, s: str) -> int:
        #hashmap method
        # string_map = {} #string->freq

        # for c in s:
        #     if c in string_map:
        #         string_map[c] += 1
        #     else:
        #         string_map[c] = 1

        # for i,c in enumerate(s):
        #     if string_map[c] == 1:
        #         return i
            
        # return -1

        #ascii method

        freq = [0]*26

        for c in s:
            freq[ord(c) - ord("a")] += 1
        
        for i,c in enumerate(s):
            if freq[ord(c) - ord("a")] == 1:
                return i
        return -1
