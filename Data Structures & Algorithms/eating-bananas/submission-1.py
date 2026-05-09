class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_hours(k: int) -> int:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours
        ## range is from 1 to max(piles)

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if eating_hours(mid) > h:
                left = mid + 1
            else:
                right = mid
        
        return left