from time import time

def devolver_Cambio(n,denominaciones):#n es la cantidad a dar como cambio
    Cambio = dict.fromkeys(denominaciones,0)#crea diccionario, indica num de monedas de cada denominacion
    s = 0 #La suma de los elementos que se guarden en S
    x = 0#el valor de la moneda en cada iteracion
    while s < n:
        for valor in range(0,len(denominaciones)):#elige el mayor elemento  de D
            if (denominaciones[valor] + s) <= n:#compara la deuda con el valor de un elemento
                x = denominaciones[valor]# le asignamos el valor a x
                break #cortamos esa iteracion ya que econtró una moneda valida
            else:
                x = 0 #el valor de x es 0 para no afectar en el calculo de la deuda
        if x == 0:#este es el If/Else que aparece en el pseudocodigo solo que invertido
            return False
        else:
            s = s+x#Se actualiza el valor de la deuda menos nuevo elemento del conjunto
            Cambio[x] += 1 #actualiza la cantidad en el conjunto solucion

    return Cambio #cuando se da solucion se regresa el conjunto solucion

def leer_Archivo():#lee el archivo con denomi de las monedas
    archivo = open('monedas.txt','r')
    lista_monedas = archivo.readlines()
    for i in range(0,len(lista_monedas)):#quita caracteres de salto de linea
        lista_monedas[int(i)] = lista_monedas[int(i)].rstrip('\n')
    lista = list(map(int,lista_monedas))#lleva de str a int de la lista leida
    return lista

def main():
    lista = leer_Archivo()
    cambio = int(input("Ingrese el monto de cambio:"))
    start_time = time()
    Sol = devolver_Cambio(cambio,lista)
    if Sol == False:
        print("No hay solucion posible")
    else:
        print(Sol)
    elapsed_time = time() - start_time
    print('Tiempo de ejecucion: ' + str(elapsed_time)+' seg')

if __name__ == "__main__":
    main()