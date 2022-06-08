class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount+1
        change = [-1]*n
        coins.sort(reverse=True)
        
        change[0] = 0
        
        for c in coins:
            if c < n:
                change[c] = 1
            
        for i in range(1,n):
            for j in range(0, i+1):
                if change[j] > -1 and change[i-j] > -1:
                    m = change[j]+change[i-j]
                    if m > 0:
                        if change[i] == -1:
                            change[i] = m
                        else:
                            change[i] = min(change[i],m)


        return change[amount]
