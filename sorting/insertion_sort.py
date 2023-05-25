from typing import List


def insertion_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(insertion_sort)
    time_sort_func(insertion_sort)
