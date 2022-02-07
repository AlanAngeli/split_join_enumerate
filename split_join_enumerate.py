"""
*split - dividir uma string # str
*join - juntar uma lista # str
*enumerate - enumerar elementos da lista # list / iteráveis

"""

var_str = "O rato roeu a roupa do rei de Roma, o rei ficou bravo."
lista = var_str.split(" ")
lista2 = var_str.split(",")

print(var_str)
print(lista)
print(lista2)

#for valor in lista:
#    print(valor)



for valor in lista:
    print("A palavra", "'",valor,"'", "apareceu", lista.count(valor),"vezes na frase.")

palavra = ""
contagem = 0

for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print("A palavra que apareceu mais vezes é: ", palavra, contagem,"vezes")