import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # just do check for normal string with reversed string?
        # REGEX + REVERSE METHOD

        s = s.lower() #upper to lower
        s = re.sub(r'[^a-zA-Z0-9]', '', s) 
        #regex to include only valid alphanumeric values i.e., a-zA-Z0-9
        #regex, replace non accepting with empty string, s
        return s == s[::-1]


        #sliding window
        left = 0
        right = len(s)-1
        
        while left<right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1

        return True




        