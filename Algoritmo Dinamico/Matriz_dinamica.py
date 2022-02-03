import numpy as np 
from time import time

def recibir_matriz_P():
    P = []
    d = {}
    Paux = []
    archivo = open('matrices.txt','r')
    lista_matrices = archivo.readlines()
    for i in range(0,len(lista_matrices)):
        lista_matrices[int(i)] = lista_matrices[int(i)].rstrip('\n')
    lista = list(map(str,lista_matrices))
    print('--Matrices--')
    print(lista)
    for i in range(len(lista)):
        st = lista[i].split()
        P.append(st[0])
        P.append(st[1])
    Paux.append(P[0])
    Paux.append(P[1])
    i = 3

    while i <= len(P):
        Paux.append(P[i])
        i +=2
    Paux = [int(i) for i in Paux]
    print(Paux)
    return Paux

def matriz_M_S(P):
    size = len(P)-1
    M = np.zeros((size,size))
    S = np.zeros((size,size))
    return M,S

def calcular_MS(P,M,S):
    n = len(P)-1
    for i in range(0,n):
        M[i][i] = 0
    for l in range(1,n):
        for i in range(0,n-l):
            j = i + l 
            M[i][j] = 1000000000
            for k in range(i,j):
                Q = M[i][k] + M[k+1][j] + (P[i]*P[k+1]*P[j+1])
                if Q < M[i][j]:
                    M[i][j] = Q
                    S[i][j] = k
    return M,S

def Imprimir_parentesis(Sf,i,j,result):
    if i == j:
        result.append('A')
    else:
        result.append('(')
        nj = int(Sf[i][j])
        ni = int(Sf[i][j]+1)
        Imprimir_parentesis(Sf,i,nj,result)
        Imprimir_parentesis(Sf,ni,j,result)
        result.append(')')

def main():
    P = recibir_matriz_P()
    start_time = time()
    M,S = matriz_M_S(P)
    Mf,Sf = calcular_MS(P,M,S)
    print('\n')
    print(Mf)
    j = len(Sf)-1
    i = 0
    result = []
    Imprimir_parentesis(Sf,i,j,result)
    print('\n')
    print('Distribucion Parentesis')
    print(result)
    elapsed_time = time() - start_time
    print('Tiempo de ejecucion: ' + str(elapsed_time)+' seg')

    

if __name__ == "__main__":
    main()
