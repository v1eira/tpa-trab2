import sys
import time

def main():
    args = sys.argv

    arq = open(args[1], 'r')
    arquivo = open(args[2], 'w+')
    entrada = arq.readline()
    entrada = arq.readlines()

    ini = time.time()

    array = []

    for linha in entrada:
        array.append(linha.split(",")[2])

    for indice in range(0,len(array)) :
        minimo = indice
        for bmin in range(indice+1,len(array)):
            if array[bmin] < array[minimo]:
                minimo = bmin
        transicao = entrada[indice]
        entrada[indice] = entrada[minimo]
        entrada[minimo] = transicao
        transicao = array[indice]
        array[indice] = array[minimo]
        array[minimo] = transicao

    fim = time.time()
    print("Fim ordenação")
    print("Gravando...")

    arquivo.writelines("selectsort,"+str(len(entrada))+"," +str(fim-ini)+"\n")
    arquivo.writelines(entrada)

    arquivo.close()
    arq.close()

if __name__ == "__main__":
    main()