from typing import List
    
    
def bubble_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        is_swapped = False # flag to finish execution when arr is sorted to eliminate unnecessary iterations
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                is_swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not is_swapped:
            return
        
        
# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(bubble_sort)
    time_sort_func(bubble_sort)
    