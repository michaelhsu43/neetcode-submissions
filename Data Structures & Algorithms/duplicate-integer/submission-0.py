class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num):
                return True
            d[num] = 1

        return False