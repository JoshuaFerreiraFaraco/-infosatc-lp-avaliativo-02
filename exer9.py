#Definiçao da lista e inputs
lista = []

a1 = input("Digite um numero: ")
a2 = input("Digite um numero: ")
a3 = input("Digite um numero: ")
a4 = input("Digite um numero: ")

#Definindo posiçao
lista.insert(0,a1)
lista.append(a2)
lista.insert(1,a3)
lista.insert(2,a4)

#Ordenando em ordem menor para o maior 
print(sorted(lista))