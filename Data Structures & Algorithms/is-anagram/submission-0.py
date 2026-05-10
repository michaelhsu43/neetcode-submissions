class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            if not dic.get(c):
                dic[c] = 0
            dic[c] += 1
        
        for c in t:
            if not dic.get(c):
                return False
            dic[c] -= 1

            if dic[c] == 0:
                dic.pop(c, None)
            
        return not dic
