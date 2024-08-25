class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        maxp = 0
        for p in prices:
            if min > p:
                min = p
            elif p - min >maxp :
                maxp = p - min
        return maxp


S = Solution()
print(S.maxProfit([1,2,3,5,9,0,9]))