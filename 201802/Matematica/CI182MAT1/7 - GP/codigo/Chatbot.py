import json
import random

class Chatbot():
	def __init__(self, nome):
		try:
			memoria = open(nome+".json","r", encoding="utf-8")      #tenta abrir o arquivo de reconhecimento dos usuarios 
		except FileNotFoundError:
			memoria = open(nome+".json","w", encoding="utf-8")					#caso n encontre o arquivo o programa mesmo cria
			memoria.write('["Vininhogp","Tabordinhagp","Carolzinhagp","Bianquinhagp"]')		#com uma lista predeterminada de usuarios

			memoria.close()
			memoria.open("usuarios.json","r", encoding="utf-8")

		with open("perguntas.json","r", encoding="utf-8") as t:			#abre o arquivo de perguntas e transforma em lista dentro 
			self.perguntas = json.load(t)								#do código
		
		with open("respostas.json","r", encoding="utf-8") as f:			#abre o arquivo de resspostas e transforma em lista dentro
			self.respostas = json.load(f)								#do código

		self.usuarios= nome 											#transforma em lista os usuarios conhecids pelo programa
		self.conhecidos = json.load(memoria)
		self.historico = []												#lista pra guardar todas as mensagens q são impressas na 
																		#tela 

		self.frases = {"/start" : "\nVamos jogar ? [S/N] ", "tchau":"\n\t\t\tTchauzinho, até a próxima!"} #frases q o programa reconhece

	def Quiz(self,num_jogadores,jogador1,jogador2):
		
		frase1 = "\n\t\t\t!!RESPOSTA CORRETA!!\n\t\tParabéns {0},você agora têm {1} acerto(s)."
		frase2 = "\n\t\t\t!!RESPOSTA INCORRETA!!\n   Não desanime {0}, a próxima você vai acertar, você têm {1} acerto(s)."
		frase3 = "\n\t\t\t!!!QUIZ FINALIZADO!!!\n\t\t\tO VENCEDOR É {0}"
		frase4 = "\n\t\t\t!!!EMPATOU!!!\n\t\t...Se quiser descobrir quem sabe mais...\n\t\t\t!!JOGUE NOVAMENTE!!\n\t\t\t!!!QUIZ FINALIZADO!!!"

		randomizar =[]							 
		for k in range(len(self.perguntas)):	#e em seguita aleatoriza esse vetor
			randomizar.append(k)
		random.shuffle(randomizar)

		if num_jogadores == 1:								#SINGLE PLAYER:

			score_J1,resposta_J1 = 0,[]				#pontuação e uma lista com as respostas do usuário
			for b in range (10):									#laço de repetição com 10 perguntas	
				print("\n\t\t\t\tPergunta {0} \nTema:".format(b+1))	#informa o número da pergunta na tela 
				resposta = input (self.perguntas[randomizar[b]])	#imprime na tela uma pergunta aleatorizada e salva a resposta 
				resposta = resposta.lower()							#como caracter minusculo
				#validação da resposta para q seja uma das possíveis alternativas

				while resposta != "a" and resposta != "b" and resposta != "c":
					print("A alternativa escolhida não existe!! \nTente novamente. As alternativas possíveis são [A/B/C]:")
					resposta = input("> ")
					resposta = resposta.lower()
				resposta_J1.append(resposta)											
				
				if resposta_J1[-1] == self.respostas[randomizar[b]]:	
					score_J1+=1															
					print(frase1.format(jogador1,score_J1))								
				else:																	
					print(frase2.format(jogador1,score_J1))								
			print("\n\t\t\t!!!QUIZ FINALIZADO!!!")
			return"\t\tParabéns!! Você está acima da média {0}!! \n\t  Gostaria de adicionar uma nova pergunta ao jogo ? [S/N]".format(jogador1) if score_J1>= 7 else "\t\tOra Ora! Parece que seu desempenho não foi dos melhores!!\n\t  Se quiser adicionar uma nova pergunta ao jogo, tente novamente!! "
			

			#imprime na tela QUIZ FINALIZADO e entao se o score for maior do q 7 o usuario pode adicionar uma pergunta ao jogo

		else:																#MULTI PLAYER:
			score_J1,score_J2,resposta_J1,resposta_J2 = 0,0,[],[]			#funiona de maneira similar à de Single player exeto caso o jogo 
			for b in range(20):												#empate
				if (b)%2==0:
					print("\n{0} é a sua vez...\n\t\t\t\tPergunta {1} \nTema:".format(jogador1,b+1))
					resposta = input (self.perguntas[randomizar[b]].replace("@@","\n"))
					resposta = resposta.lower()
					resposta_J1.append(resposta)
					
					while resposta != "a" and resposta != "b" and resposta != "c":
						print("A alternativa escolhida não existe!! \nTente novamente. As alternativas possíveis são [A/B/C]:")
						resposta = input("> ")
						resposta = resposta.lower()
					
					resposta_J1.append(resposta)
					
					if resposta_J1[-1] == self.respostas[randomizar[b]]:
						score_J1+=1
						print(frase1.format(jogador1,score_J1))
					else:
						print(frase2.format(jogador1,score_J1))
				else:
					print("\n{0} é a sua vez...\n\t\t\t\tPergunta {1} \nTema:".format(jogador2,b+1))
					resposta = input (self.perguntas[randomizar[b]].replace("@@","\n"))
					resposta = resposta.lower()
					
					while resposta != "a" and resposta != "b" and resposta != "c":
						print("A alternativa escolhida não existe!! \nTente novamente. As alternativas possíveis são [A/B/C]:")
						resposta = input("> ")
						resposta = resposta.lower()					

					resposta_J2.append(resposta)
					if resposta_J2[-1] == self.respostas[randomizar[b]]:
						score_J2+=1
						print("\n"+frase1.format(jogador2,score_J2))
					else:
						print("\n"+frase2.format(jogador2,score_J2))
			media_score = (score_J2+score_J1)/2
			

			if score_J2 == score_J1:								
				print("\n"+frase4)									
				return "empate"													

			elif score_J1 > score_J2:
				print("\n"+frase3.format(jogador1.upper()))
				return("\t\tParabéns!! Você está acima da média {0}!!\n\t  Gostaria de adicionar uma nova pergunta ao jogo ? [S/N]".format(jogador1) if media_score >= 7 else "\t\tOra Ora! Parece que seu desempenho não foi dos melhores!!\n\t  Se quiser adicionar uma nova pergunta ao jogo, tente novamente!! ")
			else:				
				print("\n"+frase3.format(jogador2.upper()))
				return("\t\tParabéns!! Você está acima da média {0}!!\n\t  Gostaria de adicionar uma nova pergunta ao jogo ? [S/N]".format(jogador2) if media_score >= 7 else "\t\tOra Ora! Parece que seu desempenho não foi dos melhores!!\n\t  Se quiser adicionar uma nova pergunta ao jogo, tente novamente!! ")

																	# o jogador vencedor tera o direito de adicionar um nova pergunta
																	#compara os scores e define o vencedor da partida

			
			
	def pegaNome(self,usuarios):			# fun$ção q identifica o nome do jogador e retorna o mesmo
		usuarios = usuarios.lower().replace("é","eh",1)
		if "o meu nome eh " in usuarios :	# caso o nome tenha a sigla gp 
			usuarios = usuarios [14:]		# o programa entao arruma essa parte pra _GP
		if "meu nome eh " in usuarios:		# e coloca o nome com letra maiuscula
			usuarios = usuarios[12:]
		usuarios = usuarios.title()
		if "gp" in usuarios:
				usuarios = usuarios[:-2]
				usuarios = usuarios+"_GP"
		
		return(usuarios)

	def respondeNome(self,usuario):													
		if usuario in self.conhecidos:												
			if "_GP" in usuario:													
				usuario = usuario[:-3]
			usuario = usuario+"_GP"
			frase = "\n\t\tOlá novamente {0}. Que bom que voltou!".format(usuario)
			return(frase,usuario)		
		else:
			if "_GP" in usuario:
				usuario = usuario[:-3]
				usuario = usuario.title()+"_GP"
			frase = "\n\t\tMuito prazer em te conhecer {0}! ".format(usuario)
			self.conhecidos.append(usuario)
			with open(self.usuarios+".json","w") as memoria:
				json.dump(self.conhecidos, memoria)
			
			return(frase,usuario)
			

	def escuta(self,k):										# funçao responsavel por ouvir as respostas do usuario 
		
		x= "@"												#caso n haja nenhuma resposta ainda ela incializa o programa com a frase
		if k == 0:											# "Digite "/start" para iniciar !"
			self.historico.append(x)
			if "@" in self.historico[-1]:
				frase = input('Digite "/start" para iniciar !\n> ')
				frase = frase.lower()
				return(frase)
	
		else:												#caso exista ela apenas guarda a resposta do usuario qndo solicitado
			frase =	input("> ")
			frase.lower()
			return(frase)
	
	def pensa(self,frase):															
		if frase in self.frases:													
			return (0,self.frases[frase],0,0,0)

		elif "Vamos jogar ? [S/N]" in self.historico[-1]:
			while frase != "s" and frase != "n":
				print("\n\t\t\t!!!Opção Inválida!!!\n\t\t  !!As opções possíveis são [S/N]!!\n\t\t\t  !Tente novamente!")
				frase = input("\nVamos jogar ? [S/N] \n> ")
				frase = frase.lower()
			if frase == "s":
				num_jogadores = input("\nQuantidade de Jogadores: [1/2]\n> ")
				while num_jogadores != "1" and num_jogadores != "2":
					print("\n\t\t  !!Quantidade de jogadores inválida!!\n\t\t\t  !!Tente novamente!!\n")
					num_jogadores = input("Quantidade de Jogadores: [1/2]\n> ")
				num_jogadores = int(num_jogadores)
				if num_jogadores == 1:												#devolve o numero de jogadores e a saudação respectiva
					print("\n\t\t\t!!SINGLE PLAYER!!\n")
					jogador1=input("Olá Jogador, qual o seu nome ?\n> ")
					Jogador1 = self.pegaNome(jogador1)
					resp , Jogador1 = self.respondeNome(Jogador1)
					return(num_jogadores,resp,Jogador1,0,0)
					
				else :
					print("\n\t\t\t!!MULTI PLAYER!!\n")
					Jogador1=input("Olá Jogador 1, qual o seu nome ?\n> ")
					Jogador1 = self.pegaNome(Jogador1)
					resp1, Jogador1 = self.respondeNome(Jogador1)
					Jogador2=input("Olá Jogador 2, qual o seu nome ?\n> ")
					Jogador2 = self.pegaNome(Jogador2)
					resp2 , Jogador2 = self.respondeNome(Jogador2)
					return(num_jogadores,resp1,Jogador1,resp2,Jogador2)
			else:

				return (0,self.frases["tchau"],0,0,0)
			

		# apos a saudaçao incializa o quiz
		elif ("Muito prazer em te conhecer " in self.historico[-1] or "Que bom que voltou!" in self.historico[-1]):
			resp = "\n\t\t\t!!!INICIAR RESPONDIDOS!!!"
			return(resp)

		elif "Parabéns!! Você está acima da média" in self.historico[-1]: 
			if frase == "s":
				resp = ("Muito bem! Digite a nova pergunta:")
				return(resp)
			else:
				resp = self.frases["tchau"]
				return (resp)
		
		elif frase == "Nova_Quest": 
			quest = "(FAN_MADE)\n"
			pergunta = input("> ")+"\n"
			if "?" in pergunta or ":" in pergunta:
				pass
			else:
				pergunta = pergunta+" ?"

			alt_a ="A)"+input("Digite a alternativa A:\n> ")+"\n"
			alt_b ="B)"+input("Digite a alternativa B:\n> ")+"\n"
			alt_c ="C)"+input("Digite a alternativa C:\n> ")+"\n"

			resposta = input("Digite a alternativa que corresponde a nova pergunta:\n> ")	
			resposta = resposta.lower()
			while resposta != "a" and resposta != "b" and resposta != "c":
				print ("\n\t\t\t!!Resposta inválida!!")
				resposta = input("Digite a alternativa que corresponde a nova pergunta:\n> ")
				resposta = resposta.lower()
			
			quest = quest+pergunta+alt_a+alt_b+alt_c
			quest = "\n"+quest+">"
			
			self.perguntas.append(quest)									 
			with open("perguntas.json","w",encoding="utf-8") as perg:		
				json.dump(self.perguntas, perg)
	

			self.respostas.append(resposta)
			with open("respostas.json","w",encoding="utf-8") as resp:
				json.dump(self.respostas, resp)
			

			resposta = "\n\t\tSua Pergunta foi adicionada com sucesso!!"	 

			return (resposta)
		else:
			return (0,'\nNão entendi!\n',0,0,0)								# caso alguma msg n atenda o esperado
	
	def fala(self, frase):								# imprime na tela as respostas geradas em Chatbot.pensa() e guarda elas na lista 
		self.historico.append(frase)					# self.historico
		print(frase)
