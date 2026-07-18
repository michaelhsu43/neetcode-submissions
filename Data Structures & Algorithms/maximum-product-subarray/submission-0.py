class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        result = nums[0]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                elif j - i == 1:
                    dp[i][j] = nums[i]*nums[j]
                else:
                    dp[i][j] = nums[j]*dp[i][j - 1]

                result = max(result, dp[i][j])

        return result