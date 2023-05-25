from typing import List
    
    
def merge_sort(arr: List[int]) -> List[int]:
    
    def merge(left, right):
        merged_arr = []
        i = j = 0
        
        # compairing elements from already sorted two halves and appending the smallest one to merged list
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged_arr.append(left[i])
                i += 1
            else:
                merged_arr.append(right[j])
                j += 1
                
        # add remaining elements from left/right half (only one while loop can be triggered)        
        while i < len(left):
            merged_arr.append(left[i])
            i += 1
            
        while j < len(right):
            merged_arr.append(right[j])
            j += 1
        
        return merged_arr
        
        
    # base case 
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # recursively divide array until reaching base case
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
     
    # calling merge func on already sorted two halves
    return merge(left_half, right_half)
    
        
# Manual check
if __name__ == '__main__':
    from utils import time_sort_func, check_sort_func
    check_sort_func(merge_sort, 20)
    time_sort_func(merge_sort)