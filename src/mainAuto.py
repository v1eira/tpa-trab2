import sys
import time
import os
import signal

from Person import Person
from selectionsort import selectionsort
from insertionsort import insertionsort
from mergesort import mergesort
from quicksort import quicksort
from heapsort import heapsort
from introsort import introsort
from patiencesort import patiencesort


def timeout(signum, frame):
    raise Exception("Algoritmo não terminou em 15 minutos.\n")


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
    signal.signal(signal.SIGALRM, timeout)

    dataPath = os.path.abspath('../data/')
    outputPath = os.path.abspath('../output/')

    dataset = [
    "data_10e0.csv",
    "data_10e1.csv",
    "data_10e2.csv",
    "data_10e3.csv",
    "data_10e4.csv",
    "data_10e5.csv",
    "data_25e0.csv",
    "data_25e1.csv",
    "data_25e2.csv",
    "data_25e3.csv",
    "data_25e4.csv",
    "data_25e5.csv",
    "data_50e0.csv",
    "data_50e1.csv",
    "data_50e2.csv",
    "data_50e3.csv",
    "data_50e4.csv",
    "data_50e5.csv",
    "data_75e0.csv",
    "data_75e1.csv",
    "data_75e2.csv",
    "data_75e3.csv",
    "data_75e4.csv",
    "data_75e5.csv"]

    algorithms = [
    selectionsort,
    insertionsort,
    mergesort,
    quicksort,
    heapsort,
    introsort,
    patiencesort]

    arqOut = open(outputPath + '/' + "tests.csv", 'w+')
    arqOut.write("algorithm,numElements,time\n")

    for algorithm in algorithms:
        print("\n\n")
        print(str(algorithm.__name__) + "\n")
        for csv in dataset:
            arqIn = open(dataPath + '/' + csv, 'r')

            print("\nProcessando " + csv + " ...")

            csvData = arqIn.readline()
            csvData = arqIn.readlines()
            
            numberOfLines = len(csvData)

            for i in range(3): # realizar ordenação 3 vezes para cada CSV
                array = fillArray(csvData)
                print("Iniciando ordenação")

                start = time.time()
                
                try:
                    signal.alarm(900)
                    array = algorithm(array, compare)
                    signal.alarm(0)
                except Exception as e:
                    arqOut.write(algorithm.__name__ + "," + str(numberOfLines) + "," + "-1" + "\n")
                    print(e)
                    break
                
                end = time.time()

                print("Fim ordenação\n")
                arqOut.write(algorithm.__name__ + "," + str(numberOfLines) + "," + str((end-start)*1000) + "\n")
            
            arqIn.close()
    
    arqOut.close()

if __name__ == "__main__":
    main()