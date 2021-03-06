from random import randint


def qsort(arr: list) -> list:
    if len(arr) < 2: return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return arr
    
    pivot_idx = randint(0, len(arr)-1)
    pivot = arr[pivot_idx]
    left_sub_arr = []
    right_sub_arr = []
    
    for el in arr[:pivot_idx]:
        if el <= pivot: left_sub_arr.append(el)
        else: right_sub_arr.append(el)
        
    for el in arr[pivot_idx+1:]:
        if el <= pivot: left_sub_arr.append(el)
        else: right_sub_arr.append(el)
        
    return qsort(left_sub_arr) + [pivot] + qsort(right_sub_arr)


print(qsort([1, 2, 3, 4, 6, 7, 8]))
print(qsort([1, 6, 3, 4, 5]))
print(qsort([]))
print(qsort([1]))
print(qsort([5, 7, 1, 0]))
print(qsort([1, 2, 3, 5, 2]))
