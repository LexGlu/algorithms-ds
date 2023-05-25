import random
from time import perf_counter

def time_sort_func(sort_func, num_iter=100, lst_size=100):
    start = perf_counter()
    for i in range(num_iter):
        lst = [random.randint(0, lst_size*2) for _ in range(lst_size)]
        sort_func(lst)
    end = perf_counter()
    avg_time = (end - start) / num_iter * 1000
    print(f'{sort_func.__name__} average execution time ({num_iter} iterations): {avg_time:.3f} ms')


def check_sort_func(sort_func, lst_size=10):
    lst = [random.randint(0, lst_size*2) for i in range(lst_size)]
    print(f'Initial array: {lst}')
    result = sort_func(lst)
    # if sort_func returns None, it means that it modifies the original array otherwise it returns a new sorted array 
    if result:
        print(f'Array after sort: {result}')
        print(f'Array is sorted: {result == sorted(lst)}')
    else:
        print(f'Array after sort: {lst}')
        print(f'Array is sorted: {lst == sorted(lst)}')
    