import numpy as np
from time import time

def monedas(valores,tabla):
    for i in range(0,(len(valores))):
        for j in range(1,len(tabla[1,:])):
            if j < valores[i]:
                tabla[i,j] = tabla[i-1,j]
            elif i-1 < 0:
                tabla[i,j] = 1 + tabla[i,j-valores[i]]
            else:
                tabla[i,j] = min(tabla[i-1,j],1 + tabla[i,j-valores[i]])
    return tabla

def min(a,b):
    if a > b:
        return b
    else:
        return a

def leer_Archivo():#lee el archivo con denomi de las monedas
    archivo = open('monedas_dinam.txt','r')
    lista_monedas = archivo.readlines()
    for i in range(0,len(lista_monedas)):#quita caracteres de salto de linea
        lista_monedas[int(i)] = lista_monedas[int(i)].rstrip('\n')
    lista = list(map(int,lista_monedas))#lleva de str a int de la lista leida
    return lista

def main():
    lista = leer_Archivo()
    valores_aux = np.asarray(lista)
    print("**Denominaciones**")
    print(valores_aux)
    cantidad = int(input("Ingrese el monto de cambio:"))
    start_time = time()
    tabla = np.zeros((len(valores_aux), cantidad+1))
    resultado = monedas(valores_aux,tabla)
    print(resultado)
    print('La cantidad minima de monedas como cambio')
    print(resultado[(len(tabla[:,1])-1),(len(tabla[1,:])-1)])
    elapsed_time = time() - start_time
    print('Tiempo de ejecucion: ' + str(elapsed_time)+' seg')
    
if __name__ == "__main__":
    main()