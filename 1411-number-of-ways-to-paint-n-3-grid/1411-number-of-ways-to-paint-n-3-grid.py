class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        aba = 6
        abc = 6
        
        for i in range(2, n + 1):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD
            
            aba = new_aba
            abc = new_abc
        
        return (aba + abc) % MOD