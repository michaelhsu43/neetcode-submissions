class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## suffix array
        max_num = 0
        suffix_array = [0]*len(prices)
        for i in range(len(prices) - 1, -1, -1):
            max_num = max(max_num, prices[i])
            suffix_array[i] = max_num
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, suffix_array[i]-prices[i])

        return max_profit