import sys
import time
import os

from Person import Person
from compare import compare
from quicksort import quicksort

def main():
    args = sys.argv

    dataPath = os.path.abspath('data')
    outputPath = os.path.abspath('output')

    arqIn = open(dataPath + '/' + 'data_25e2.csv', 'r')
    arqOut = open(outputPath + '/' + 'quicksort_data_25e2.csv', 'w+')

    print("Processando arquivo...")
    csvData = arqIn.readline()
    csvData = arqIn.readlines()

    array = []

    for line in csvData:
        data = line.split(",")
        p = Person(data[0], data[1], data[2], data[3], data[4], data[5])
        array.append(p)

    print("Iniciando ordenação")

    start = time.time()

    array = quicksort(array, compare)

    end = time.time()

    print("Fim ordenação")

    print("quicksort       "+str(len(csvData))+"       " +str(end-start)+"\n")

    print("Escrevendo csv...")
    
    for p in array:
        arqOut.write(p.email + ",")
        arqOut.write(p.gender + ",")
        arqOut.write(p.uid + ",")
        arqOut.write(p.birthdate + ",")
        arqOut.write(p.height + ",")
        arqOut.write(p.weight)

    arqOut.close()
    arqIn.close()

if __name__ == "__main__":
    main()