class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        a, b = 0, len(s) - 1

        while a < b:
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            print("a", s[a])
            print("b", s[b])
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1

        return True