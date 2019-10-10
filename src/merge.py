import sys
import time


def merge(array,inicio,fim):
    meio = (inicio + fim)//2
    esq_ini = inicio
    esq_fim = meio
    dir_ini = meio + 1
    dir_fim = fim
    aux = []
    auxArray = []
    while esq_ini <= esq_fim or dir_ini <= dir_fim:
        if esq_ini > esq_fim:
            aux.append(entrada[dir_ini])
            auxArray.append(array[dir_ini])
            dir_ini +=1
        elif dir_ini > dir_fim:
            aux.append(entrada[esq_ini])
            auxArray.append(array[esq_ini])
            esq_ini +=1
        elif array[dir_ini] > array[esq_ini]:
            aux.append(entrada[esq_ini])
            auxArray.append(array[esq_ini])
            esq_ini +=1
        elif array[esq_ini] > array[dir_ini]:
            aux.append(entrada[dir_ini])
            auxArray.append(array[dir_ini])
            dir_ini +=1
    
    for k in range(0,len(aux)):
        array[inicio + k] = auxArray[k]
        entrada[inicio + k] = aux[k]

def merge_div(array,inicio, fim):
    if inicio >= fim:
        return
    
    meio = (inicio + fim)//2

    merge_div(array,inicio,meio)
    merge_div(array,meio+1,fim)

    merge(array,inicio,fim)



def main():
    args = sys.argv
    arq = open(args[1], 'r')
    arquivo = open(args[2], 'w+')
    global entrada
    entrada = arq.readline()
    entrada = arq.readlines()

    ini = time.time()

    array = []

    for linha in entrada:
        array.append(linha.split(",")[2])

    merge_div(array,0,len(array)-1)

    fim = time.time()
    print("Fim ordenação")
    print("Gravando...")

    arquivo.writelines("selectsort,"+str(len(entrada))+"," +str(fim-ini)+"\n")
    arquivo.writelines(entrada)

    arquivo.close()
    arq.close()

if __name__ == "__main__":
    main()
