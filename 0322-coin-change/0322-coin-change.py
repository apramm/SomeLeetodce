class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        amountCoinTable = [inf] * (amount+1) 
        # for each amount, min coin needed table
        amountCoinTable[0] = 0
        
        for coin in coins: # for each coin

            #update table for remaining denom
            for i in range(coin, amount+1, 1): 
                amountCoinTable[i] = min(amountCoinTable[i], amountCoinTable[i-coin]+ 1)
        
        # no way found
        if amountCoinTable[amount] == float('inf'):
            return -1

        return amountCoinTable[amount]