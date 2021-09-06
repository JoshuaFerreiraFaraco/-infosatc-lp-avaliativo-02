#Definiçao da lista e inputs
listaCompras = []

a1 = input("Digite o que voce deseja comprar: ")
a2 = input("Digite o que voce deseja comprar: ")
a3 = input("Digite o que voce deseja comprar: ")
a4 = input("Digite o que voce deseja comprar: ")

#Definindo posiçao
listaCompras.insert(0,a1)
listaCompras.append(a2)
listaCompras.insert(1,a3)
listaCompras.insert(2,a4)

#Printando a lista
print(listaCompras)

#Removendo os valores RTX e Gabinete
listaCompras.remove("RTX")
listaCompras.remove("Gabinete")

#Mostrando a lista final
print(listaCompras)
