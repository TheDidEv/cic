import time
import copy

def bubble_sort(arr):
    start_time = time.time()
    
    operations = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            operations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    end_time = time.time()
    final_time = end_time - start_time
    return copy.deepcopy(arr), operations, final_time

def insertion_sort(arr):
    start_time = time.time()
    
    operations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                operations += 1
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        
    end_time = time.time()
    final_time = end_time - start_time
    return copy.deepcopy(arr), operations, final_time
