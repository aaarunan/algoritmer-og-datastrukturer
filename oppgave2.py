import math
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import numpy as np


bases = [2]


def pow(n: int, base: float):
    if n < 1:
        return 1
    return base * pow(n - 1, base)


def powEfficient(n: int, base: float):
    if n < 1:
        return 1
    if n % 2 == 0:
        return powEfficient(n / 2, base * base)

    return base * powEfficient((n - 1) / 2, base * base)


# create list of powers with a certain interval for n times
def create_powers(n: int, interval: int):
    powers = []
    sum = interval
    for n in range(n):
        powers.append(sum)
        sum += interval
    return powers


def main():

    # used for testing purposes. Caues unstable results and may cause segmentation issues with memory
    # sys.setrecursionlimit(5000)
    yPointsPow = []
    yPointsPowEff = []
    yPointsPowSys = []
    powers = create_powers(100, 5)

    # test if works
    base = 2
    power = 6
    print("Base ", base, "Pow:", power)
    print("Pow:", pow(6, 2))
    print("PowEfficient:", powEfficient(6, 2))
    print("SystemPow:", math.pow(2, 6), "\n")

    # test for time complexity
    for base in bases:
        print("Base:", base, "\n")
        for power in powers:

            start = timer()
            pow(power, base)
            end = timer() - start
            yPointsPow.append(end)

            start = timer()
            powEfficient(power, base)
            end = timer() - start
            yPointsPowEff.append(end)

            start = timer()
            math.pow(base, power)
            end = timer() - start
            yPointsPowSys.append(end)


    # Fjern denne hvis powEfficient er vanskelig å se
    plt.plot(np.array(powers), np.array(yPointsPow), label="Normal pow")
    plt.plot(np.array(powers), np.array(yPointsPowEff), label="Efficient pow")
    plt.plot(np.array(powers), np.array(yPointsPowSys), label="System pow")
    plt.ylabel("Time")
    plt.xlabel("Power")
    plt.legend()

    print("Plotting finished.")
    plt.show()


main()
