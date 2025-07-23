import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # just do check for normal string with reversed string?
        s = s.lower() #upper to lower
        s = re.sub(r'[^a-zA-Z0-9]', '', s) #regex to include only valid alphanumeric values i.e., a-zA-Z0-9
        return s == s[::-1]


        