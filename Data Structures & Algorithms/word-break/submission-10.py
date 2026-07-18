class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_arr = {}



        def dp(s: str, wordDict: List[str]) -> bool:
            if s == '':
                return True
            
            if s in dp_arr:
                return dp_arr[s]

            for word in wordDict:
                if s.startswith(word):
                    if dp(s[len(word):], wordDict):
                        dp_arr[s] = True
                        return True
            dp_arr[s] = False
            return False

        return dp(s, wordDict)

