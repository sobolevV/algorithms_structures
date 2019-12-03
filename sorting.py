import random
from time import time


# Sort array with 2 len
def sort_small_arr(arr):
    if len(arr) > 1:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
    return arr


# Merge 2 arrays with sorting
def sort(left, right):
    res_sort = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res_sort.append(left[i])
            i += 1
        else:
            res_sort.append(right[j])
            j += 1
    if i == len(left):
        for k in range(j, len(right)):
            res_sort.append(right[k])
    else:
        for k in range(i, len(left)):
            res_sort.append(left[k])

    return res_sort


def merge_sort(array):
    if len(array) <= 2:
        return sort_small_arr(array)
    res = sort(merge_sort(array[:len(array)//2]), merge_sort(array[len(array)//2:]))
    return res


if __name__ == "__main__":
    # Create random array
    size = 20000
    arr = [random.randint(-1000, 1000) for i in range(size)]
    print(arr)
    # Compare time difference for merge sort and python sort
    start = time()
    res = merge_sort(arr)
    stop = time()
    print(res)
    print(f"Time of merge_sort is {stop-start:.10f}")

    start = time()
    res = arr.sort()
    stop = time()
    print(f"Time of standard sort is {stop - start:.10f}")
