class Solution:
    def twoSum(self, nums: List[int], start, target) -> List[List[int]]:
        left, right = start, len(nums) - 1
        return_nums = []
        while left < right:
            if nums[left] + nums[right] == target:
                return_nums.append([-target, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
        # print(return_nums)
        return return_nums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            triplets.extend(self.twoSum(nums, i + 1, -nums[i]))
        
        return triplets

