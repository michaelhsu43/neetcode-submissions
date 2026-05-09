class Solution:
    def isValid(self, s: str) -> bool:
        l_r_map = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in l_r_map:
                stack.append(c)
            else:
                if stack and c == l_r_map[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return not stack