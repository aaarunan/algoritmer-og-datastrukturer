import random
import numpy as np
from matplotlib import pyplot as plt
from timeit import default_timer as timer
import copy


def median3sort(nums, low, high):
    m = (low + high) // 2
    if nums[low] > nums[m]:
        swap(nums, low, m)
    if nums[m] > nums[high]:
        swap(nums, m, high)
        if nums[low] > nums[m]:
            swap(nums, m, low)
    return m


def quicksort(nums: int, low: int, high: int):
    if high - low > 2:
        pivot = partition(nums, low, high)
        quicksort(nums, low, pivot - 1)
        quicksort(nums, pivot + 1, high)
    else:
        median3sort(nums, low, high)


def partition(nums, low, high):
    m = median3sort(nums, low, high)
    swap(nums, m, high - 1)
    pivot = nums[high - 1]

    # Why not work with +1
    min_index = low + 1

    for current_index in range(min_index, high - 1):
        if nums[current_index] < pivot:
            swap(nums, min_index, current_index)
            min_index += 1

    swap(nums, min_index, high - 1)

    return min_index


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


def create_random_list(length):
    randomList = []

    for i in range(length):
        n = random.randint(-200, 200)
        randomList.append(n)

    return randomList


def create_random_same_list(length):
    randomList = []

    n = random.randint(-100000, 100000)
    for i in range(length):
        randomList.append(n)

    return randomList


def create_interval(n: int, interval: int):
    powers = []
    sum = interval
    for n in range(n):
        powers.append(sum)
        sum += interval
    return powers


def main():
    xPoints = []
    yPoints = []
    yPointsDualPivot = []
    n = 10
    while n < 40000:
        nums = create_random_list(n)

        start = timer()
        quicksort(nums, 0, n - 1)
        end = timer() - start
        yPoints.append(end)

        start = timer()
        dual_pivot_quicksort(nums, 0, n - 1)
        end = timer() - start
        yPointsDualPivot.append(end)

        xPoints.append(n)
        n += 2000
        print(n)

    plt.plot(np.array(xPoints), np.array(yPoints), label="quicksort median3")
    plt.plot(np.array(xPoints), np.array(yPointsDualPivot), label="quicksort dualpivot")
    plt.legend()
    plt.show()


def test_quicksort_with_random_list():
    n = 100000
    nums1 = create_random_list(n)
    nums2 = copy.deepcopy(nums1)
    nums1.sort()
    quicksort(nums2, 0, n - 1)
    if nums1 != nums2:
        print("sort:     ", nums1)
        print("quicksort:", nums2)
    print(nums1 == nums2)


def test_dual_pivot_quicksort_with_random_list():
    n = 100000
    nums1 = create_random_list(n)
    nums2 = copy.deepcopy(nums1)
    nums1.sort()
    dual_pivot_quicksort(nums2, 0, n - 1)
    if nums1 != nums2:
        print("sort:     ", nums1)
        print("quicksort:", nums2)
    print(nums1 == nums2)


if __name__ == "__main__":
    main()

test_quicksort_with_random_list()
test_dual_pivot_quicksort_with_random_list()
