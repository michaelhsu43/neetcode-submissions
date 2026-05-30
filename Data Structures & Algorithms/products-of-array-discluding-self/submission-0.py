class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0]*len(nums), [0]*len(nums)

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix[i] = product

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            suffix[i] = product

        output = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                output[i] = suffix[i+1]
            elif i == len(nums) - 1:
                output[i] = prefix[i-1]
            else:
                output[i] = suffix[i + 1] * prefix[i - 1]

        return output

