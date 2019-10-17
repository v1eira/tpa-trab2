def merge(array, start, end, compare):
    middle = (start + end)//2
    left_start = start
    left_end = middle
    right_start = middle + 1
    right_end = end
    new_array = []
    while left_start <= left_end or right_start <= right_end:
        if left_start > left_end:
            new_array.append(array[right_start])
            right_start += 1
        elif right_start > right_end:
            new_array.append(array[left_start])
            left_start += 1
        elif (compare(array[right_start], array[left_start]) == 1):
            new_array.append(array[left_start])
            left_start += 1
        elif (compare(array[left_start], array[right_start]) == 1):
            new_array.append(array[right_start])
            right_start += 1
    
    for k in range(len(new_array)):
        array[start + k] = new_array[k]
    
    return array


def mergesort(array, compare, start=0, end=-1):
    if end == -1:
        end = len(array)-1
    
    if start >= end:
        return
    
    middle = (start + end)//2

    mergesort(array, compare, start, middle)
    mergesort(array, compare, middle + 1, end)
    
    return merge(array, start, end, compare)