class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        result = 0
        for num in nums:
            dic[num] = 1
        
        heads = {}
        for num in nums:
            if dic.get(num - 1) == None:
                heads[num] = 1

        result = 1
        for key in heads:
            num = key
            while True:
                num += 1
                if dic.get(num) == None:
                    result = max(result, heads[key])
                    break
                heads[key] += 1
                
        return result
        

        