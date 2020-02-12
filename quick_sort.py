import random
import asyncio
import time


def partition(array):
    pivot_index = len(array) - 1
    pivot = array[pivot_index]

    i = -1
    j = 0

    while j < pivot_index:
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1

    new_array = array[:i+1] + [pivot] + array[i+1:pivot_index]
    return new_array, i+1


def quick_sort_req(array):
    if len(array) <= 1:
        return array
    if len(array) == 2:
        if array[0] >= array[1]:
            array[1], array[0] = array[0], array[1]
        return array

    array, pivot_index = partition(array)

    # sort and back
    left_sorted = quick_sort_req(array[:pivot_index-1])
    array[:pivot_index - 1] = left_sorted

    right_sorted = quick_sort_req(array[pivot_index + 1:])
    array[pivot_index+1:] = right_sorted

    return array


if __name__ == '__main__':

    iterations = 5
    size = 10

    sizes = []
    times = []
    times_standard_sort = []

    for i in range(iterations):
        unsorted_arr = [random.randint(-size, size) for i in range(size)]

        # timer
        start = time.time()
        sorted = quick_sort_req(unsorted_arr)
        end = time.time()
        # print(sorted)

        # calculate sor times for standard sort
        start_st = time.time()
        unsorted_arr.sort()
        end_st = time.time()

        # save times
        times.append(end - start)
        times_standard_sort.append(end_st-start_st)
        # save size and change it
        sizes.append(size)
        size *= 10

    for i in range(iterations):
        print(f"Array size: {sizes[i]}, sort time: {times[i]}, standard sort time: {times_standard_sort[i]}")
