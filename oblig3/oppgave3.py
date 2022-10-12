from random import random
import math

# import numpy as np
# from matplotlib import pyplot as plt
# from timeit import default_timer as timer
# from tqdm import tqdm

# For å kjøre tester: pytest Oppgave3.py


def median3sort(nums, low, high):
    m = (low + high) // 2
    if nums[low] > nums[m]:
        swap(nums, low, m)
    if nums[m] > nums[high]:
        swap(nums, m, high)
        if nums[low] > nums[m]:
            swap(nums, m, low)
    return m


def quicksort(nums, low, high):
    if high - low > 2:
        pivot = partition(nums, low, high)
        quicksort(nums, low, pivot - 1)
        quicksort(nums, pivot + 1, high)
    else:
        median3sort(nums, low, high)


def quicksort_dual_pointers(nums, low, high):
    if high - low > 2:
        pivot = partition_dual_pointers(nums, low, high)
        quicksort(nums, low, pivot - 1)
        quicksort(nums, pivot + 1, high)
    else:
        median3sort(nums, low, high)


def partition(nums, low, high):
    m = median3sort(nums, low, high)
    swap(nums, m, high - 1)
    pivot = nums[high - 1]

    min_index = low + 1
    # Bad for lists with same elements, uneven recursion!
    for current_index in range(min_index, high - 1):
        if nums[current_index] < pivot:
            swap(nums, min_index, current_index)
            min_index += 1

    swap(nums, min_index, high - 1)

    return min_index


def partition_dual_pointers(nums: list, low: int, high: int):
    pivot_index = median3sort(nums, low, high)
    middle = nums[pivot_index]

    swap(nums, pivot_index, high - 1)
    pivot_index = high - 1

    # Assign pointers
    left = low + 1
    right = high - 2

    while right > left:
        while nums[right] > middle:
            right -= 1
        while nums[left] < middle:
            left += 1

        if right <= left:
            break

        swap(nums, left, right)
        right -= 1
        left += 1

    swap(nums, pivot_index, left)
    return left


def dual_pivot_quicksort(nums, low, high):
    if low < high:

        # lp means left pivot and rp
        # means right pivot
        lp, rp = dual_pivot_partition(nums, low, high)

        dual_pivot_quicksort(nums, low, lp - 1)
        dual_pivot_quicksort(nums, lp + 1, rp - 1)
        dual_pivot_quicksort(nums, rp + 1, high)


def dual_pivot_partition(nums, low, high):

    # Pivot points are  low and high
    # Incase list is already sorted, we swap left and right to different indexes
    low_temp = low + (high - low) // 3
    high_temp = high - (high - low) // 3

    swap(nums, low, low_temp)
    swap(nums, high_temp, high)

    # Check if left pivot is larger than right
    # Swap if this is the case

    if nums[low] > nums[high]:
        swap(nums, low, high)

    start = current = low + 1
    end = high - 1
    p_left = nums[low]
    p_right = nums[high]

    while current <= end:
        # Swap if the current number is less than left pivot move move to the right of pivot
        if nums[current] < p_left:
            swap(nums, current, start)
            start += 1
        # If the number is bigger than right pivot loop
        elif nums[current] >= p_right:
            # Do the same only backwards on the right pivot
            while nums[end] > p_right and current < end:
                end -= 1
            swap(nums, current, end)
            end -= 1
            # if the number is less than left pivot move to left of left pivot
            if nums[current] < p_left:
                swap(nums, current, start)
                start += 1

        current += 1

    start -= 1
    end += 1

    # Move the pivots to the correct position
    swap(nums, low, start)
    swap(nums, high, end)

    # Return indexes of pivots
    return start, end


def swap(nums, i1, i2):
    nums[i1], nums[i2] = nums[i2], nums[i1]


algorithms = [quicksort, dual_pivot_quicksort, quicksort_dual_pointers]


def main():
    start = 10
    stop = 20000
    increment = 40

    xPoints = [i for i in range(start, stop, increment)]
    print("Running code to start CPU turbo boosting:")
    for _ in tqdm(range(300)):
        test = [random() for _ in range(10000)]
        quicksort(test, 0, len(test) - 1)

    for alg in algorithms:
        yPoints = []
        print("Plotting:", alg.__name__)
        for n in tqdm(range(start, stop, increment)):
            nums = [n for n in range(n)]
            t0 = timer()
            alg(nums, 0, n - 1)
            yPoints.append(timer() - t0)

        plt.plot(np.array(xPoints), np.array(yPoints), label=alg.__name__)
    plt.legend()
    print("Done.")
    plt.show()


# if __name__ == "__main__":
#    main()


def _test_algorithms(nums, algorithms):
    nums_original = nums[:]
    for alg in algorithms:
        alg(nums, 0, len(nums) - 1)
        assert _is_ascending(nums)
        assert math.isclose(sum(nums), sum(nums_original))


def test_on_same_numbers():
    # Few numbers because of recursion depth
    _test_algorithms([0 for _ in range(1000)], algorithms)


def test_on_pre_sorted_numbers():
    _test_algorithms([i for i in range(50000)], algorithms)


def test_on_pre_sorted_inverted_numbers():
    _test_algorithms([-i for i in range(50000)], algorithms)


def test_on_random_numbers():
    _test_algorithms([random() for _ in range(100000)], algorithms)


def test_on_alternating_numbers():
    nums = []
    inc = 10
    for n in range(0, 1000):
        nums.append(inc)
        inc = -inc

    _test_algorithms(nums, algorithms)


def _is_ascending(nums):
    prev = nums[0]

    for num in nums:
        if num < prev:
            return False
        prev = num
    return True


tests = [
    test_on_alternating_numbers,
    test_on_pre_sorted_inverted_numbers,
    test_on_pre_sorted_numbers,
    test_on_same_numbers,
    test_on_alternating_numbers,
]


def test(tests):
    for func in tests:
        try:
            func()
            print(func.__name__, "passed.")
        except AssertionError:
            print (func.__name__, "failed!")


test(tests)
