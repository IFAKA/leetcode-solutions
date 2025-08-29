# stock 
# [7,1,5,3]
#  ^ day 1

# 

# stock price is going down, descending
# [3, 2, 1]

# [1] => 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]  # Track minimum price seen so far
        max_profit = 0  # Track maximum profit possible
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price  # Update minimum price
            else:
                current_profit = price - min_price  # Potential profit
                max_profit = max(max_profit, current_profit)  # Update max profit
        
        return max_profit