import numpy as np
from binarytree import tree, Node

def palabra():
    word = 'allelujah'
    table = dict()
    simple_list = list()
    for letter in word:
        string_table(table,letter)
    for i in table:
        simple_list.append([table[i],i])
    simple_list = ordering(simple_list)
    print(simple_list)
    return simple_list

def string_table(table,letter):
    if letter in table:
        table[letter] = table[letter] + 1
    else:
        table[letter] = 1

def ordering(list):
    list.sort()
    return list

def arbol_binario(simple_list):
    pass

def main():
    simple_list = palabra()
    arbol_binario(simple_list)
    
if __name__ == "__main__":
    main()