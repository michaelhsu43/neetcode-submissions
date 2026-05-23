class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 1
        dic = defaultdict(int)
        dic[s[left]] += 1

        most_freq_char = s[left]

        result = 1
        while right < len(s):
            dic[s[right]] += 1
            if dic[s[right]] > dic[most_freq_char]:
                most_freq_char = s[right]

            cur_len = right - left + 1
            needed_k = cur_len - dic[most_freq_char]
            if needed_k <= k:
                right += 1
                result = max(result, cur_len)

            else:
                dic[s[left]] -= 1
                right += 1
                left += 1
        
        return result
            

