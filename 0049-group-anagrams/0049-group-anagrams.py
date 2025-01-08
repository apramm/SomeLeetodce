class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #TODO: group the anagrams in the list together
        #my initial ideas:
        #find anagrams within the list of strs by iterating and store
        
        # IMPORTANT HINT : 
        # in python list cannot be keys as immutable so store as tuples
        # also defaultdict to avoid append and long key error

        #TRIVIAL length = 1
        length = len(strs)
        if length == 1:
            return [strs]
        
        # SORT
        # i feel that strings can also be sorted as per ascii but that will be too poor time complexity around n^2logn
        #time : O(n^2logn) space : O(1)
        
        sort_map = defaultdict(list)

        for s in strs:

            sort = tuple(sorted(s))
            
            sort_map[sort].append(s)
        
        return(list(sort_map.values()))
            

        #trying soln without sorting using HASHMAP smart key method
        # hard to come up with the key storing method but idea is intuitive
        #TIME : O(n*m) SPACE : O(1) or O(m) 
        
        res_map = defaultdict(list)

        for s in strs: #each str in strs
            key = [0]*26 #specific char pattern for key

            for c in s: #each char in str
                key[ord(c)-ord("a")] += 1 #create key based on occurence of char
            
            res_map[tuple(key)].append(s)
       
        return(list(res_map.values()))

    
