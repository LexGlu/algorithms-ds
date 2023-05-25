from typing import List


def reverse_bubble_sort(arr: List[int]) -> None:
    # will move the smallest element to the start of the array
    n = len(arr)
    for i in range(-1, -n - 1, -1):
        is_swapped = False
        for j in range(-1, -n - i - 1, -1):
            if arr[j] < arr[j - 1]:
                is_swapped = True
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        if not is_swapped:
            return
        
        
# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(reverse_bubble_sort)
    time_sort_func(reverse_bubble_sort)
