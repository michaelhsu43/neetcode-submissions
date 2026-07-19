class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: 
            return False
        target = sum(nums) / 2
        mem = {}
        def dp(index, remaining):
            if remaining == 0:
                return True
            if index == len(nums) or remaining < 0:
                return False
            
            key = (index, remaining)
            if key in mem:
                return mem[key]
            skip = dp(index + 1, remaining)
            take = dp(index + 1, remaining - nums[index])
            
            mem[key] = skip or take
            return mem[key]


        return dp(0, target)