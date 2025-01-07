class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # BASIC Method using SORT
        # time : O(nlogn) space: O(1)

        return sorted(s) == sorted(t)

        #MY METHOD: COMPARE DICTIONARIES(HASHTABLES)
        # time : O(n) space : O(1)**
        # MY SPACE COMPLEXITY ANALYSIS WAS WRONG IT'S O(1)
        # as we atmost have 26 chars to store

        #sanity check [important to think of]
        #length should be same if not then obv not anagram
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        # set will not work need to use dictionary i.e., some sort of counter
        #make the char key and iterations as value

        dict_s, dict_t = {}, {}
        
        for char in s:
            if char in dict_s.keys():
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        
        for char in t:
            if char in dict_t.keys():
                dict_t[char] += 1
            else:
                dict_t[char] = 1
        
        return dict_s == dict_t


        #OPTIMAL using HASHTABLE
        # time: O(n) space: O(1)
        # this is better as shows understanding of ASCII and integration with dict
        count = [0]*26        
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1

        for val in count:
            if val!=0:
                return False
        return True