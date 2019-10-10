def quicksort(array, compare):
    if len(array) < 2:
        return array

    pivot = array[0]
    i = 0
    
    for j in range(len(array)-1):
        if compare(array[j+1], pivot):
            array[j+1],array[i+1] = array[i+1], array[j+1]
            i += 1
    
    array[0],array[i] = array[i],array[0]

    before = quicksort(array[:i], compare)
    after = quicksort(array[i+1:], compare)
    before.append(array[i])
    
    return before + after