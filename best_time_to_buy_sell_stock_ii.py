from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        buy_price = 999999999999
        sell_day = 0
        total_profit = 0
        max_profit = 0
        total_prices_len = len(prices) - 1

        for day, price in enumerate(prices):
            if price < buy_price and day != total_prices_len:
                buy_price = price

            if (price - buy_price) > max_profit and day > sell_day:
                max_profit = price - buy_price

                if day == total_prices_len or prices[day] >= prices[day + 1]:
                    sell_day = day
                    total_profit += max_profit

                    buy_price = 999999999999
                    max_profit = 0

        return total_profit


if __name__ == '__main__':
    solution = Solution()
    # print(solution.max_profit([7, 1, 5, 3, 6, 4]))  # expected 7
    # print(solution.max_profit([1,2,3,4,5]))  # expected 4
    # print(solution.max_profit([7, 6, 4, 3, 1]))  # expected 4
    print(solution.max_profit([5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]))  # expected 20
