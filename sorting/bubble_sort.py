import random

lst = [random.randint(0, 100) for i in range(10)]
    
def bubble_sort(arr):
    print(f'Initial array: {arr}')
    n = len(arr)
    for i in range(n - 1):
        sorted = True # flag to finish execution when arr is sorted to increase performance
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                sorted = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'iteration {i + 1}: {arr}')
        if sorted:
            return
        
# Manual check
bubble_sort(lst)
print(f'Array after sort: {lst}')
print(f'Array is sorted: {lst == sorted(lst)}')