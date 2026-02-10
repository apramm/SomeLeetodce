import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s) 
        n = len(s)

        #simple rev string check:
        # return s==s[::-1]

        #sliding window soln
        left = 0
        right = n-1
        while right>left:
            if s[right] != s[left]:
                return False
            right -=1
            left +=1
        return True
        

        
        