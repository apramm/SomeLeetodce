class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # if neg then def not palindrome
            return False
        if x == 0:
            return True
        
        #solve without converting to string
        #reverse the number and compare to original
        original = x
        reversed_num = 0
        while x > 0:
            digit = x % 10 # get the last digit
            reversed_num = reversed_num * 10 + digit # add the digit to the rightmost position
            x //= 10 # remove last digit using floor division

        return original == reversed_num
    
        #solution by converting to string
        # str_x = str(x)
        # return str_x == str_x[::-1] # check if string is equal to its reverse
    