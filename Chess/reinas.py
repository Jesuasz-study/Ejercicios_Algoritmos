import numpy as np 

def colocar_reinas(no_reinas):
    tablero_np = np.zeros((8,8))
    if no_reinas == 0:
        for i in range(0,8):
            reina_posicion = np.random.randint(0,7,size=2)
            tablero_np[reina_posicion[0],reina_posicion[1]] = 1
        return tablero_np
        ###################################################################
    elif no_reinas == 3:
        tablero_np[5][0] = 1
        tablero_np[3][1] = 1
        tablero_np[0][2] = 1
        for i in range(0,5):
            reina_posicion = np.random.randint(0,7,size=2)
            tablero_np[reina_posicion[0],reina_posicion[1]] = 1
        return tablero_np
        ##################################################################
    elif no_reinas == 4:
        tablero_np[5][0] = 1
        tablero_np[3][1] = 1
        tablero_np[0][2] = 1
        tablero_np[4][3] = 1
        for i in range(0,4):
            reina_posicion = np.random.randint(0,7,size=2)
            tablero_np[reina_posicion[0],reina_posicion[1]] = 1
        return tablero_np
        #################################################################
    elif no_reinas == 5:
        tablero_np[5][0] = 1
        tablero_np[3][1] = 1
        tablero_np[0][2] = 1
        tablero_np[4][3] = 1
        tablero_np[7][4] = 1
        for i in range(0,3):
            reina_posicion = np.random.randint(0,7,size=2)
            tablero_np[reina_posicion[0],reina_posicion[1]] = 1
        return tablero_np

def problema_reinas(tablero):
    lista_ataque = []
    for f in range(0,8):
        for c in range(0,8):
            if tablero[f][c] == 1:
                ataque = revisar_ataque(tablero,f,c)
                lista_ataque.append(ataque)
    for n in lista_ataque:
        or_ataque = lista_ataque[n] | lista_ataque[n+1]
    if or_ataque == 1:
        return False
    elif or_ataque == 0:
        return True

def revisar_ataque(tablero,f,c):
    aux_f = f
    aux_c = c
    aux_lin = 0
    aux_tablero = np.copy(tablero)
    while aux_lin < 8:
        if aux_f == f and aux_lin == c:
            aux_lin += 1
            continue
        if(aux_tablero[aux_f][aux_lin] == 1):
            return 1
        aux_lin += 1

    aux_lin = 0
    while aux_lin < 8:
        if(aux_lin == f and aux_c == c):
            aux_lin += 1
            continue
        if(aux_tablero[aux_lin][aux_c] == 1):
            return 1
        aux_lin += 1
    
    while aux_f >=0 or aux_c>=0:
        if(aux_f < 0 or aux_c < 0):
            break
        else:
            if(aux_f == f and aux_c == c):
                aux_f = aux_f-1
                aux_c = aux_c-1
                continue
            if(aux_tablero[aux_f][aux_c] == 1):
                return 1
            aux_f = aux_f-1
            aux_c = aux_c-1

    aux_f4 = f
    aux_c4 = c
    while aux_f4 <=7 or aux_c4<=7:
        if(aux_c4 > 7 or aux_f4 > 7):
            break
        else:
            if(aux_f4 == f and aux_c4 == c):
                aux_f4 += 1
                aux_c4 += 1
                continue
            if(aux_tablero[aux_f4][aux_c4] == 1):
                return 1
            aux_f4 += 1
            aux_c4 += 1

    aux_f2 = f
    aux_c2 = c
    while aux_f2>=0 or aux_c2<=7:
        if(aux_f2<0 or aux_c2>7):
            break
        else:
            if(aux_f2 == f and aux_c2 == c):
                aux_f2 = aux_f2 - 1 
                aux_c2 += 1
                continue
            if(aux_tablero[aux_f2][aux_c2] == 1):
                return 1
            aux_f2 = aux_f2 - 1 
            aux_c2 += 1

    aux_f3 = f
    aux_c3 = c
    while aux_f3<=7 or aux_c3>=0:
        if(aux_f3>7 or aux_c3<0):
            break
        else:
            if(aux_c3 == c and aux_f3 == f):
                aux_f3 += 1
                aux_c3 = aux_c3 -1
                continue
            if(aux_tablero[aux_f3][aux_c3] == 1):
                return 1
            aux_f3 += 1
            aux_c3 = aux_c3 -1 
    return 0

def main():
    ciclo = 1000
    no_reinas = input('¿No de reinas a colocar fijas en el tablero? Op:0 - 3 - 4 - 5\n')
    no_reinas = int(no_reinas)
    while ciclo <= 1000000:
        archivo = open('resultados-5reinas','a')
        aciertos = 0
        for i in range(0,ciclo):
            tablero = colocar_reinas(no_reinas)
            resultado = problema_reinas(tablero)
            if resultado == True:
                aciertos += 1
        print(str(aciertos))
        archivo.write(str(aciertos)+'\n')
        ciclo = ciclo*10
    archivo.close()

if __name__ == "__main__":
    main()