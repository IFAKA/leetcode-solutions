class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # handle edge cases
        # define variable max profit and minimum value
        # iterate over prices
        # if price is lower than current min value
        #   update min value with current value
        # else skip it
        # if current value minus min value is greater than max profit
        #   max profit is current value - minimum value
        # return max profit

        # tc: o(n)
        # sc: o(1)
        
        # mv,mp = 7, 0
        # loop prices[1:]
        # 1 < 7
        # mv = 1
        # 5 < 1
        # 5 - 1 > 0
        # mp = 5 - 1
        # 3 < 1
        # 3 - 1 > 4
        # 6 < 1
        # 6 - 1 > 4
        # mp = 5
        # 4 < 1
        # 4 - 1 > 5
        # return mp == 5
        

        max_profit = 0
        min_val = prices[0]

        for price in prices[1:]:
            if price < min_val:
                min_val = price
            elif price - min_val > max_profit:
                max_profit = price - min_val

        return max_profit