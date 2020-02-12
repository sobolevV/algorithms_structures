import random
import time

def bubble_sort(array):

    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    return array


if __name__ == "__main__":
    times = []
    sizes = []

    size = 10
    iterations = 4
    sizes.append(size)

    for i in range(iterations):
        print("Iteration", i+1, "Size", size)
        # generate array
        unsorted_array = [random.randint(-size, size) for _ in range(size)]

        # sort it
        start_time = time.time()
        sorted_array = bubble_sort(unsorted_array)
        end_time = time.time()

        # save time
        times.append(end_time-start_time)

        # change size
        size = size*10
        sizes.append(size)

    print(f"\nArray size: {sizes[0]}, sorting time: {times[0]}")
    for i in range(1, len(times)):
        print(f"Array size: {sizes[i]}, sorting time: {times[i]}, difference time: {times[i]-times[i-1]}")
