
''' o  Heap  Sort  o  vetor ́e visto como uma  ́arvore bin ́aria,  
onde ordena os elementos a medida que os insere naestrutura.   
O  heap(monte)  ́e  gerado  e  montado  no  pr ́oprio  vetor.   C
omparado  a  outrosalgoritmos  de  ordena ̧c ̃ao  possui  um  bom  desempenho 
 e  bom  uso  de  mem ́oria  pois  n ̃aonecessita de recurs ̃ao.  Baseado nisso 
 sua complexidade tanto no pior, melhor e no m ́ediocaso  ́e de Θ(nlogn).'''

def heapsort_pilha(tamanho_pilha): 
        troca = False
        i = 0
        while i < tamanho_pilha:
            Tno_esquerdo = 2 * i + 1      
            Tno_direito = 2 * i + 2     
            # verificar se o filho esquerdo da raiz existe e é maior que q raiz. 
            if Tno_esquerdo < tamanho_pilha and comparaLinha(entrada[i] , entrada[Tno_esquerdo])==-1: 
                aux = entrada[i]
                entrada[i] = entrada[Tno_esquerdo]
                entrada[Tno_esquerdo] = aux
                troca = True
            # verificar se o filho da direita da raiz existe e é maior que q raiz. 
            if Tno_direito < tamanho_pilha and comparaLinha(entrada[i] , entrada[Tno_direito])==-1: 
                aux = entrada[i]
                entrada[i] = entrada[Tno_direito]
                entrada[Tno_direito] = aux
                troca = True
            i +=1
        return troca
            




def comparaLinha(alin,blin):
    aval = alin.split(",")[2]
    bval = blin.split(",")[2]
    if aval > bval:
        return 1
    elif aval < bval:
        return -1
    else:
        return 0


import sys
import time

def main():
    args = sys.argv

    #lstEntradas = ["data_10e0","data_10e1","data_10e2","data_10e3","data_10e4","data_10e5","data_25e0","data_25e1","data_25e2","data_25e3","data_25e4","data_25e5","data_50e0","data_50e1","data_50e2","data_50e3","data_50e4","data_50e5","data_75e0","data_75e1","data_75e2","data_75e3","data_75e4","data_75e5"]
    lstEntradas = ["data_10e0"]
    for i in lstEntradas:
        for j in range(0,3):
            arq = open(i+".csv", 'r')
            global entrada
            entrada = arq.readline()
            entrada = arq.readlines()
            arquivo = open("heapsort"+i[4:]+"_saida"+str(j)+".csv", 'w+')
            ini = time.time()
            
            tamF=len(entrada)
            while tamF>1:
                troca = True
                while troca:
                    troca = heapsort_pilha(tamF)
                
                aux = entrada[tamF - 1]
                entrada[tamF - 1] = entrada[0]
                entrada[0] = aux
                tamF -=1
            



            fim = time.time()
            print("Fim ordenação")
            print("Gravando...")

            arquivo.writelines("heapsort,"+str(len(entrada))+"," +str(fim-ini)+"\n")
            arquivo.writelines(entrada)

            arquivo.close()
            arq.close()
    print ("FIM DE TODO O PROCESSO - MONIQUE JÁ PODE DESLIGAR O COMPUTADOR")

if __name__ == "__main__":
    main()