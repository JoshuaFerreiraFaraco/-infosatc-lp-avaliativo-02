#Criacao da lista e inputs
lista = []
a1 = input("Digite um valor a ser inserido na lista: ")
a2 = input("Digite um valor a ser inserido na lista: ")
a3 = input("Digite um valor a ser inserido na lista: ")
a4 = input("Digite um valor a ser inserido na lista: ")
a5 = input("Digite um valor a ser inserido na lista: ")

#Definindo posiçao
lista.insert(0,a1)
lista.insert(1,a2)
lista.insert(2,a3)
lista.append(a5)
lista.insert(3,a4)

#Copiando a lista
lista_copia = lista.copy()
print(lista_copia)