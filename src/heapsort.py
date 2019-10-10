
''' o  Heap  Sort  o  vetor ́e visto como uma  ́arvore bin ́aria,  
onde ordena os elementos a medida que os insere naestrutura.   
O  heap(monte)  ́e  gerado  e  montado  no  pr ́oprio  vetor.   C
omparado  a  outrosalgoritmos  de  ordena ̧c ̃ao  possui  um  bom  desempenho 
 e  bom  uso  de  mem ́oria  pois  n ̃aonecessita de recurs ̃ao.  Baseado nisso 
 sua complexidade tanto no pior, melhor e no m ́ediocaso  ́e de Θ(nlogn).'''

def heapsort_pilha(array, stackSize, compare):
        change = False
        i = 0
        while i < stackSize:
            left_node = 2 * i + 1
            right_node = 2 * i + 2
            # verificar se o filho esquerdo da raiz existe e é maior que q raiz.
            if ((left_node < stackSize) and (compare(array[i] , array[left_node]) == -1)):
                array[i], array[left_node] = array[left_node], array[i]
                change = True
            # verificar se o filho da direita da raiz existe e é maior que q raiz. 
            if ((right_node < stackSize) and (compare(array[i] , array[right_node]) == -1)):
                array[i], array[right_node] = array[right_node], array[i]
                change = True
            i +=1
        return change


def heapsort(array, compare):
    arraySize = len(array)
    while arraySize > 1:
        change = True
        
        while change:
            change = heapsort_pilha(array, arraySize, compare)
        
        array[arraySize-1], array[0] = array[0], array[arraySize-1]
        arraySize -=1
    
    return array