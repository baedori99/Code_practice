class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max_value = 0
        # sum_value = 0

        if len(prices) == 1:
            return 0

        # for i in range(len(prices)):
        #     if prices[min_index] == prices[i] or min_index > i:
        #         continue
        #     sum_value = prices[i] - prices[min_index]
        #     max_value = max(max_value, sum_value)
        #     print(sum_value, max_value)
        
        # return max_value
        
        # max_value = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if prices[i] < prices[j]:
        #             profit = prices[j] - prices[i]
        #             max_value = max(max_value, profit)
        
        # return max_value        
        
        l = 0
        max_value = 0
        profit = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            max_value = max(max_value, profit)

            if profit < 0:
                l += 1
            if prices[r] < prices[l]:
                l = r
                r = l + 1
        return max_value