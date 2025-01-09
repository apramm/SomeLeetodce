class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #base implementation idea : 
        # store the num in a hashmap as num:freq 
        # check the max freq and return first k num

        res = defaultdict(int)
        lis = []

        for num in nums: #O(n) 
            if num in res:
                res[num] += 1
            else: res[num] = 1
        

        return sorted(res, key=res.get, reverse=True)[:k]
        #this return statement returns k keys with highest value

        