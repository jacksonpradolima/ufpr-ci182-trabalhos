from Chatbot import Chatbot

Bot = Chatbot("usuarios")
k=0

frase = Bot.escuta(k)

num_jogadores,resp1,jogador1,resp2,jogador2 = Bot.pensa(frase)

while resp1 == "\nNão entendi!\n":
	Bot.fala(resp1)
	frase = Bot.escuta(k)
	num_jogadores,resp1,jogador1,resp2,jogador2 = Bot.pensa(frase)

k=1

while num_jogadores == 0:
	
	if resp1 == "\n\t\t\tTchauzinho, até a próxima!":
		break
	else:
		Bot.fala(resp1)
		frase = Bot.escuta(k)
		num_jogadores,resp1,Jogador1,resp2,Jogador2 = Bot.pensa(frase)

if resp1 != "\n\t\t\tTchauzinho, até a próxima!" :
	
	if num_jogadores == 1:
		Bot.fala(resp1)
		Resp = Bot.pensa(frase)
		Bot.fala(Resp)
		frase_final = Bot.Quiz(num_jogadores,Jogador1,0)

	elif num_jogadores == 2:
		Bot.fala(resp1+"\n"+resp2)
		Resp = Bot.pensa(frase)
		Bot.fala(Resp)
		frase_final = Bot.Quiz(num_jogadores,Jogador1,Jogador2)
	
	if "\t\tParabéns!! Você está acima da média " in frase_final:
		Bot.fala(frase_final)
		frase = Bot.escuta(k)
		resp = Bot.pensa(frase)
		
		if resp == "Muito bem! Digite a nova pergunta:":
			Bot.fala(resp)
			frase = "Nova_Quest"
			resposta_add = Bot.pensa(frase)
			Bot.fala(resposta_add)
			frase = "tchau"
			a,despede,b,c,d = Bot.pensa(frase)
			Bot.fala(despede)
		else:
			Bot.fala(resp)
	elif "empate" in frase_final:
		frase = "tchau"
		a,despede,b,c,d = Bot.pensa(frase)
		Bot.fala(despede)

	else:
		Bot.fala(frase_final)
		frase = "tchau"
		a,despede,b,c,d = Bot.pensa(frase)
		Bot.fala(despede)	

else:
	Bot.fala(resp1)
