import random

lst = [random.randint(0, 100) for i in range(10)]
    
def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        flag = False # flag is used to check if the array is already sorted -> best-case time complexity is O(n) instead of O(n^2)
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'iteration {i + 1}: {arr}')
        if not flag:
            return arr
    return arr
        
print(f'Sorted arr: {bubble_sort(lst)}')

print(f'Array is sorted: {lst == sorted(lst)}')