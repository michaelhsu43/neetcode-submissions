class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        count = {}
        maxf = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
            
        
        return result
            

