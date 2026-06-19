class Solution:
    def climbStairs(self, n: int) -> int:
        ## n = (n - 1) + (n - 2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        pprev = 1
        prev = 2
        res = 0
        for i in range(3, n+1):
            res = pprev + prev
            pprev = prev
            prev = res

        return res