# coding: utf-8

import numpy as np

def jogada(tabuleiro, jogador, x, y):

	tabuleiro[x][y] = jogador
	return tabuleiro

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
	else:
		return 0 #empate ou nenhum vencedor ainda

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

def main():

	t = np.zeros([3, 3], dtype=int) #Cria o tabuleiro 3x3: 'X' = 1 MAX; 'O' = -1 MIN; 0 = Espaço vazio
	nivel = 8 #nível máximo da árvore

	while(0 in t): 					#enquanto houver espaço em branco no tabuleiro:
		
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

		valor, t = miniMax(t.copy(), nivel, -1)
		nivel = nivel - 1

		print(t)
		if(vitoria(t) == -1):
			print('Computador venceu')
			break



main()