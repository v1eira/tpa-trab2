import sys
import time

def main():
    args = sys.argv
    arq = open(args[1], 'r')
    entrada = arq.readline()
    entrada = arq.readlines()
    arquivo = open(args[2], 'w+')
    print("Inicio da ordenação")
    ini = time.time()
    array = []
    linha = 0
    for linha in entrada:
        array.append(linha.split(",")[2])
    for indice in range(1,len(array)):
        bol = True
        while indice>0 and bol:
            if(array[indice]<array[indice - 1]):
                aux = entrada[indice]
                entrada[indice] = entrada[indice - 1]
                entrada[indice - 1] = aux
                aux2 = array[indice]
                array[indice] = array[indice - 1]
                array[indice - 1] = aux2
                indice -=1
            else:
                bol = False

    fim = time.time()
    print("Fim ordenação")
    print("Gravando...")

    arquivo.writelines("insertsort,"+str(len(entrada))+"," +str(fim-ini)+"\n")
    #arquivo.writelines(entrada)

    arquivo.close()
    arq.close()

if __name__ == "__main__":
    main()