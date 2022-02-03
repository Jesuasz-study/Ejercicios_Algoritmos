import numpy as np

def palabra(tab,Xa):
    i = tab.shape[0]-1
    j = tab.shape[1]-1
    res = []
    while i!=0:
        if(tab[i][j] == tab[i-1][j]):
            i = i-1
        elif(tab[i][j] != tab[i-1][j]):
            while j!=0:
                if(tab[i][j] == tab[i][j-1]):
                    j = j-1
                elif(tab[i][j] != tab[i][j-1]):
                    j = j-1
                    res.insert(0,Xa[i-1])
                    break
        
    return res

def table(lx,ly):
    tab = np.zeros((lx+1,ly+1))
    return tab

def LCS(tab,lx,ly,Xa,Ya):
    for i in range(1,lx+1):
        for j in range(1,ly+1):
            if Xa[i-1] == Ya[j-1]:
                tab[i][j] = tab[i-1][j-1] + 1
            elif Xa[i-1] != Ya[j-1]:
                tab[i][j] = max(tab[i-1][j],tab[i][j-1])
    return tab   

def max(a,b):
    if a>b:
        return a
    else:
        return b

def leer_Archivo():#lee el archivo con denomi de las monedas
    lista_monedas = []
    for i in range(1,3):
        archivo = open('Ejercicio'+str(i)+'.txt','r')
        lista_monedas.append(archivo.readline())
    return lista_monedas

def main():
    lista = leer_Archivo()
    X = lista[0]
    Y = lista[1]
    Xa = np.array(list(X))
    Ya = np.array(list(Y))
    tab = table(len(X),len(Y))
    tab = LCS(tab,len(X),len(Y),Xa,Ya)
    resultado = palabra(tab,Xa)
    print('--Resultado del LCK dinamico--\n')
    print(resultado)
    print(tab)

if __name__ == "__main__":
    main()