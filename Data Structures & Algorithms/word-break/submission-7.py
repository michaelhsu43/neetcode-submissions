class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_arr = {}
        return self.dp(s, wordDict, dp_arr)


    def dp(self, s: str, wordDict: List[str], dp_arr) -> bool:
        if s == '':
            return True
        
        if s in dp_arr:
            return dp_arr[s]

        for word in wordDict:
            if s.startswith(word):
                if self.dp(s[len(word):], wordDict, dp_arr):
                    dp_arr[s] = True
                    return True
        dp_arr[s] = False
        return False