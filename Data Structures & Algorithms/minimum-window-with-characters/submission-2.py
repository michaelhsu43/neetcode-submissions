class Solution:

    def check_satisfied(self, s_map:dict, t_map:dict) -> bool:
        for key, value in t_map.items():
            if s_map.get(key,0) < t_map[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_map = {}

        for ct in t:
            t_map[ct] = 1 + t_map.get(ct, 0)

        s_map = {}
        l = 0
        m = 0
        res = ""
        satisfied = False
        for r in range(len(s)):
            if s[r] in t_map:
                s_map[s[r]] = 1 + s_map.get(s[r], 0)
            
            if self.check_satisfied(s_map, t_map) and not satisfied:
                satisfied = True
                res = s[l:r+1]

            if satisfied:
                while (s_map.get(s[l], 0) > t_map.get(s[l], 0)) or (s[l] not in t_map):
                    print(s[l])
                    
                    if s_map.get(s[l], 0) > t_map.get(s[l], 0):
                        s_map[s[l]] -= 1
                    l += 1
                    if (r - l + 1) < len(res):
                        res = s[l:r+1]
                    print(res)

        return res