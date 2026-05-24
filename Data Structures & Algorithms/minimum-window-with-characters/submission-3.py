class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_map = {}
        
        for ct in t:
            t_map[ct] = 1 + t_map.get(ct, 0)
        
        have, need = 0, len(t_map)

        res, res_len = [-1, -1], float("inf")

        l = 0
        s_map = {}
        for r in range(len(s)):
            char = s[r]
            s_map[char] = 1 + s_map.get(char, 0)

            if char in t_map and s_map[char] == t_map[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                

                s_map[s[l]] -= 1

                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1

                
                l += 1

        l, r = res

        return s[l:r+1] if res_len != float("inf") else ""

        
