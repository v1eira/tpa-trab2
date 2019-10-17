import sys
import time
import os

from Person import Person
from selectionsort import selectionsort
from insertionsort import insertionsort
from mergesort import mergesort
from quicksort import quicksort
from heapsort import heapsort
from introsort import introsort
from patiencesort import patiencesort


def compare(a: Person, b: Person):
    if a.uid < b.uid:
        return -1
    
    if a.uid > b.uid:
        return 1

    else:
        return 0


def fillArray(csvData):
    array = []
    for line in csvData:
        data = line.split(",")
        p = Person(data[0], data[1], data[2], data[3], data[4], data[5])
        array.append(p)
    
    return array


def main():
    args = sys.argv

    dataPath = os.path.abspath('../data/')
    outputPath = os.path.abspath('../output/')

    dataset = ["data_10e0.csv",
    "data_10e1.csv",
    "data_10e2.csv",
    "data_10e3.csv",
    "data_10e4.csv",
    "data_25e0.csv",
    "data_25e1.csv",
    "data_25e2.csv",
    "data_25e3.csv",
    "data_25e4.csv",
    "data_50e0.csv",
    "data_50e1.csv",
    "data_50e2.csv",
    "data_50e3.csv",
    "data_50e4.csv",
    "data_75e0.csv",
    "data_75e1.csv",
    "data_75e2.csv",
    "data_75e3.csv",
    "data_75e4.csv"]

    algorithm = args[1]
    csvIn = args[2]
    csvOut = args[3]

    if csvIn not in dataset:
        return print("Arquivo de entrada inválido.")

    arqIn = open(dataPath + '/' + csvIn, 'r')
    arqOut = open(outputPath + '/' + csvOut, 'w+')

    print("Processando arquivo...")

    csvData = arqIn.readline()
    csvData = arqIn.readlines()

    array = fillArray(csvData)

    print("Iniciando ordenação")

    start = time.time()

    if algorithm == "selectsort":
        array = selectionsort(array, compare)
    elif algorithm == "insertsort":
        array = insertionsort(array, compare)
    elif algorithm == "mergesort":
        array = mergesort(array, 0, len(array)-1, compare)
    elif algorithm == "quicksort":
        array = quicksort(array, compare)
    elif algorithm == "heapsort":
        array = heapsort(array, compare)
    elif algorithm == "introsort":
        array = introsort(array, compare)
    elif algorithm == "patiencesort":
        array = patiencesort(array, compare)
    else:
        return print("Algoritmo inválido.")

    end = time.time()

    print("Fim ordenação")

    print(algorithm + "       " + str(len(csvData)) + "       " + str((end-start)*1000) + "\n")

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