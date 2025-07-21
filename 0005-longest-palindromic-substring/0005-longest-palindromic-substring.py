class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s:str, left:int, right:int):
            while left>= 0 and right < len(s) and s[left] == s[right]:
                #keep checking for palindromes
                left -=1
                right+=1
            return right-left-1 #len of palindrome

        # need to check for palindromes within a string
        # how to check for sub-palindromes?
        
        # TIP : when set and map cant do the check/lookup correctly
        # think in twopointers as they allow for smart check
       
       
        n = len(s)
        start = 0
        end = 0
        
        for i in range(n):
            #when string is odd we expand diff way i.e., from single center
            
            odd_palindrome =  expand_around_center(s,i,i) # palindrome is odd
            even_palindrome = expand_around_center(s,i,i+1) #palindrom is even

            max_len = max(odd_palindrome, even_palindrome)

            if max_len > end-start: 
                #if this palindrome is longer than curr longest palindrome
                start = i - (max_len - 1) // 2 #first half except center
                end = i + max_len // 2 #second half except center
                # easy to viz how start and endpoint come 

        return s[start:end+1]








    


