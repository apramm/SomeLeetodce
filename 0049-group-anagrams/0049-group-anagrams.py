class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #TODO: group the anagrams in the list together
        #my initial ideas:
        #find anagrams within the list of strs by iterating and store
        # IMPORTANT HINT : 
        # in python list cannot be keys as immutable so store as tuples

        #TRIVIAL length = 1
        length = len(strs)
        if length == 1:
            return [strs]
        
        #to find anagrams
        # do i need to see each char or no? hmm 
        # i feel that strings can also be sorted as per ascii but that will be too poor time complexity around n^2logn
        # res = []
        # sorted_map = {}
        # for idx in range(length):
        #     sort = sorted(strs[idx])
        #     if sort in sorted_map:
        #         sorted_map[sort].add(strs[idx])
        #     sorted_map[sort] = strs[idx]
        
        # print(sorted_map)
            

        #trying soln without sorting using HASHMAP smart key method
        res_list = []
        res_map = defaultdict(list)
        for s in strs: #each str in strs
            key = [0]*26 #specific char pattern for key

            for c in s: #each char in str
                key[ord(c)-ord("a")] += 1 #create key based on occurence of char
            
            res_map[tuple(key)].append(s)
       
        return(list(res_map.values()))

    
