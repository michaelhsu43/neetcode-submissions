class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0] * n
        prefix_max = 0
        for i in range(n):
            prefix_max = max(prefix_max, height[i])
            prefix[i] = prefix_max
        
        suffix = [0] * n
        suffix_max = 0
        for i in range(n - 1, -1, -1):
            suffix_max = max(suffix_max, height[i])
            suffix[i] = suffix_max

        total = 0
        for i in range(n):
            total += max(min(prefix[i], suffix[i]) - height[i], 0)

        return total