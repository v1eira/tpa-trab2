import math

from heapsort import heapsort

def introsort(array, compare):
    size = len(array)
    max_depth = math.log(size, 2)
    pivot = size-1

    if size < 2:
        return
    elif pivot > max_depth:
        array = heapsort(array, compare)
        return array

    before = introsort(array[:pivot], compare)
    after = introsort(array[pivot+1:], compare)
    before.append(array[p])
    
    return before + after