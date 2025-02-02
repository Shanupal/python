# class solution
# def profir(self, price: list[int])
# max = 0
#      if prices ([l] <[r]):
#          profir = prices ([r]-[l]):
#              max = more(profir,prices)
#     else
#     l=r
#     r +=1
#     return max       
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0 
        l, r = 0, 1    

        while r < len(prices):
            if prices[l] < prices[r]:  
                profit = prices[r] - prices[l]  
                max_profit = max(max_profit, profit)  
            else:
                l = r  
            r += 1  

        return max_profit

    
