class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sanity check
        #length should be same if not then obv not anagram
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        # set will not work need to use dictionary i.e., some sort of counter
        #make the char key and iterations as value
        dict_s = {}
        dict_t = {}
        
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
        
        print(dict_s)
        print(dict_t)

        if dict_s == dict_t:
            return True
        return False


        