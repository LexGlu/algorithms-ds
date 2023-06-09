from typing import List
    
    
def shaker_sort(arr: List[int]) -> None:
    # aka cocktail sort
    n = len(arr)
    for i in range(n - 1):
        is_swapped = False # flag to finish execution when arr is sorted to eliminate unnecessary iterations
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                is_swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        for k in range(-1 -i, -n + i, -1):
            if arr[k] < arr[k - 1]:
                arr[k], arr[k - 1] = arr[k - 1], arr[k]
            # the 'is_swapped' flag within the second inner loop is redundant
            # it won't be triggered if the first inner loop does not trigger a swap

        if not is_swapped:
            return
        

# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(shaker_sort)
    time_sort_func(shaker_sort)
        