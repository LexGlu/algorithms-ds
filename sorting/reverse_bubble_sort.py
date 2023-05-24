import random
from typing import List


lst = [random.randint(0, 100) for i in range(10)]


def reverse_bubble_sort(arr: List[int]) -> None:
    # will move the smallest element to the start of the array
    print(f'Initial array: {arr}')
    n = len(arr)
    for i in range(-1, -n - 1, -1):
        is_swapped = False
        for j in range(-1, -n - i - 1, -1):
            if arr[j] < arr[j - 1]:
                is_swapped = True
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        print(f'iteration {-i}: {arr}')
        if not is_swapped:
            return
        
        
# Manual check
if __name__ == '__main__':
    reverse_bubble_sort(lst)
    print(f'Array after sort: {lst}')
    print(f'Array is sorted: {lst == sorted(lst)}')
