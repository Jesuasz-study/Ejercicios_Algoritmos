import numpy as np
def recibir_matriz():
    #Esta funcion toma la matriz de .txt y la vuelve matriz de numpy
    #trabajo a futuro: hacer que funcione con cualquer tamaño de matriz
    matriz = []
    archivo = open('matriz.txt','r')
    for linea in archivo:
        matriz.append(linea.strip().split())
    print('--Matriz--')
    matriz_0 = list(map(int,matriz[0]))
    matriz_1 = list(map(int,matriz[1]))
    matriz_2 = list(map(int,matriz[2]))
    matriz_3 = list(map(int,matriz[3]))
    matriz_4 = list(map(int,matriz[4]))
    m_completa = np.array([[i for i in matriz_0],
                    [i for i in matriz_1],
                    [i for i in matriz_2],
                    [i for i in matriz_3],
                    [i for i in matriz_4]])
    archivo.close()
    return m_completa

def menor(vertx,fila,weights,nodo_inicio):
    menor = 100
    fila = list(fila)
    for i in range (0,5):
        if i in vertx:
            continue
        else:
            if fila[i] <= menor:
                menor = fila[i]
    if menor == 100:
        idx = nodo_inicio
        menor = fila[idx]
    else:
        idx = fila.index(menor)
    vertx.add(idx)
    print('Hacia nodo ' + str(idx) + ' con costo de ' + str(menor))
    weights.add(menor)
    return idx

def camino(matrix,vertx,weights,index):
    nodo_inicio = index
    vertx.add(index)
    print('Parte de nodo ' + str(index))
    for _ in range(1,6):
        fila = matrix[index,:]
        idx = menor(vertx,fila,weights,nodo_inicio)
        index = idx
    print("--Costo--")
    print(weights)
    sum = 0
    for element in weights:
        sum = sum + element
    print(sum)

def main():
    matrix = recibir_matriz()
    print(matrix)
    vertx = set()
    weights = set()
    index = input("Ingrese el nodo inicial: ")
    index = int(index)
    print("--Ruta--")
    camino(matrix,vertx,weights,index)

if __name__ == "__main__":
    main()