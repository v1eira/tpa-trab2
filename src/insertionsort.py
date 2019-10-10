def insertionsort(array, compare):
    for index in range(1, len(array)):
        bol = True
        while index > 0 and bol:
            if(compare(array[index], array[index-1]) == -1):
                array[index], array[index-1] = array[index-1], array[index]
                index -=1
            else:
                bol = False
    
    return array