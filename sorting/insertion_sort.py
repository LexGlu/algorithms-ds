import random

lst = [random.randint(0, 100) for i in range(10)]

def insertion_sort(arr):
    n = len(arr)
    print(f'Initial array: {arr}')
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        print(f'iteration {i}: {arr}')


# Manual check
insertion_sort(lst)
print(f'Array after sort: {lst}')
print(f'Array is sorted: {lst == sorted(lst)}')