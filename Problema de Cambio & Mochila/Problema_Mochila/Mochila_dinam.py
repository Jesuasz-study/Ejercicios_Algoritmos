import numpy as np
from time import time

def monedas(valores,tabla,peso):
    for i in range(0,(len(valores))):
        for j in range(1,len(tabla[1,:])):
            if j-peso[i] < 0:
                tabla[i,j] = tabla[i-1,j]
            else:
                tabla[i,j] = max((tabla[i-1,j]),(tabla[i-1,j-peso[i]]+valores[i]))        
    return tabla

def max(a,b):
    if a > b:
        return a
    else:
        return b

def leer_Archivo(nombre):#lee el archivo con denomi de las monedas
    archivo = open(nombre,'r')
    lista_monedas = archivo.readlines()
    for i in range(0,len(lista_monedas)):#quita caracteres de salto de linea
        lista_monedas[int(i)] = lista_monedas[int(i)].rstrip('\n')
    lista = list(map(int,lista_monedas))#lleva de str a int de la lista leida
    return lista

def main():
    nombre_valores = 'valores_dinam.txt'
    nombre_pesos = 'pesos_dinam.txt'
    list_val = leer_Archivo(nombre_valores)
    valores = np.asarray(list_val)
    list_pesos = leer_Archivo(nombre_pesos)
    peso = np.asarray(list_pesos)
    Wmax = int(input("Peso maximo que puede soportar la mochila:"))
    start_time = time()
    tabla = np.zeros((len(peso),Wmax+1))
    resultado = monedas(valores,tabla,peso)
    print(resultado)
    print('Valor maximo de los objetos que podemos transportar:')
    print(resultado[(len(tabla[:,1])-1),(len(tabla[1,:])-1)])
    elapsed_time = time() - start_time
    print('Tiempo de ejecucion: ' + str(elapsed_time)+' seg')
    
if __name__ == "__main__":
    main()