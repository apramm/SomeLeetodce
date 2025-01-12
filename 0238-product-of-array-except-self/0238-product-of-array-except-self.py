class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Must be O(n) and no division operator

        # optimal method
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #we store prefix in result array
            prefix *= nums[i] #calculate prefix in each iteration 
        
        #store in rev for postfix
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i] #same as before just reverse to get postfix

        return res


        # my try : i kind of overdid it and made O(n2)
        #think of storing the values in repeated way 
        #go to an element and iterate to the pre array and store in a pre-array
        # go to post array and store in post array
        # then multiply and store daamn! this is the hint

        ans = []
        dummy_nums = nums
        # me  thinking on hint
        # what is the repeated thing that i need to store value of?
        # we are going thru each value and multiplying the next value with 1 and so on 
        #store in pre and post
        pre = []
        post = []
        current
        for i in range(len(nums)):
            pre_num = 1
            post_num = 1    
            for j in range(0,i):
                if j != i:
                    pre_num *= nums[j]   
            pre.append(pre_num)
            
            for j in range(i+1,len(nums)):
                if j != len(nums):
                    post_num *= nums[j]
                    
            post.append(post_num)

        for i in range(len(nums)):
            ans.append(pre[i]*post[i])

        return ans
        
            
          