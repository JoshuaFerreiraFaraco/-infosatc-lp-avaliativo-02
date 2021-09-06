Filmes = []
Jogos = []
Livros = []
Esportes = []

a1 = input("Digite um valor a ser inserido na lista filmes: ")
a2 = input("Digite um valor a ser inserido na lista filmes: ")
a3 = input("Digite um valor a ser inserido na lista jogos: ")
a4 = input("Digite um valor a ser inserido na lista jogos: ")
a5 = input("Digite um valor a ser inserido na lista livros: ")
a6 = input("Digite um valor a ser inserido na lista livros: ")
a7 = input("Digite um valor a ser inserido na lista esportes: ")
a8 = input("Digite um valor a ser inserido na lista esportes: ")

Filmes.insert(0,a1)
Filmes.insert(1,a2)
Jogos.insert(0,a3)
Jogos.append(a4)
Livros.insert(0,a5)
Livros.insert(1,a6)
Esportes.insert(0,a7)
Esportes.insert(1,a8)

listas = Filmes + Jogos + Livros + Esportes
print(listas)

mostrar = Livros.pop(1)
print(mostrar)

del Esportes[0]
print(Esportes)

disciplinas = []
listas = Filmes + Jogos + Livros + Esportes + disciplinas
print(listas)