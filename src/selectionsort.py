def selectionsort(array, compare):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if (compare(array[j], array[minimum]) == -1):
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    
    return array