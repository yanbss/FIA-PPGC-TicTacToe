# coding: utf-8

import numpy as np

'''
class Nodo:
	def __init__(self, tabuleiro, nivel, pai):
		self.tab = tabuleiro
		self.pai = pai #nodo pai
		self.valor = 0 #valor do MiniMax
		self.nivel = nivel
'''

def jogada(tabuleiro, jogador, x, y):

	tabuleiro[x][y] = jogador
	return tabuleiro

'''
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

'''

def abreTabuleiro(tabuleiro, jogador):

	x = 0
	y = 0
	filhos = []

	while(x <= 2):
		while(y <= 2):
			if(tabuleiro[x][y] == 0):
				filhos.append(jogada(tabuleiro.copy(), jogador, x, y))
			y = y + 1
		x = x + 1
		y = 0

	return filhos

'''
def geraArvore(raiz):

	i = 0
	arvore = []
	arvore.append(raiz)
	nodoAtual = arvore[0]

	while(arvore[i].nivel < 8): #Nível máximo = 8
		if(vitoria(arvore[i].tab) == 0): #Se não for um tabuleiro com um vencedor
			if(arvore[i].nivel % 2 == 0): #JOGADOR
				abreNodo(arvore, arvore[i], 1)
			else: #COMPUTADOR
				abreNodo(arvore, arvore[i], -1)
		i = i + 1

	return arvore
'''

'''
def miniMax(arvore):

	i = len(arvore)-1

	while(i > 0): #percorre o vetor de trás pra frente pra botar os valores
		arvore[i].pai.valor = arvore[i].pai.valor + arvore[i].valor
		i = i - 1

	i = 1
	escolhido = arvore[i]
	while(i < len(arvore)): #seleciona entre os filhos do tabuleiro atual qual o com maior chance de vitória para o computador
		if((arvore[i].nivel == (arvore[0].nivel + 1)) and (arvore[i].valor < escolhido.valor)):
			print(arvore[i].valor)
			escolhido = arvore[i]
		i = i + 1

	return escolhido.tab
'''

def miniMax(tabuleiro, nivel, jogador): #MIN = JOGADOR MAX = COMPUTADOR

	filhos = []

	if(vitoria(tabuleiro) != 0 or nivel == 0): #SE nó é um nó terminal OU profundidade = 0 ENTÃO
		return vitoria(tabuleiro), tabuleiro   #RETORNE o valor da heurística do nó

	elif(jogador == 1): 					   #SENÃO SE maximizador é FALSE ENTÃO
		minimo = 99							   #α ← +∞
		escolhido = None
		filhos = abreTabuleiro(tabuleiro, jogador)
		for filho in filhos:				   #PARA CADA filho DE nó
			var, tab = miniMax(filho, nivel-1, -1)
			if(var < minimo):
				minimo = var   				   #α ← min(α, minimax(filho, profundidade-1,true))
				escolhido = filho
		return minimo, escolhido  		   	   #RETORNE α

	else:									   #SENÃO //Maximizador
		maximo = -99						   #α ← -∞
		escolhido = None
		filhos = abreTabuleiro(tabuleiro, jogador)
		for filho in filhos:				   #PARA CADA filho DE nó
			var, tab = miniMax(filho, nivel-1, 1)   
			if(var > maximo):
				maximo = var 				   #α ← max(α, minimax(filho, profundidade-1,false))
				escolhido = filho
		return maximo, escolhido


def vitoria(tabuleiro):

	if(tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != 0): #linha superior
		return tabuleiro[0][0]

	elif(tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != 0): #linha do meio
		return tabuleiro[1][0]

	elif(tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != 0): #linha inferior
		return tabuleiro[2][0]

	elif(tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != 0): #coluna esquerda
		return tabuleiro[0][0]

	elif(tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != 0): #coluna do meio
		return tabuleiro[0][1]

	elif(tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != 0): #coluna da direita
		return tabuleiro[0][2]

	elif(tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0): #diagonal esquerda
		return tabuleiro[0][0]

	elif(tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0): #diagonal direita
		return tabuleiro[0][2]

	return 0 #empate ou nenhum vencedor ainda

def main():

	t = np.zeros([3, 3], dtype=int) #Cria o tabuleiro 3x3: 'X' = 1 MAX; 'O' = -1 MIN; 0 = Espaço vazio
	#a = [] #Árvore
	nivel = 8

	#Primeira jogada:
	while(vitoria(t) == 0): #enquanto nenhum vencer, faz jogada e gera jogada do computador
		#Jogador:
		x = int(input("x = "))
		y = int(input("y = "))
		t = jogada(t, 1, x, y)
		print(t)

		#Se jogador já ganhou, não faz jogada do computador
		if(vitoria(t) == 1):
			print('Jogador venceu')
			break

		#Computador:
		#raiz = Nodo(t.copy(), nivel, None)
		#a = geraArvore(raiz)
		valor, t = miniMax(t.copy(), nivel, -1)
		nivel = nivel - 1
		#jogada(t, -1, x, y)
		#nivel = nivel + 2
		print(t)
		if(vitoria(t) == -1):
			print('Computador venceu')
			break
		#a.clear() #limpa a árvore pra construir de novo



main()