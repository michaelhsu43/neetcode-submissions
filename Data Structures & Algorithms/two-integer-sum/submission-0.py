class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for index, num in enumerate(nums):
            if num in compliment:
                return [compliment[num], index]
            compliment[target - num] = index