import random
from typing import List


lst = [random.randint(0, 100) for i in range(10)]
    
    
def bubble_sort(arr: List[int]) -> None:
    print(f'Initial array: {arr}')
    n = len(arr)
    for i in range(n - 1):
        is_swapped = False # flag to finish execution when arr is sorted to eliminate unnecessary iterations
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                is_swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'iteration {i + 1}: {arr}')
        if not is_swapped:
            return
        
        
# Manual check
if __name__ == '__main__':
    bubble_sort(lst)
    print(f'Array after sort: {lst}')
    print(f'Array is sorted: {lst == sorted(lst)}')
    