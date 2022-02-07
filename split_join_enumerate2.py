"""
*split - dividir uma string # str
*join - juntar uma lista # str
*enumerate - enumerar elementos da lista # list / iteráveis

"""

var_str = "Aranha arranha o jarro, o jarro arranha a aranha..."

lista = var_str.split(",")

for valor in lista:
    print(valor.strip().capitalize())

# função Join


var2 = "O Brasil é penta"
lista = var2.split(" ")
var3 = ",".join(lista)

print(var2)
print(lista)
print(var3)