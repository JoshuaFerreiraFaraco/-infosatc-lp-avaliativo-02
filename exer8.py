listaCompras = []

a1 = input("Digite o que voce deseja comprar: ")
a2 = input("Digite o que voce deseja comprar: ")
a3 = input("Digite o que voce deseja comprar: ")
a4 = input("Digite o que voce deseja comprar: ")

listaCompras.insert(0,a1)
listaCompras.append(a2)
listaCompras.insert(1,a3)
listaCompras.insert(2,a4)

print(listaCompras)

listaCompras.remove("RTX")
listaCompras.remove("Gabinete")

print(listaCompras)
