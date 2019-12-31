class Carta(object):
	valor, naipe = "", ""
	def __init__(self, valor, naipe):
		self.valor = valor
		self.naipe = naipe
		
	def __str__(self):
		return self.valor + "[" + self.naipe + "]"
		
	def __repr__(self):
		return self.valor + "[" + self.naipe + "]"


class Jogo(object):
	def __init__(self, rodada_pontos, ultimo_comando, sair, primeira_mao, next_round, embaralhar):
		self.rodada_pontos  = rodada_pontos
		self.ultimo_comando = ultimo_comando
		self.sair           = sair 
		self.primeira_mao   = primeira_mao
		self.next_round     = next_round
		self.embaralhar     = embaralhar
		self.carta_mesa     = -1
		self.rodada_atual   = 1
		self.daCarta        = 1

  
class Player(object):
	def __init__(self, nome, pontos, carta1, carta2, carta3, ident):
		self.nome   = nome
		self.pontos = pontos
		self.carta1 = carta1
		self.carta2 = carta2
		self.carta3 = carta3
		self.ident  = ident

import random
import sys
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def diff():
	if player1.pontos > player2.pontos:
		rdiff = player1.pontos - player2.pontos
	else:
		rdiff = player2.pontos - player1.pontos
	if len(str(rdiff)) == 1:
		return "0" + str(rdiff)
	else:
		return str(rdiff)
	

def bem_vindo():
	print ("Bem vindo ao PYTRUCO!!!")
	print ("Caso algum dos jogadores nao conheca o jogo segue o link com instrucoes ")
	
def help_truco():
	print ("Cartas disponiveis no baralho: A, 2, 3, 4, 5, 6, 7, Q, J e K")
	print ("Naipes disponiveis: * (Paus), S2 (Copas), I (Espadas), ^ (Ouros)")
	print ("Comandos: TRUCO, SEIS, NOVE, DOZE, CORRER, ACEITO, DESISTO, PLACAR, AJUDA e CLEAR")
	print ("A selecao de cartas deve ser feita a partir da posicao da carta em sua mao, ou seja, Digitar 1, 2 ou 3.")
	
def remover_carta(indice, player):
	if indice == 1:
		if player.ident == 1:
			player1.carta1 = -1
		else:
			player2.carta1 = -1
	elif indice == 2:
		if player.ident == 1:
			player1.carta2 = -1
		else:
			player2.carta2 = -1
	elif indice == 3:
		if player.ident == 1:
			player1.carta3 = -1
		else:
			player2.carta3 = -1

def copy_cartausada(indice, player):
	if indice == 1:
		jogo.carta_mesa = player.carta1
	elif indice == 2:
		jogo.carta_mesa = player.carta2
	elif indice == 3:
		jogo.carta_mesa = player.carta3

def iniciar_baralho(naipe):
	carta = Carta("A", naipe)
	baralho.append(carta)
	for i in range(2, 8):
		carta = Carta(str(i), naipe)
		baralho.append(carta)
	carta = Carta("Q", naipe)
	baralho.append(carta)
	carta = Carta("J", naipe)
	baralho.append(carta)
	carta = Carta("K", naipe)
	baralho.append(carta)
	
def carta_usada(carta):
	if carta in cartas_usadas:
		return True
	else:
		return False
	
def manilha(vira):
	if vira.valor == 'A':
		return '2'	
	elif vira.valor == '7':
		return 'Q'
	elif vira.valor == 'Q':
		return 'J'
	elif vira.valor == 'J':
		return 'K'
	elif vira.valor == 'K':
		return 'A'
	else:
		valor = int(vira.valor) + 1
		return str(valor)
		
def maior_naipe(naipe1, naipe2):
	if naipe1 == '*':
		return 1
	elif naipe2 == '*':
		return 2
	elif naipe1 == 'S2':
		return 1
	elif naipe2 == 'S2':
		return 2
	elif naipe1 == 'I':
		return 1
	elif naipe2 == 'I':
		return 2
	else:
		print ("putz, se entrou aqui deu muito ruim.")
		return -1

def maior_valor_carta(valor1, valor2):
	if ordem_forca[valor1] > ordem_forca[valor2]:
		return 1
	elif ordem_forca[valor1] < ordem_forca[valor2]:
		return 2
	else:
		return -1
		
def bora_jogar():
	if jogo.daCarta == 1:
		jogar(player1)
		jogar(player2)
	else:
		jogar(player2)
		jogar(player1)
		
def win_player1():
	jogo.daCarta = 1
	if jogo.rodada_atual == 1:
		jogo.primeira_mao = 1
		jogo.rodada_atual = 2
		bora_jogar()
	elif jogo.rodada_atual == 2:
		if jogo.primeira_mao == 1:
			player1.pontos += jogo.rodada_pontos
			jogo.rodada_pontos = 1
			jogo.rodada_atual = 1	
		elif jogo.primeira_mao == 2:
			jogo.rodada_atual = 3
			bora_jogar()	
		else:
			player1.pontos += jogo.rodada_pontos
			jogo.rodada_pontos = 1
			jogo.rodada_atual = 1
	else:
		player1.pontos += jogo.rodada_pontos
		jogo.rodada_pontos = 1
		jogo.rodada_atual = 1

def maior_carta(carta1, carta2, vira):
	maior = manilha(vira)
	if (carta1.valor == maior) and (carta2.valor == maior):
		if maior_naipe(carta1.naipe, carta2.naipe) == 1:
			win_player1()
		else:
			if jogo.rodada_atual == 1:
				jogo.primeira_mao = 2
				jogo.rodada_atual = 2
				jogo.daCarta = 2
				bora_jogar()
			elif jogo.rodada_atual == 2:
				if jogo.primeira_mao == 2:
					player2.pontos += jogo.rodada_pontos
					jogo.rodada_pontos = 1
					jogo.rodada_atual = 1	
				elif jogo.primeira_mao == 1:
					jogo.rodada_atual = 3
					jogo.daCarta = 2
					bora_jogar()
				else:
					player2.pontos += jogo.rodada_pontos
					jogo.rodada_pontos = 1
					jogo.rodada_atual = 1						
			else:
				player2.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.rodada_atual = 1
	elif (carta1.valor == maior):
		if jogo.rodada_atual == 1:
			jogo.primeira_mao = 1
			jogo.rodada_atual = 2
			jogo.daCarta = 1
			bora_jogar()
		elif jogo.rodada_atual == 2:
			if jogo.primeira_mao == 1:
				player1.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.rodada_atual = 1	
			elif jogo.primeira_mao == 2:
				jogo.rodada_atual = 3
				jogo.daCarta = 1
				bora_jogar()
			else:
				player1.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.rodada_atual = 1
		else:
			player1.pontos += jogo.rodada_pontos
			jogo.rodada_pontos = 1
			jogo.rodada_atual = 1
	elif (carta2.valor == maior):
		if jogo.rodada_atual == 1:
				jogo.primeira_mao = 2
				jogo.rodada_atual = 2
				jogo.daCarta = 2
				bora_jogar()
		elif jogo.rodada_atual == 2:
			if jogo.primeira_mao == 2:
				player2.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.rodada_atual = 1	
			elif jogo.primeira_mao == 1:
				jogo.rodada_atual = 3
				jogo.daCarta = 2
				bora_jogar()
			else:
				player2.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.rodada_atual = 1
		else:
			player2.pontos += jogo.rodada_pontos
			jogo.rodada_pontos = 1
			jogo.rodada_atual = 1
	else:
		maior_valor = maior_valor_carta(carta1.valor, carta2.valor)
		if maior_valor == 1:
			win_player1()
		elif maior_valor == 2:
			if jogo.rodada_atual == 1:
				jogo.primeira_mao = 2
				jogo.rodada_atual = 2
				jogo.daCarta = 2
				bora_jogar()
			elif jogo.rodada_atual == 2:
				if jogo.primeira_mao == 2:
					player2.pontos += jogo.rodada_pontos
					jogo.rodada_pontos = 1
					jogo.rodada_atual = 1	
				elif jogo.primeira_mao == 1:
					jogo.rodada_atual = 3
					jogo.daCarta = 2
					bora_jogar()
				else:
					player2.pontos += jogo.rodada_pontos
					jogo.rodada_pontos = 1
					jogo.rodada_atual = 1
			else:
				player2.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.rodada_atual = 1
		else:
			if jogo.rodada_atual == 1:
				jogo.primeira_mao = -1
				jogo.rodada_atual = 2
				jogo.daCarta = 1
				bora_jogar()
			elif jogo.rodada_atual == 2:
				if jogo.primeira_mao == -1:
					jogo.rodada_atual = 3
					jogo.daCarta = 1
					bora_jogar()
				elif jogo.primeira_mao == 1:
					player1.pontos += jogo.rodada_pontos
					jogo.rodada_pontos = 1
					jogo.primeira_mao = -1
					jogo.rodada_atual = 1
				else:
					player2.pontos += jogo.rodada_pontos
					jogo.rodada_pontos = 1
					jogo.primeira_mao = -1
					jogo.rodada_atual = 1
			else:
				if jogo.primeira_mao == -1:
					print ("mano, pqp nao pensei em nada aqui!!!!!!!!!!!")
				elif jogo.primeira_mao == 1:
					player1.pontos += jogo.rodada_pontos
				else:
					player2.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
				jogo.primeira_mao  = -1
				jogo.rodada_atual  = 1
	
def gera_carta():
	num_random = random.randint(0,39)
	while carta_usada(num_random):
		num_random = random.randint(0,39)
	cartas_usadas.append(num_random)
	return num_random
	
def dar_cartas(player):
	player.carta1 = gera_carta()
	player.carta2 = gera_carta()
	player.carta3 = gera_carta()
	
def retorna_carta(indice):
	if indice != -1:
		return baralho[indice]
	else:
		return "X[x]"
	
def jogar(player):
	if not jogo.sair:
		print ("E a vez do jogador " + player.nome + " realizar sua jogada.")
		print ("A vira do jogo e:", vira(
		print ("Voce possui as seguintes cartas:", retorna_carta(player.carta1) , retorna_carta(player.carta2), retorna_carta(player.carta3))
               
			

def executar_comando(comando, player):
	print
	if comando == "TRUCO":
		if not jogo.ultimo_comando in ["TRUCO","SEIS","NOVE","DOZE","ACEITO","ACEITO","CORRER"]:	
			jogo.embaralhar = False
			print "O player ", player.nome, "esta solicitando TRUCO, deseja aceitar?"
			jogo.ultimo_comando = comando
			return True
		else:
			print ("Comando nao aceitado pois o ultimo comando executado foi", jogo.ultimo_comando)
			return False
	elif comando == "SEIS":
		if jogo.ultimo_comando == "TRUCO":
			jogo.rodada_pontos = 3
			jogo.embaralhar = False
			print "O player ", player.nome, "esta solicitando SEIS, deseja aceitar?"
			jogo.ultimo_comando = comando
			return True
		else:
			print "Comando nao aceitado pois o ultimo comando executado foi", jogo.ultimo_comando
			return False
	elif comando == "NOVE":
		if jogo.ultimo_comando == "SEIS":
			jogo.rodada_pontos = 6
			jogo.embaralhar = False
			print "O player ", player.nome, "esta solicitando NOVE, deseja aceitar?"
			jogo.ultimo_comando = comando
			return True
		else:
			print "Comando nao aceitado pois o ultimo comando executado foi", jogo.ultimo_comando
			return False
	elif comando == "DOZE":
		if jogo.ultimo_comando == "NOVE":
			jogo.rodada_pontos = 9
			jogo.embaralhar = False
			print "O player ", player.nome, "esta solicitando DOZE, deseja aceitar?"
			jogo.ultimo_comando = comando
			return True
		else:
			print "Comando nao aceitado pois o ultimo comando executado foi", jogo.ultimo_comando
			return False
	elif comando == "CORRER":
		if jogo.ultimo_comando in ["TRUCO","SEIS","NOVE","DOZE"]:
			jogo.embaralhar = True
			jogo.next_round = True
			jogo.ultimo_comando = comando
			if player.ident == 1:
				player2.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
			else:
				player1.pontos += jogo.rodada_pontos
				jogo.rodada_pontos = 1
			return True
		else:
			print "Comando nao aceitado pois o ultimo comando executado foi", jogo.ultimo_comando
	elif comando == "ACEITO":
		jogo.embaralhar = False
		if jogo.ultimo_comando == "TRUCO":
			jogo.rodada_pontos = 3
			print "Rodada esta valendo 3 PONTOS!"
			jogo.ultimo_comando = comando
		elif jogo.ultimo_comando == "SEIS":
			jogo.rodada_pontos = 6
			print "Rodada esta valendo 6 PONTOS!"
			jogo.ultimo_comando = comando
		elif jogo.ultimo_comando == "NOVE":
			jogo.rodada_pontos = 9
			print "Rodada esta valendo 9 PONTOS!"	
			jogo.ultimo_comando = comando
		elif jogo.ultimo_comando == "DOZE":
			jogo.rodada_pontos = 12
			print "Rodada esta valendo 12 PONTOS!"	
			jogo.ultimo_comando = comando
		else:
			print "Comando nao aceitado pois o ultimo comando executado foi", jogo.ultimo_comando
			return False
		if jogo.daCarta == 1:
			if player.ident == 1:
				if jogo.carta_mesa != -1:
					return True
				return False
			else:
				return True
		else:
			if player.ident == 1:
				return True
			else:
				if jogo.carta_mesa != -1:
					return True
				return False
	elif comando == "DESISTO":
		if player.ident == 1:
			print "Vitoria do Player:", player2.nome
			player2.pontos += 12
		else:
			print "Vitoria do Player:", player1.nome
			player1.pontos += 12
		jogo.sair = True
		return True
	elif comando == "AJUDA":
		help_truco()
		return False
	elif comando == "CLEAR":
		cls()
		return False
	elif comando == "PLACAR":
		print "Placar do jogo:", player1.nome, str(player1.pontos), "x", player2.nome, str(player2.pontos)
		return False
	elif comando in ["1","2","3"]:
		jogo.embaralhar = True
		jogo.ultimo_comando = comando
		if pode_escolher(comando, player):
			if jogo.daCarta == 1:
				if player.ident == 1:
					copy_cartausada(int(comando), player)
					remover_carta(int(comando), player1)
				elif player.ident == 2:
					if comando == "1":
						carta_temp = player.carta1
					elif comando == "2":
						carta_temp = player.carta2
					elif comando == "3":
						carta_temp = player.carta3
					remover_carta(int(comando), player)
					maior_carta(baralho[jogo.carta_mesa], baralho[carta_temp], vira)
			else:				
				if player.ident == 2:
					copy_cartausada(int(comando), player)
					remover_carta(int(comando), player)
				elif player.ident == 1:
					if comando == "1":
						carta_temp = player.carta1
					elif comando == "2":
						carta_temp = player.carta2
					elif comando == "3":
						carta_temp = player.carta3
					remover_carta(int(comando), player)
					maior_carta(baralho[carta_temp], baralho[jogo.carta_mesa], vira)
			return True
		else:
			return False
	else:
		print "Comando nao reconhecido, caso necessario utilize o comando: AJUDA"

def pode_escolher(indice, player):
	if indice == "1":
		if player.carta1 == -1:
			return False
	elif indice == "2":
		if player.carta2 == -1:
			return False
	elif indice == "3":
		if player.carta3 == -1:
			return False
	return True
	
def exibir_ranking(arquivo, vinte):
	try:
		if vinte:
			print "============ Ranking dos 20 Melhores Truco-PY ============"
		else:
			print "============ Ranking do Truco-PY ============"
		farquivo = open(arquivo, 'r')
		for line in farquivo:
			arquivo_memoria.append(line)
		farquivo.close()
		arquivo_memoria.sort(reverse = True)
		count = 1
		for i in arquivo_memoria:
			if count <= 20 or not vinte:
				print i.replace("\n", "")
			count+=1
		print
		print
	except (RuntimeError, TypeError, NameError, IOError):
		print "Arquivo nao encontrado ou sem direito de leitura/escrita."
		print "Verifique os itens e tente novamente."
		exit()

if len(sys.argv) != 2:
	print "Eh obrigatorio passar apenas 1 arquivo por parametro."
	exit()
else:
	arquivo_txt = sys.argv[1]
	if arquivo_txt[-4:] != ".txt":
		print "Eh obrigatorio passar um arquivo com a extensao .txt!"
		exit()
		
arquivo_memoria = []
exibir_ranking(arquivo_txt, False)

bem_vindo()
print
help_truco()

#Ordem forca
ordem_forca = { 	
	"4" : 1,
	"5" : 2,
	"6" : 3,
	"7" : 4,
	"Q" : 5,
	"J" : 6,
	"K" : 7,
	"A" : 8,
	"2" : 9,
	"3" : 10
}

#Vira da jogo.
vira = Carta("-1", "-1")

#Baralho do jogo, com objetos do tipo CARTA.
baralho = []

#Cartas utilizadas na rodada.
cartas_usadas = []

jogo = Jogo(1, "", False, -1, False, True)

#Dois jogadores.
player1 = Player(raw_input("Informe seu nome Player 1: "), 0, -1, -1, -1, 1)
player2 = Player(raw_input("Informe seu nome Player 2: "), 0, -1, -1, -1, 2)

print
print
print "Embaralhando as cartas."
print

#Iniciando o baralho com os 4 naipes.
iniciar_baralho("*")   # PAUS - ZAP
iniciar_baralho("S2")  # Copas
iniciar_baralho("I")   # Espadas
iniciar_baralho("^")   # Ouros

#print baralho
while (not jogo.sair) or (player1.pontos >= 12) or (player2.pontos >= 12):
	if (player1.pontos >= 12) or (player2.pontos >= 12):
		break
	if jogo.embaralhar:
		random.seed(int(raw_input("Informe o Seed do embaralhamento:")))
		num_random = random.randint(0,39)
		vira = baralho[num_random]
		cartas_usadas.append(num_random)
		dar_cartas(player1)
		dar_cartas(player2)
		jogo.carta_mesa = -1
		jogo.ultimo_comando = ""
	if jogo.daCarta == 1:
		jogar(player1)
		if jogo.next_round:
			jogo.next_round = False
			continue
		if (player1.pontos >= 12) or (player2.pontos >= 12):
			break
		jogar(player2)
	else:
		jogar(player2)
		if jogo.next_round:
			jogo.next_round = False
			continue
		if (player1.pontos >= 12) or (player2.pontos >= 12):
			break
		jogar(player1)
	cartas_usadas = []
	if (player1.pontos >= 12) or (player2.pontos >= 12):
		break

print "Placar final do jogo:", player1.nome, str(player1.pontos), "x", player2.nome, str(player2.pontos)

arquivo_final = open(arquivo_txt, 'a')

arquivo_final.writelines(diff() + " foi a diferenca entre " + player1.nome + " " + str(player1.pontos) + "x" + str(player2.pontos) + " " + player2.nome + "\n")

arquivo_final.close()

exibir_ranking(arquivo_txt, True) #Vinte melhores
	    

