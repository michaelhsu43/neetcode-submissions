class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, 1
        dic = defaultdict(int)

        dic[s[left]] += 1
        result = 1
        cur = 1
        while right < len(s):

            if dic[s[right]] < 1:
                dic[s[right]] += 1
                cur += 1
                right += 1
            else:
                dic[s[left]] -= 1
                cur -= 1
                left += 1

            result = max(result, cur)

        return result
