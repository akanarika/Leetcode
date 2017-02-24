class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        opt = [0] * len(prices)
        res = 0
        for i in range(1, len(prices)):
            max_i = opt[i-1]
            if prices[i] > prices[i-1]:
                for j in range(0, i):
                    max_i = max(prices[i] - prices[j] + opt[j-1], max_i)
            opt[i] = max_i
            res = max(res, max_i)
        
        return res