class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            print(nums[mid])
            if nums[mid] >= nums[left]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else: ## ascending
                    return nums[left]
            else:
                right = mid

        return nums[left]

                