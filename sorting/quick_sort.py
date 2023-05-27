from typing import List
import random
    
    
def quick_sort(arr: List[int]) -> List[int]:
    
    n = len(arr)
    
    if n <= 1:
        return arr
    
    # randomized pivot selection for avoiding worst-case scenarios
    pivot = random.randint(0, n - 1)
    arr[pivot], arr[-1] = arr[-1], arr[pivot]
    pivot = n - 1
    
    left, right = 0, n - 2
    
    while left <= right:
        if arr[left] > arr[pivot]:
            if arr[right] <= arr[pivot]:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
            else:
                right -= 1
        else:
            left += 1
    
    arr[left], arr[n - 1] = arr[n - 1], arr[left]
        
    return quick_sort(arr[:left]) + [arr[left]] + quick_sort(arr[left + 1:])
    
        
# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(quick_sort, 10)
    time_sort_func(quick_sort)
    