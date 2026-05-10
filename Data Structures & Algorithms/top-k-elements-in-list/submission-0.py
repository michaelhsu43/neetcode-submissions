class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if not dic.get(num):
                dic[num] = 0
            dic[num] += 1
        frq = defaultdict(list)
        for key, value in dic.items():
            frq[value].append(key)

        result = []
        for i in range(len(nums), -1, -1):
            if not frq.get(i):
                continue
            else:
                for item in frq[i]:
                    result.append(item)
                    k -= 1
                    if k == 0:
                        return result