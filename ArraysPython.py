import random
import time
ooo
# bubble sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# merge sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# generate random arrays
def generate_arrays():
    arrays = {}
    for size in [20, 40, 80, 160, 320]:
        arrays[size] = [random.randint(1, 10000) for _ in range(size)]
    return arrays

# measure time taken to sort an array
def measure_time(sort_func, arr):
    start_time = time.time_ns()
    sort_func(arr)
    end_time = time.time_ns()
    return end_time - start_time

# measure runtime behavior of bubble sort and merge sort
def measure_runtime_behavior():
    arrays = generate_arrays()
    bubble_sort_times = []
    merge_sort_times = []
    for size in [20, 40, 80, 160, 320]:
        arr = arrays[size].copy()
        bubble_sort_times.append(measure_time(bubble_sort, arr))
        arr = arrays[size].copy()
        merge_sort_times.append(measure_time(merge_sort, arr))
    return bubble_sort_times, merge_sort_times

# plot the graph for runtime behavior
import matplotlib.pyplot as plt

bubble_sort_times, merge_sort_times = measure_runtime_behavior()

plt.plot([20, 40, 80, 160, 320], bubble_sort_times, label='Bubble Sort')
plt.plot([20, 40, 80, 160, 320], merge_sort_times, label='Merge Sort')
plt.xlabel('Input size')
plt.ylabel('Time taken (nanoseconds)')
plt.title('Runtime behavior of Bubble Sort and Merge Sort')
plt.legend()
plt.show()

