import sys
from timeit import default_timer as timer
import random

# Parameters for testing purposes
price_change_max = 10
price_change_min = -10
# Length of the randomLists made
nums_length = [100_000, 200_000, 400_000, 800_000, 1_600_000, 3_200_000]
price_changes_example = [-1, 3, -9, 2, 2, -1, 2, -1, -5]

# Algorithm finds max profit
def max_profit(price_changes):
    profit = 0
    temp_profit = 0
    sell_price = 0

    for price_change in price_changes:
        temp_profit += price_change

        # If higher price, sell
        if temp_profit < 0:
            profit = max(sell_price, profit)
            sell_price = 0
            temp_profit = 0
        # If lower price, buy
        elif temp_profit > sell_price:
            sell_price = temp_profit

        profit = max(sell_price, profit)

    return profit


# Creates a random list of numbers
def create_random_prices(length):
    randomList = []

    for i in range(length):
        n = random.randint(price_change_min, price_change_max)
        randomList.append(n)

    return randomList


def main():
    prev_time = 0
    
    print("Example case max profit: ", max_profit(price_changes_example))
    print("")

    for n in nums_length:
        randomList = create_random_prices(n)
        start = timer()
        profit = max_profit(randomList)
        time = timer() - start

        # Prints all results and information
        print("Time: ", time, " ", "n: ", n, "profit: ", profit)
        if prev_time != 0:
            print("timeIncrease: x", time / prev_time, "")

        print("")

        prev_time = time


main()
