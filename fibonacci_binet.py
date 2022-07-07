from decimal import Decimal
from math import sqrt


def solution(n):
    fiblist = [0, 1]
    for i in range(n - 1):
        fiblist.append(fiblist[i] + fiblist[i + 1])
    return fiblist[-1]


def binet_solution(n):
    return Decimal((1 / sqrt(5)) * (pow(((1 + sqrt(5)) / 2), n) - pow(((1 - sqrt(5)) / 2), n)))


def fibonacci(n):
    five_sqrt = 5 ** 0.5

    return int(round((((1 + five_sqrt) / 2) ** n) / five_sqrt))


if __name__ == "__main__":
    print(solution(800))
    print(binet_solution(800))
