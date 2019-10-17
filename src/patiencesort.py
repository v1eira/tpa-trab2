def merge(firstArray, secondArray, compare):
    left_start = 0
    left_end = len(firstArray)-1
    right_start = 0
    right_end = len(secondArray)-1
    
    newArray = []

    while left_start <= left_end or right_start <= right_end:
        if left_start > left_end:
            newArray.append(secondArray[right_start])
            right_start +=1
        elif right_start > right_end:
            newArray.append(firstArray[left_start])
            left_start +=1
        elif compare(secondArray[right_start] , firstArray[left_start]) == 1:
            newArray.append(firstArray[left_start])
            left_start +=1
        elif compare(firstArray[left_start] , secondArray[right_start])==1:
            newArray.append(secondArray[right_start])
            right_start +=1
    
    return newArray


def patiencesort(array, compare):
    lst = []

    for index in range(len(array)) :
        pos = 0
        while (pos < len(lst) and compare(array[index], lst[pos][-1]) == -1):
            pos += 1

        if pos < len(lst):
            lst[pos].append(array[index])
        else:
            lstaux = []
            lstaux.append(array[index])
            lst.append(lstaux)
    

    while(len(lst) > 1):
        a = lst.pop()
        b = lst.pop()
        res = merge(a, b, compare)
        lst.append(res)
    
    return lst[0]