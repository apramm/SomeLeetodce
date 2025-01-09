class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #optimized technique in O(n) time and space
        #BUCKET SORT ALGORITHM
        # we still need the num:freq hashmap
        # important is we store the list of num occuring with n freq in a n list

        opt = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums: #O(n) 
            opt[num] = 1 + opt.get(num,0) #concise way to do the same num:freq map
        print(opt.items())

        for n,c in opt.items(): #smart thing to make a list with num at freq index
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1): #go in reverse order of max freq
            for n in freq[i]: #each number in max freq
                res.append(n)
                if len(res) == k: #as we need k items
                    return res
        #NOTE: it may seem as n^2 time but obv as there are only n items we have to go thru only n items and not n^2

        # base implementation idea : 
        # store the num in a hashmap as num:freq 
        # check the max freq and return first k num
        # time: O(nlogn) space: O(n)

        res = defaultdict(int)
        lis = []

        for num in nums: #O(n) 
            if num in res:
                res[num] += 1
            else: res[num] = 1
        

        return sorted(res, key=res.get, reverse=True)[:k]
        #this return statement returns k keys with highest value


        #heapify method is better than sorting as that's nlogn and heap is klogn
    