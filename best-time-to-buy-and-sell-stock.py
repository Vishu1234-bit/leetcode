class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyIndex=-1
        sellIndex=-1
        price = -1
        for i in range(0,len(prices)):
            if(buyIndex == -1):
                buyIndex = i
                price = prices[i]
            elif(prices[i]<price):
                buyIndex = i
                price = prices[i]
                maxProfit = max(maxProfit,prices[i]-price)
            else:
                maxProfit = max(maxProfit,prices[i]-price)
        return maxProfit
