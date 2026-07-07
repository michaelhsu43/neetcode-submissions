class Solution:

    def dp(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_arr = [0]*len(nums)
        dp_arr[0] = nums[0]
        dp_arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp_arr[i] = max(dp_arr[i - 1], dp_arr[i - 2] + nums[i])
        return dp_arr[len(nums) - 1]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ## Left 0 ~ n - 2, Right 1 ~ n - 1
        n = len(nums)
        left = nums[0:n-1]
        right = nums[1:n]
        
        return max(self.dp(left), self.dp(right))
