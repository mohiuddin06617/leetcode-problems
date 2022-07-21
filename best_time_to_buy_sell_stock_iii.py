"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""

from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        buy_price = 999999999999
        sell_day = 0
        total_profit = 0
        max_profit = 0
        total_prices_len = len(prices) - 1
        total_profit_list = list()

        for day, price in enumerate(prices):
            if price < buy_price and day != total_prices_len:
                buy_price = price

            if (price - buy_price) > max_profit and day > sell_day:
                max_profit = price - buy_price

                if day == total_prices_len or prices[day] >= prices[day + 1]:
                    sell_day = day
                    total_profit += max_profit
                    total_profit_list.append(max_profit)

                    buy_price = 999999999999
                    max_profit = 0

        return sum(sorted(total_profit_list)[-2:])


if __name__ == '__main__':
    solution = Solution()
    # print(solution.max_profit([3, 3, 5, 0, 0, 3, 1, 4]))  # expected 6
    # print(solution.max_profit([7, 6, 4, 3, 1]))  # expected 0
    # print(solution.max_profit([1, 2, 3, 4, 5]))  # expected 4
    print(solution.max_profit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))  # expected 13
