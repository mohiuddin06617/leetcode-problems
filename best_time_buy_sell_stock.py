from typing import List


def max_profit(prices: List[int]):
    high = 0
    low = 100000000000
    buy_index = 0
    last_list_index = len(prices) - 1
    result = 0

    for index, price in enumerate(prices):
        if low and low >= price and index != last_list_index:
            low = price
            buy_index = index

        if price >= high and index > buy_index:
            high = price
            diff = high - low

            if diff > result:
                result = diff

    return result


def max_profit_test(prices: List[int]):
    high = 0
    low = 100000000000
    last_list_index = len(prices) - 1
    buy_index = 0
    result = 0

    for index, price in enumerate(prices):
        if low and low >= price and index != last_list_index:
            low = price
            buy_index = index

        if price >= high:
            high = price
            diff = high - low

            if diff > result:
                result = diff


    return result


if __name__ == '__main__':
    # print(max_profit([7, 6, 4, 3, 1]))
    # print(max_profit([7, 1, 5, 3, 6, 4]))
    # print(max_profit([2, 4, 1]))
    # print(max_profit_test([3, 2, 6, 5, 0, 3]))  # expected 4
    # print(max_profit_test([2, 1, 2, 1, 0, 1, 2]))  # expected 2
    print(max_profit_test([3, 3, 5, 0, 0, 3, 1, 4]))  # expected 4
    # print(max_profit_test([3, 2, 6, 5, 0, 3]))  # expected 4
