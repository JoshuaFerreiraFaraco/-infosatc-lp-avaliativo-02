#Definiçao da lista e inputs para valores
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

#Definindo posiçao
Filmes.insert(0,a1)
Filmes.insert(1,a2)
Jogos.insert(0,a3)
Jogos.append(a4)
Livros.insert(0,a5)
Livros.insert(1,a6)
Esportes.insert(0,a7)
Esportes.insert(1,a8)

#Lista que vai receber as outras listas
listas = Filmes + Jogos + Livros + Esportes
print(listas)

#Mostrando o valor da lista Livros na posiçao 1
mostrar = Livros.pop(1)
print(mostrar)

#Deletando o valor da lista Esportes na posiçao 0
del Esportes[0]
print(Esportes)

#Adicionando mais uma lista na lista geral
disciplinas = []
listas = Filmes + Jogos + Livros + Esportes + disciplinas
print(listas)