class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        solution = []
        

        def backtracking(chosen, target, index):
            if target == 0:
                solution.append(chosen.copy())
                return

            for i, num in enumerate(nums):
                if i < index:
                    continue
                if num <= target:
                    chosen.append(num)
                    backtracking(chosen, target - num, i)
                    chosen.pop()

        backtracking([], target, 0)

        return solution