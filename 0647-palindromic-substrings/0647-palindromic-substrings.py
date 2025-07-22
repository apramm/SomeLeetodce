class Solution:
    def countSubstrings(self, s: str) -> int:
        # to find palindromes within string 
        # check for each possible pair O(n2) : BRUTE FORCE

        # palindrome_count = 0
        # n = len(s)

        # for i in range(n):
        #     # print("c:", s[i])
        #     palindrome_count+=1
        #     # print(palindrome_count)
        #     for j in range(i+1,n,1):
        #         # print("i:",i , "j:",j)
        #         # print("substring1:", s[i:j+1])
        #         # print("rev substring:", s[i:j+1][::-1])
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             palindrome_count+=1
        #             # print(palindrome_count)
        # return palindrome_count

        #OPTIMIZED SOLN?
        # left, right method same O(n2)

        palindrome_count = 0

        def count_palindrome(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        for i in range(len(s)):
            palindrome_count += count_palindrome(s, i, i) 
            #odd palindrome with l,r, on same
            palindrome_count += count_palindrome(s, i, i + 1)
            #even palindrome with r being a pair

        return palindrome_count






                
            

    





        