from typing import List



def selection_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        is_swapped = False
        min = i
        for j in range (i, n - 1):
            if arr[min] > arr[j + 1]:
                is_swapped = True
                min = j + 1
        if is_swapped:
            arr[i], arr[min] = arr[min], arr[i]
            
        
# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(selection_sort)
    time_sort_func(selection_sort)
    