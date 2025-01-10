class Solution:

    def encode(self, strs: List[str]) -> str:
        #Encode with number of characters and # in between
        res_str = ""
        for s in strs:
            res_str += str(len(s)) + "#" + s

        print(res_str)
        return res_str


    def decode(self, s: str) -> List[str]:
        #IMPORTANT in decoding is using while to hover over unwanted #
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
