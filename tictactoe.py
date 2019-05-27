# coding: utf-8

import numpy as np

class Nodo:
	def __init__(self, tabuleiro, nivel, pai):
		self.tab = tabuleiro
		self.pai = None #vetor de nodos filhos
		self.valor = 0 #valor do minimax
		self.nivel = nivel

def jogada(tabuleiro, jogador, x, y):

	tabuleiro[x][y] = jogador
	return tabuleiro

def abreNodo(arvore, nodo, jogador):

	x = 0
	y = 0

	while(x <= 2):
		while(y <= 2):
			if(nodo.tab[x][y] == 0):
				arvore.append(Nodo(jogada(nodo.tab.copy(), jogador, x, y), nodo.nivel+1, nodo))
			y = y + 1
		x = x + 1
		y = 0

def geraArvore(raiz):

#	nivel = raiz.nivel
	i = 0
	arvore = []
	arvore.append(raiz)
	nodoAtual = arvore[0]

	while(arvore[i].nivel < 8): #Nível máximo = 8
		if(arvore[i].nivel % 2 == 0): #JOGADOR
			abreNodo(arvore, arvore[i], 1)
		else: #COMPUTADOR
			abreNodo(arvore, arvore[i], -1)
		i = i + 1

	return arvore

def vitoria(tabuleiro):

	if(tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]): #linha superior
		return tabuleiro[0][0]
	if(tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]): #linha do meio
		return tabuleiro[1][0]
	if(tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]): #linha inferior
		return tabuleiro[2][0]
	if(tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]): #coluna esquerda
		return tabuleiro[0][0]
	if(tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]): #coluna do meio
		return tabuleiro[0][1]
	if(tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]): #coluna da direita
		return tabuleiro[0][2]
	if(tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]): #diagonal esquerda
		return tabuleiro[0][0]
	if(tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]): #diagonal direita
		return tabuleiro[0][2]
	return 0 #empate ou nenhum vencedor ainda

def main():

	t = np.zeros([3, 3], dtype=int) #Cria o tabuliro 3x3: 'X' = 1 MAX; 'O' = -1 MIN; 0 = Espaço vazio
	a = [] #Árvore
	nivel = 0

	#Primeira jogada:
	while(vitoria(t) == 0): #enquanto nenhum vencer, faz jogada e gera jogada do computador
		#Jogador:
		x = int(input("x = "))
		y = int(input("y = "))
		jogada(t, 1, x, y)
		print(t)

		if(vitoria(t) != 0):
			print('oi')
			break

		#Computador:
		raiz = Nodo(t.copy(), nivel, None)
		a = geraArvore(raiz)
		nivel = nivel + 2
		a.clear() #limpa a árvore pra construir de novo
	#for i in range(len(vetorNodos)):
	#	print (vetorNodos[i].tab)

main()