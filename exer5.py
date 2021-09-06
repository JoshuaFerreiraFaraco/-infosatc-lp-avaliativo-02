#Definiçao da lista e inputs
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

#Caso nao tenha algo com o nome Melancia na lista
if "Melancia" in lista:
    print("Melancia está na lista!")
else:
    print("Melancia nao está na lista!")