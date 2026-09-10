class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # keep track of best profit, lowest val seen so far
        best_profit = 0
        curr_min = float("inf")

        # go through each, use lowest seen so far and calculate profit
        for i, num in enumerate(prices):
            curr_min = min(curr_min, num)

            curr_profit = (prices[i] - curr_min)

            # save best profit
            if curr_profit > best_profit:
                best_profit = curr_profit
        
        return best_profit
