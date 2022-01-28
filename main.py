'''
1. Feladat
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál, és ezeket a listákat egy 'tarolo' nevű listába helyezi. 
A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
'''

from random import randrange

tarolo = []

lista1 = [randrange(0,25,1) for i in range(3)]
lista2 = [randrange(0,25,1) for i in range(3)]
lista3 = [randrange(0,25,1) for i in range(3)]
lista4 = [randrange(0,25,1) for i in range(3)]

tarolo.append(lista1)
tarolo.append(lista2)
tarolo.append(lista3)
tarolo.append(lista4)

print(tarolo)