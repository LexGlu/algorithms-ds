import random
from typing import List

lst = [random.randint(0, 100) for i in range(10)]

def selection_sort(arr: List[int]) -> None:
    n = len(arr)
    print(f'Initial array: {arr}')
    for i in range(n - 1):
        is_swapped = False
        min = i
        for j in range (i, n - 1):
            if arr[min] > arr[j + 1]:
                is_swapped = True
                min = j + 1
        if is_swapped:
            arr[i], arr[min] = arr[min], arr[i]
        print(f'iteration {i+1}: {arr}')
        
            
        
# Manual check
if __name__ == '__main__':
    selection_sort(lst)
    print(f'Array after sort: {lst}')
    print(f'Array is sorted: {lst == sorted(lst)}')
    