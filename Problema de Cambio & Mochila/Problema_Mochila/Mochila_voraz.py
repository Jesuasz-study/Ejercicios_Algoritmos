from time import time

def mochila(w,v,Vw,Wtotal):
    x = []
    Wsum = 0
    Vsum =0
    peso = 0
    for i in range(0,len(Vw)):
        x.append(0)

    while peso < Wtotal:
        mayor = max(Vw)
        indx = Vw.index(mayor)
        if(peso + w[indx] < Wtotal):
            x[indx] = 1
            peso = peso + w[indx]
            Vw[indx] = 0 #Evita que se repita este valor al buscar la cantidad mayor 
            Vsum = Vsum + v[indx]
        else:
            x[indx] = (Wtotal - peso)/w[indx]
            peso = peso + w[indx]*x[indx]
            Vw[indx] = 0
            Vsum = Vsum + (v[indx]*x[indx])
    #print('Valor: '+str(Vsum))
    return x,Vsum

def leer_Archivo(nombre):#lee el archivo con denomi de las monedas
    archivo = open(nombre,'r')
    lista_monedas = archivo.readlines()
    for i in range(0,len(lista_monedas)):#quita caracteres de salto de linea
        lista_monedas[int(i)] = lista_monedas[int(i)].rstrip('\n')
    lista = list(map(int,lista_monedas))#lleva de str a int de la lista leida
    return lista

def main():
    nombre_pesos = 'pesos_voraz.txt'
    nombre_valores = 'valores_voraz.txt'
    w = leer_Archivo(nombre_pesos)
    v = leer_Archivo(nombre_valores)
    Wtotal = int(input("Peso maximo que puede soportar la mochila:"))
    start_time = time()
    Vw = []
    for i in range(0,len(w)):
        Vw.append(v[i]/w[i])
    result,Vs = mochila(w,v,Vw,Wtotal)
    print('***Maximo v/w***')
    print('Valor: '+str(Vs))
    print(result)
    elapsed_time = time() - start_time
    print('Tiempo de ejecucion: ' + str(elapsed_time)+' seg')

if __name__ == "__main__":
    main()