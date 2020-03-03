import random
import asyncio
import time
import copy

# def partition(array):
#     pivot_index = len(array) - 1
#     pivot = array[pivot_index]

#     i = 0
#     j = 0

#     while j < pivot_index:
#         if array[j] < pivot:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#         j += 1

#     # new_array = array[:i+1] + [pivot] + array[i+1:pivot_index]
#     return i+1 # new_array


def quick_sort_req(array):
    if len(array) <= 1:
        return array
    
    pivot_index = len(array)//2
    pivot = array[pivot_index]
    array = array[:pivot_index] + array[pivot_index+1:] 
    
    left, right = [], []
    for i in range(len(array)):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    array = quick_sort_req(left) + [pivot] + quick_sort_req(right)

    return array


if __name__ == '__main__':

    iterations = 4
    size = 10

    sizes = []
    times = []
    times_standard_sort = []

    for i in range(iterations):
        unsorted_arr = [random.randint(-size, size) for i in range(size)]
        unsorted_arr_c = unsorted_arr[:] 
        # timer
        start = time.time()
        sorted = quick_sort_req(unsorted_arr)
        end = time.time()
        # print(sorted)

        # calculate sor times for standard sort
        start_st = time.time()
        unsorted_arr_c.sort()
        end_st = time.time()

        # save times
        times.append(end - start)
        times_standard_sort.append(end_st-start_st)
        # save size and change it
        sizes.append(size)
        size *= 10

    for i in range(iterations):
        print(f"Array size: {sizes[i]}, sort time: {times[i]}, standard sort time: {times_standard_sort[i]}")
