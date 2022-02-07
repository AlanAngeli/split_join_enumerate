"""
*split - dividir uma string # str
*join - juntar uma lista # str
*enumerate - enumerar elementos da lista # list / iteráveis

"""

#enumerate

#índice[1] [2]  [3] [4]       1 = [O] 2 = [Brasil] 3 = [é] 4 = [penta]
var = "O Brasil é penta"
lista = var.split(" ")
print("Lista 1:")
for indice, valor in enumerate(lista):
    print(indice, valor)
print()

print("Lista 2:")

lista2 = ["Alan", "Maria", "Klelson"]

for indice, valor in enumerate(lista2):
    print(indice, valor)
print()

n1, n2, n3 = lista2 #n1 = Alan, n2 = Maria, n3 = Klelson

print(n1)
print(n2)
print(n3)