import telebot                      #pip install pyTelegramBotAPI (Módulo do bot usado)
from telebot import types  # função para o teclado
import datetime, threading, time, sched  # funções usadas para os lembretes
import funcoes 

# Token para o bot (obtida pelo BotFather)
token = '661545941:AAFGeT9-HdTrligeFC192HYNDoFUUz-xPfw'

# Caso o arquivo 'usuarios' não exista, é criado um, e cada usuário que usou o bot é salvo na última linha desse arquivo chamado usuarios.txt; Caso o usuário seja novo, ele é colocado na última linha.
usuariosConhecidos = []
try:
	with open('usuarios.txt', 'r') as users:
		for linha in users:
			usuariosConhecidos.append(int(linha[:-1]))
except FileNotFoundError:
	f = open('usuarios.txt', 'x')
	f.close()

# Os envios dos lembretes são salvos em um dicionário para cada usuário, caso (mais para frente) o usuário queira cancelar
lembretes = {}
for cid in usuariosConhecidos:
	lembretes[cid] = {}

# O passo que cada usuário está, é salvo em um arquivo de texto na pasta 'passo' com o nome 'id.txt', onde 'id' é o id do usuário.
passoUsuario = {}
for cid in usuariosConhecidos:
	try:
		with open('passo/{}.txt'.format(cid), 'r') as f:
			passoUsuario[cid] = int(f.readline())
	except FileNotFoundError:
		f = open('passo/{}.txt'.format(cid), 'w')
		f.write("0")
		f.close()
		passoUsuario[cid] = 0

# Lê as informações (são as informações fornecidas pelo usuário ao criar o evento) temporárias salvas na pasta 'linhatemp' com o nome 'id.txt' e salva no dicionário 'linhatemp'.
linhatemp = {} 
temp = ["titulo", "data", "detalhes", "casolembrete"]
for user in usuariosConhecidos:
	try:
		f = open('linhatemp/{}.txt'.format(user), 'r')
		linhas = f.readlines()
		for i in range(len(linhas)):
			if '\n' in linhas[i]:
				linhas[i] = linhas[i][:-1]
			if i == 1:
				linhatemp[str(user)+temp[i]] = funcoes.texto_para_datetime(linhas[i])
			if i == 3:
				linhatemp[str(user)+temp[i]] = int(linhas[i])
			else:
				linhatemp[str(user)+temp[i]] = linhas[i]
	except FileNotFoundError:
		f = open('linhatemp/{}.txt'.format(user), 'x')
		f.close()

# Lê os eventos salvos em arquivos de texto para cada usuário e colocá-os em uma matriz no dicionário 'evento' na chave 'id'. As datas salvas em formato de texto são convertidas para datetime e a matriz é organizada.
eventos = {}
for user in usuariosConhecidos:
	try:
		f = open('eventos/{}.txt'.format(user), 'r')
		eventos[user] = []
		lista = f.readlines()
		for i in range(len(lista)):
			lista[i] = lista[i][:-1]
		for i in range(0, len(lista), 4):
			eventos[user].append(lista[i:i+4])		
		f.close()
	except FileNotFoundError:
		f = open('eventos/{}.txt'.format(user), 'x')
		eventos[user] = []
		f.close()

for user in usuariosConhecidos:
	for i in range(len(eventos[user])):
		if eventos[user][i][-1] != "0":
			eventos[user][i][-1] = funcoes.texto_para_datetime(eventos[user][i][-1])
		else:
			eventos[user][i][-1] = 0
		eventos[user][i][1] = funcoes.texto_para_datetime(eventos[user][i][1])

for cid in usuariosConhecidos:
	for k in range(len(eventos[cid])):
		for i in range(1, len(eventos[cid]) - k):
			if eventos[cid][i][1] < eventos[cid][i-1][1]:
				eventos[cid][i], eventos[cid][i-1] = eventos[cid][i-1], eventos[cid][i]

# Criação de teclados	
comandos = ['Adicionar evento', 'Lista de eventos'] 
selecionarComando = types.ReplyKeyboardMarkup()
selecionarComando.add(*comandos)

sim_ou_não = types.ReplyKeyboardMarkup()
sim_ou_não.add('SIM', 'NÃO')
 

cancelar = types.ReplyKeyboardMarkup()
cancelar.add('CANCELAR')

# Esconde o teclado
esconderTeclado = types.ReplyKeyboardRemove()

# Essa função serve só para evitar erros que aconteceriam se tentasse ler o passo de um usuário que não está no dicionário.
def passo_do_usuario(uid):
	# Recebe o id do usuário, retorna o passo em que ele está. Se o usuário não estiver na lista de usuário conhecidos e se o passo é colocado em 0, são criados arquivos, dicionários e lista necessários.
	if uid in passoUsuario:
		return passoUsuario[uid]
	else:
		usuariosConhecidos.append(uid)
		lembretes[uid] = {}
		eventos[uid] = []
		f = open('usuarios.txt', 'a')
		f.write(str(uid)+"\n")
		f.close()

		try:
			f = open('linhatemp/{}.txt'.format(uid), 'x')
			f.close()
		except FileExistsError:
			pass
		try:
			f = open('eventos/{}.txt'.format(uid), 'x')
			f.close()
		except FileExistsError:
			pass

		passoUsuario[uid] = 0
		v = open('passo/{}.txt'.format(uid), 'w')
		v.write("0")
		v.close()
		return 0


# Essa função é para criar um teclado, ela é usada na lista e mostra ao usuário um teclado com números para cada evento e a opção de cancelar
def teclado_editar(quantidade_items):
	tecladoEditar = types.ReplyKeyboardMarkup()
	tecladoEditar.add(*[str(n)+")" for n in range(1, quantidade_items + 1)]+["CANCELAR"])
	return tecladoEditar

# Salva no dicionário de eventos e no arquivo do usuário cid, o seu evento e organiza os eventos do dicionário por ordem de data.
def salvar_evento(eventos, cid, titulo, data, detalhes, lembrete, selecionarComando):
	# O bot vai tentar colocar as informações dentro da matriz de eventos (#1), mas se no dicionário nada estiver salvo no cid, vai dar KeyError, nesse caso (#2) é criada uma matriz com o evento dentro.
	try:#1                                                           
		eventos[cid].append([titulo, data, detalhes, lembrete])     
	except KeyError:#2                                              
		eventos[cid] = [[titulo, data, detalhes, lembrete]]       

	if lembrete == 0:
		lembreteTexto = "0"
	else:
		lembreteTexto = funcoes.datetime_para_texto(lembrete)

	f = open('eventos/{}.txt'.format(cid), 'a')
	f.write(str(titulo)+"\n"+funcoes.datetime_para_texto(data)+"\n"+str(detalhes)+"\n"+lembreteTexto+"\n")
	f.close()

	for k in range(len(eventos[cid])): 
		for i in range(1, len(eventos[cid]) - k): 
			if eventos[cid][i][1] < eventos[cid][i-1][1]: 
				eventos[cid][i], eventos[cid][i-1] = eventos[cid][i-1], eventos[cid][i] 

	bot.send_message(cid, "Evento \"{}\" - {} salvo!\nO que deseja fazer?".format(titulo, funcoes.datetime_para_texto(data)), reply_markup=selecionarComando) 

# Coloca em fila crescente todos os lembretes salvos e programa o envio.
fila = sched.scheduler(time.time, time.sleep)
def enviar_lembrete(usuario, titulo, data):
	bot.send_message(usuario, "Você terá \"{}\" em {}".format(titulo, data))

for cid in usuariosConhecidos:
	agora = datetime.datetime.now()
	for i in range(len(eventos[cid])):
		if eventos[cid][i][-1] != 0:
			if eventos[cid][i][-1] < agora:
				eventos[cid][i][-1] = 0
			else:
				st = (eventos[cid][i][-1] - agora).total_seconds()
				lembretes[cid][eventos[cid][i][0]+funcoes.datetime_para_texto(eventos[cid][i][1])] = fila.enter(st, 1, enviar_lembrete, argument=(cid, eventos[cid][i][0], funcoes.datetime_para_texto(eventos[cid][i][1])))				
t = threading.Thread(target=fila.run)
t.start()

# Essa função é usada para mostrar na tela cada mensagem recebida num print do tipo: Nome [ID]: "mensagem"
def listener(mensagens):
	# Usado somente para mostrar as mensagens recebidas no console.
	for mensagem in mensagens:
		if mensagem.content_type == 'text':
			print(str(mensagem.chat.first_name) + " [" + str(mensagem.chat.id) + "]: " + mensagem.text)

bot = telebot.TeleBot(token) 
bot.set_update_listener(listener) # a função anterior é usada aqui

# O que o bot faz quando recebe o comando '/start'
@bot.message_handler(commands=['start']) 
def comando_start(mensagem):
	cid = mensagem.chat.id   # ID do usuário que mandou o comando
	# Se o usuário não estiver na lista de usuários conhecidos será mandada a mensagem "Bem vindo [...]" para o usuário cid e vai mostrar o teclado de selecionarComando, isso é o reply_markup=selecionarComando que faz.
	if cid not in usuariosConhecidos:   
		usuariosConhecidos.append(cid)
		lembretes[cid] = {}
		eventos[cid] = []
		with open('usuarios.txt', 'a') as f:
			f.write(str(cid)+"\n")
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "Bem vindo ao AgendaBot, gostaria de adicionar algum evento?", reply_markup=selecionarComando)
		
	else:
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)

# O que o bot responde quando o usuário seleciona a opção 'Adicionar evento'
@bot.message_handler(func=lambda message: message.text == comandos[0] and passo_do_usuario(message.chat.id) == 0)
def adicionar_evento(mensagem):
	cid = mensagem.chat.id 
	bot.send_message(cid, "Digite um título, por favor", reply_markup=cancelar) # Manda uma mensagem pedindo o título e mostra o teclado com a opção cancelar
	passoUsuario[cid] = 1
	with open('passo/{}.txt'.format(cid), 'w') as f:
		f.write("1")

# Salva o título e pergunta a data
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 1) # O que o bot vai fazer quando receber mensagem de um usuário que
def adicionar_evento1(mensagem):                                                  # está no passo 1
	cid = mensagem.chat.id
	if mensagem.text == "CANCELAR": # Se a mensagem for "CANCELAR" 
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
		# Basicamente vai voltar para ao começo, colocando passo = 0 e mostrando a mensagem "O que deseja fazer?" e o teclado
	else:
		linhatemp[str(cid)+"titulo"] = mensagem.text # Salva o título na linhatemp
		with open('linhatemp/{}.txt'.format(cid), 'a') as f:
			f.write(mensagem.text+'\n')
		bot.send_message(cid, "Qual é a data? (digite no formato DD/MM/AAAA)", reply_markup=cancelar)
		# pergunta a data mostrando a opção de cancelar
		passoUsuario[cid] = 2
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("2")

# Salva a data, pergunta o horário
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 2) # O que o bot vai fazer quando receber mensagem de um usuário que
def adicionar_evento2(mensagem):                                                  # está no passo 2
	cid = mensagem.chat.id
	if mensagem.text == "CANCELAR":
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		del linhatemp[str(cid)+"titulo"]
		f = open('linhatemp/{}.txt'.format(cid), 'w')
		f.writelines([""])
		f.close()
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
	else:
		try:
			data = mensagem.text
			data = [int(n) for n in data.split("/")]
			if funcoes.validar_data(data[0], data[1], data[2]) == False or len(data) != 3:
				raise ValueError("Data inválida")
			linhatemp[str(cid)+"data"] = datetime.datetime(data[-1], data[-2], data[-3])
			with open('linhatemp/{}.txt'.format(cid), 'a') as f:
				f.write(funcoes.datetime_para_texto(linhatemp[str(cid)+"data"]))
			bot.send_message(cid, "Qual é o horário? (digite no formato HH:MM)", reply_markup=cancelar) # Pergunta o horário
			passoUsuario[cid] = 3
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("3")
		except (ValueError, IndexError):
			bot.send_message(cid, "Data inválida! Digite a data no formato DD/MM/AAAA !\nExemplo: dia 17 de janeiro de 2029 corresponde a data 17/01/2029.", reply_markup=cancelar)

# Salva o horário e pede os detalhes
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 3)
def adicionar_evento3(mensagem):
	cid = mensagem.chat.id
	if mensagem.text == "CANCELAR":
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		del linhatemp[str(cid)+"titulo"]
		del linhatemp[str(cid)+"data"]
		with open('linhatemp/{}.txt'.format(cid), 'w') as f:
			f.writelines([''])
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
	else:
		try:
			horario = mensagem.text
			horario = [int(n) for n in horario.split(":")]
			if horario[0] < 0 or horario[0] > 23:
				raise ValueError("Hora inválida")
			if horario[1] < 0 or horario[1] > 59:
				raise ValueError("Minuto inválido")
			if len(horario) != 2:
				raise ValueError("Horário inválido")
			linhatemp[str(cid)+"data"] = linhatemp[str(cid)+"data"].replace(hour=horario[0], minute=horario[1])
			with open('linhatemp/{}.txt'.format(cid), 'w') as f:
				f.write(linhatemp[str(cid)+"titulo"]+"\n"+funcoes.datetime_para_texto(linhatemp[str(cid)+"data"])+"\n")
			bot.send_message(cid, "Digite mais detalhes sobre o evento:", reply_markup=cancelar) # Pergunta os detalhes
			passoUsuario[cid] = 4
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("4")
		except (ValueError, IndexError):
			bot.send_message(cid, "Horário inválido! Digite o horário no formato HH:MM !\nExemplo: duas e quarenta e cinco da tarde são 14:45")

# Salva os detalhes e pergunta se quer adicionar um lembrete
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 4)
def adicionar_evento4(mensagem):
	cid = mensagem.chat.id
	if mensagem.text == "CANCELAR":
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		del linhatemp[str(cid)+"titulo"]
		del linhatemp[str(cid)+"data"]
		with open('linhatemp/{}.txt'.format(cid), 'w') as f:
			f.writelines([''])
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
	else:
		linhatemp[str(cid)+"detalhes"] = mensagem.text
		with open('linhatemp/{}.txt'.format(cid), 'a') as f:
			f.write(mensagem.text+"\n")
		agora = datetime.datetime.now()
		if agora < linhatemp[str(cid)+"data"]:
			bot.send_message(cid, "Deseja adicionar lembrete?", reply_markup=sim_ou_não)
			passoUsuario[cid] = 5
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("5")
		else: #3
			salvar_evento(eventos, cid, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], 0, selecionarComando) #4
			passoUsuario[cid] = 0
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("0")
			del linhatemp[str(cid)+"titulo"]
			del linhatemp[str(cid)+"data"]
			del linhatemp[str(cid)+"detalhes"]
			with open('linhatemp/{}.txt'.format(cid), 'w') as f:
				f.writelines([''])

# o que o bot faz dependendo da resposta
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 5)
def lembrete(mensagem):
	cid = mensagem.chat.id
	if mensagem.text == "SIM":
		agora = datetime.datetime.now()
		if (linhatemp[str(cid)+"data"]-agora).days >= 1:
			bot.send_message(cid, "Quantos dias antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((linhatemp[str(cid)+"data"]-agora).days), reply_markup=esconderTeclado)
			linhatemp[str(cid)+"casolembrete"] = 1
			with open('linhatemp/{}.txt'.format(cid), 'a') as f:
				f.write("1")
			passoUsuario[cid] = 6
		elif linhatemp[str(cid)+"data"] < agora:
			bot.send_message(cid, "Não é mais possível criar um lembrete.")
			salvar_evento(eventos, cid, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], 0, selecionarComando)
			passoUsuario[cid] = 0
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("0")
			del linhatemp[str(cid)+"titulo"]
			del linhatemp[str(cid)+"data"]
			del linhatemp[str(cid)+"detalhes"]
		else: 
			bot.send_message(cid, "Quantos horas antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((linhatemp[str(cid)+"data"]-agora).total_seconds()//3600) , reply_markup=esconderTeclado)
			linhatemp[str(cid)+"casolembrete"] = 2
			with open('linhatemp/{}.txt'.format(cid), 'a') as f:
				f.write("1")                                                                                       
			passoUsuario[cid] = 6
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("6")
	elif mensagem.text == "NÃO":
		salvar_evento(eventos, cid, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], 0, selecionarComando)
		del linhatemp[str(cid)+"titulo"] 
		del linhatemp[str(cid)+"data"]
		del linhatemp[str(cid)+"detalhes"]
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
	else:
		bot.send_message(cid, "Por favor selecione uma das opções", reply_markup=sim_ou_não)

# Verifica a data
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 6)
def lembrete1(mensagem):
	cid = mensagem.chat.id
	agora = datetime.datetime.now()
	if linhatemp[str(cid)+"data"] < agora:
		bot.send_message(cid, "Não é mais possível criar um lembrete.")
		salvar_evento(eventos, cid, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], 0, selecionarComando)
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		del linhatemp[str(cid)+"titulo"]
		del linhatemp[str(cid)+"data"]
		del linhatemp[str(cid)+"detalhes"]
		with open('linhatemp/{}.txt'.format(cid), 'w') as f:
			f.write("")
	else:
		try:
			tempo = int(mensagem.text)
			if tempo < 0:
				raise ValueError
			dataE = linhatemp[str(cid)+"data"]
			titulo = linhatemp[str(cid)+"titulo"]
			if linhatemp[str(cid)+"casolembrete"] == 1:
				lembrete = dataE - datetime.timedelta(days=tempo)
			else:
				lembrete = dataE - datetime.timedelta(hours=tempo)
			agora = datetime.datetime.now()
			if lembrete < agora:
				if dataE < agora:
					bot.send_message(cid, "Não é mais possível criar um lembrete.")
					salvar_evento(eventos, cid, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], 0, selecionarComando)
					passoUsuario[cid] = 0
					with open('passo/{}.txt'.format(cid), 'w') as v:
						v.write("0")
					del linhatemp[str(cid)+"titulo"]
					del linhatemp[str(cid)+"data"]
					del linhatemp[str(cid)+"detalhes"]
					with open('linhatemp/{}.txt'.format(cid), 'w') as f:
						f.write("")
				elif (dataE - agora).days >= 1:
					bot.send_message(cid, "Por favor digite um número válido!\nQuantos dias antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((linhatemp[str(cid)+"data"]-agora).days))
					linhatemp[str(cid)+"casolembrete"] = 1
					with open('linhatemp/{}.txt'.format(cid), 'w') as f:
						f.write(linhatemp[str(cid)+"titulo"]+"\n"+funcoes.datetime_para_texto(linhatemp[str(cid)+"data"])+"\n"+linhatemp[str(cid)+"detalhes"]+"1\n")
				else:
					bot.send_message(cid, "Quantos horas antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((linhatemp[str(cid)+"data"]-agora).total_seconds()//3600))
					linhatemp[str(cid)+"casolembrete"] = 2
					with open('linhatemp/{}.txt'.format(cid), 'w') as f:
						f.write(linhatemp[str(cid)+"titulo"]+"\n"+funcoes.datetime_para_texto(linhatemp[str(cid)+"data"])+"\n"+linhatemp[str(cid)+"detalhes"]+"2\n")
			else: #2
				bot.send_message(cid, "Lembrete definido para {}".format(funcoes.datetime_para_texto(lembrete)))
				salvar_evento(eventos, cid, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], lembrete, selecionarComando)			
				del linhatemp[str(cid)+"titulo"]
				del linhatemp[str(cid)+"data"]
				del linhatemp[str(cid)+"detalhes"]
				with open('linhatemp/{}.txt'.format(cid), 'w') as f:
					f.write("")
				passoUsuario[cid] = 0
				with open('passo/{}.txt'.format(cid), 'w') as v:
					v.write("0")
				st = (lembrete - agora).total_seconds()
				lembretes[cid][titulo+funcoes.datetime_para_texto(dataE)] = fila.enter(st, 1, enviar_lembrete, argument=(cid, titulo, funcoes.datetime_para_texto(dataE)))
				t = threading.Thread(target=fila.run)
				t.start()				
		except ValueError:
			agora = datetime.datetime.now()
			if linhatemp[str(cid)+"data"] < agora:
				bot.send_message(cid, "Não é mais possível criar um lembrete.")
				salvar_evento(cid, eventos, linhatemp[str(cid)+"titulo"], linhatemp[str(cid)+"data"], linhatemp[str(cid)+"detalhes"], 0, selecionarComando)
				passoUsuario[cid] = 0
				with open('passo/{}.txt'.format(cid), 'w') as v:
					v.write("0")
				del linhatemp[str(cid)+"titulo"]
				del linhatemp[str(cid)+"data"]
				del linhatemp[str(cid)+"detalhes"]
				with open('linhatemp/{}.txt'.format(cid), 'w') as f:
					f.write("")
			else:
				bot.send_message(cid, "Valor inválido! Por favor digite um número não negativo")

# O que acontece quando o usuário seleciona a opção lista de eventos
@bot.message_handler(func=lambda message: message.text == comandos[1] and passo_do_usuario(message.chat.id) == 0)
def lista_de_eventos(mensagem):
	cid = mensagem.chat.id
	if len(eventos[cid]) == 0:
		bot.send_message(cid, "Não há eventos salvos", reply_markup=esconderTeclado)
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
	else:
		texto1 = "Selecione qual evento deseja editar:\n\n"
		for i in range(len(eventos[cid])):
			texto1 += "{0}) {1}: {2}\n".format(i+1, eventos[cid][i][0], funcoes.datetime_para_texto(eventos[cid][i][1]))
		bot.send_message(cid, texto1, reply_markup=teclado_editar(len(eventos[cid])))
		passoUsuario[cid] = 10
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("10")

opcoesEditar = ["Título", "Data", "Detalhes", "Lembrete", "Deletar", "CANCELAR"]
opcoesTeclado = types.ReplyKeyboardMarkup()
opcoesTeclado.add(*opcoesEditar)

# Caso não consiga ler algo, só ignora
editartemp = {}
for cid in usuariosConhecidos:
	try:
		with open('editartemp/{}.txt'.format(cid), 'r') as f:
			if f.readlines()[0] != "":
				editartemp[cid] = int(f.readlines()[0])
	except FileNotFoundError:
		f = open('editartemp/{}.txt'.format(cid), 'x')
		f.close()
	except IndexError:
		pass

editartempcaso = {}
for cid in usuariosConhecidos:
	try:
		with open('editartempcaso/{}.txt'.format(cid), 'r') as f:
			if f.readlines()[0] != "":
				editartemp[cid] = int(f.readlines()[0])
	except FileNotFoundError:
		f = open('editartempcaso/{}.txt'.format(cid), 'x')
		f.close()
	except IndexError:
		pass

# Ao escolher um dos números, mostra todas as informações e pergunta qual delas deseja editar, caso escolha a opção 'cancelar' volta para o começo, e se não escolher nenhuma das opções, o bot mandará uma mensagem pedindo para escolher uma.
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 10)
def editar(mensagem):
	cid = mensagem.chat.id
	if mensagem.text in [str(n)+")" for n in range(1, len(eventos[cid]) + 1)]:
		edt = int(mensagem.text[:-1]) - 1
		editartemp[cid] = edt
		with open('editartemp/{}.txt'.format(cid), 'w') as f:
			f.write(str(edt))
		if eventos[cid][edt][3] == 0:
			texto2 = "Título:\n{}\n\nData:\n{}\n\nDetalhes:\n{}\n\nLembrete:\nNão definido".format(eventos[cid][edt][0], funcoes.datetime_para_texto(eventos[cid][edt][1]), eventos[cid][edt][2])
		else:
			texto2 = "Título:\n{}\n\nData:\n{}\n\nDetalhes:\n{}\n\nLembrete:\n{}".format(eventos[cid][edt][0], funcoes.datetime_para_texto(eventos[cid][edt][1]), eventos[cid][edt][2], funcoes.datetime_para_texto(eventos[cid][edt][3]))
		bot.send_message(cid, texto2, reply_markup=opcoesTeclado)
		passoUsuario[cid] = 12
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("12")
	elif mensagem.text == "CANCELAR":
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "O que gostaria de fazer?", reply_markup=selecionarComando)
	else:
		bot.send_message(cid, "Por favor selecione uma das opções", reply_markup=teclado_editar(len(eventos[cid])))

# Pede a informação nova caso seja possível, ou faz a ação de deletar ou cancelar.
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 12)
def editar2(mensagem):
	cid = mensagem.chat.id
	agora = datetime.datetime.now()
	if mensagem.text == "Título":
		bot.send_message(cid, "Digite o novo título:", reply_markup=esconderTeclado)
		editartempcaso[cid] = 1
		with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
			f.write("1")
		passoUsuario[cid] = 13
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("13")
	elif mensagem.text == "Data":
		bot.send_message(cid, "Digite a nova data (no formato DD/MM/AAAA):", reply_markup=esconderTeclado)
		editartempcaso[cid] = 2
		with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
			f.write("2")
		passoUsuario[cid] = 13
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("13")
	elif mensagem.text == "Detalhes":
		bot.send_message(cid, "Digite os novos detalhes:", reply_markup=esconderTeclado)
		editartempcaso[cid] = 3
		with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
			f.write("3")
		passoUsuario[cid] = 13
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("13")
	elif mensagem.text == "Lembrete":
		if eventos[cid][editartemp[cid]][1] < datetime.datetime.now():
			bot.send_message(cid, "Não é possível fazer isso! Esse evento já aconteceu!", reply_markup=esconderTeclado)
			passoUsuario[cid] = 0
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("0")
			del editartemp[cid]
			with open('editartemp/{}.txt'.format(cid), 'w') as f:
				f.write("")
			bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
		elif (eventos[cid][editartemp[cid]][1] - datetime.datetime.now()).days >= 1:
			bot.send_message(cid, "Quantos dias antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((eventos[cid][editartemp[cid]][1]-agora).days), reply_markup=esconderTeclado)
			editartempcaso[cid] = 4
			with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
				f.write("4")
			passoUsuario[cid] = 13
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("13")
		else:
			bot.send_message(cid, "Quantos horas antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((eventos[cid][editartemp[cid]][1]-agora).total_seconds()//3600), reply_markup=esconderTeclado)
			editartempcaso[cid] = 5
			with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
				f.write("5")
			passoUsuario[cid] = 13
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("13")
	elif mensagem.text == "Deletar":
		if eventos[cid][editartemp[cid]][3] != 0:
			if datetime.datetime.now() < eventos[cid][editartemp[cid]][3]:
				fila.cancel(lembretes[cid][eventos[cid][editartemp[cid]][0]+funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])])
		del eventos[cid][editartemp[cid]]
		funcoes.salvar_edicao(eventos, cid)
		del editartemp[cid]
		with open('editartemp/{}.txt'.format(cid), 'w') as f:
			f.write("")
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "Evento deletado com sucesso!", reply_markup=esconderTeclado)
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
	elif mensagem.text == "CANCELAR":
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
	else:
		bot.send_message(cid, "Por favor selecione uma das opções", reply_markup=opcoesTeclado)

editartempdata = {}
for cid in usuariosConhecidos:
	try:
		with open('editartempdata/{}.txt'.format(cid), 'r') as f:
			data = [int(n) for n in f.readline().split("/")]
			if len(data) == 3:
				editartempdata[cid] = datetime.datetime(data[-1], data[-2], data[-3])
	except FileNotFoundError:
		f = open('editartempdata/{}.txt'.format(cid), 'x')
		f.close()
	except ValueError:
		pass

# Faz a edição de cada caso (título, data, detalhes, lembrete, deletar e cancelar); a alteração da data é feita em três etapas, nesse def é a primeira.
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 13)
def editar2(m):
	cid = m.chat.id
	if editartempcaso[cid] == 1:
		tituloNovo = m.text
		if eventos[cid][editartemp[cid]][3] != 0:
			if datetime.datetime.now() < eventos[cid][editartemp[cid]][3]:
				fila.cancel(lembretes[cid][eventos[cid][editartemp[cid]][0]+funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])])
				st = (eventos[cid][editartemp[cid]][3] - datetime.datetime.now()).total_seconds()
				lembretes[cid][tituloNovo+funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])] = fila.enter(st, 1, enviar_lembrete, argument=(cid, tituloNovo, funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])))
				t = threading.Thread(target=fila.run)
				t.start()
		eventos[cid][editartemp[cid]][0] = tituloNovo
		funcoes.salvar_edicao(eventos, cid)
		bot.send_message(cid, "Título editado com sucesso!")
		del editartempcaso[cid]
		with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
			f.write("")
		del editartemp[cid]
		with open('editartemp/{}.txt'.format(cid), 'w') as f:
			f.write("")
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)

	elif editartempcaso[cid] == 2:
		try:
			dataNova = [int(n) for n in m.text.split("/")]
			validar = funcoes.validar_data(dataNova[0], dataNova[1], dataNova[2])
			if validar == False or len(dataNova) != 3:
				raise ValueError("Data inválida")
			with open('editartempdata/{}.txt'.format(cid), 'w') as f:
				f.write(m.text)
			editartempdata[cid] = datetime.datetime(dataNova[-1], dataNova[-2], dataNova[-3])
			bot.send_message(cid, "Digite o novo horário (no formato HH:MM): ")
			passoUsuario[cid] = 14
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("14")
		except (ValueError, IndexError):
			bot.send_message(cid, "Data inválida! Digite a data no formato DD/MM/AAAA !\nExemplo: dia 17 de janeiro de 2029 corresponde a data 17/01/2029.")

	elif editartempcaso[cid] == 3:
		detalhesNovo = m.text
		eventos[cid][editartemp[cid]][2] = detalhesNovo
		funcoes.salvar_edicao(eventos, cid)
		bot.send_message(cid, "Detalhes editados com sucesso!")
		del editartempcaso[cid]
		with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
			f.write("")
		del editartemp[cid]
		with open('editartemp/{}.txt'.format(cid), 'w') as f:
			f.write("")
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
		bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)

	elif editartempcaso[cid] == 4 or editartempcaso[cid] == 5:
		try:
			tempo = int(m.text)	
			if tempo < 0:
				raise ValueError
			titulo = eventos[cid][editartemp[cid]][0]
			if editartempcaso[cid] == 4:
				lembrete = eventos[cid][editartemp[cid]][1] - datetime.timedelta(days=tempo)
			else:
				lembrete = eventos[cid][editartemp[cid]][1] - datetime.timedelta(hours=tempo)
			agora = datetime.datetime.now()
			if lembrete < agora:
				if eventos[cid][editartemp[cid]][1] < agora:
					bot.send_message(cid, "Não é possível criar um lembrete.")
					bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
					passoUsuario[cid] = 0
					with open('passo/{}.txt'.format(cid), 'w') as v:
						v.write("0")
				elif (eventos[cid][editartemp[cid]][1] - agora).days >= 1:
					bot.send_message(cid, "Número inválido!\nQuantos dias antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((eventos[cid][editartemp[cid]][1]-agora).days))
					editartempcaso[cid] == 4
					with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
						f.write("4")
				else:
					bot.send_message(cid, "Número inválido!\nQuantos horas antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((eventos[cid][editartemp[cid]][1]-agora).total_seconds()//3600))
					editartempcaso[cid] == 5
					with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
						f.write("5")
			else:
				try:
					fila.cancel(lembretes[cid][eventos[cid][editartemp[cid]][0]+funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])])
				except KeyError:
					pass
				st = (lembrete - datetime.datetime.now()).total_seconds()
				eventos[cid][editartemp[cid]][3] = lembrete
				lembretes[cid][eventos[cid][editartemp[cid]][0]+funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])] = fila.enter(st, 1, enviar_lembrete, argument=(cid, eventos[cid][editartemp[cid]][0], funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])))
				t = threading.Thread(target=fila.run)
				t.start()
				bot.send_message(cid, "Lembrete definido para {}".format(funcoes.datetime_para_texto(lembrete)))
				funcoes.salvar_edicao(eventos, cid)
				passoUsuario[cid] = 0
				with open('passo/{}.txt'.format(cid), 'w') as v:
					v.write("0")
				bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
				
		except ValueError:
			agora = datetime.datetime.now()
			if eventos[cid][editartemp[cid]][1] < agora:
				bot.send_message(cid, "Não é possível criar um lembrete.")
				bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
				passoUsuario[cid] = 0
				with open('passo/{}.txt'.format(cid), 'w') as v:
					v.write("0")
			else:
				bot.send_message(cid, "Valor inválido! Por favor digite um número não negativo")

# Segunda parte da data vai perguntar se quer um lembrete 
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 14)
def editar_horario(mensagem):
	try:
		cid = mensagem.chat.id
		horarioNovo = mensagem.text
		horarioNovo = [int(n) for n in horarioNovo.split(":")]
		if horarioNovo[0] < 0 or horarioNovo[0] > 23:
			raise ValueError("Hora inválida")
		if horarioNovo[1] < 0 or horarioNovo[1] > 59:
			raise ValueError("Minuto inválido")
		if len(horarioNovo) != 2:
			raise ValueError("Horário inválido")
		editartempdata[cid] = editartempdata[cid].replace(hour=horarioNovo[0], minute=horarioNovo[1])
		newDate = editartempdata[cid]
		if eventos[cid][editartemp[cid]][3] != 0:
			if datetime.datetime.now() < eventos[cid][editartemp[cid]][3]:
				fila.cancel(lembretes[cid][eventos[cid][editartemp[cid]][0]+funcoes.datetime_para_texto(eventos[cid][editartemp[cid]][1])])
		eventos[cid][editartemp[cid]][1] = newDate
		del editartempdata[cid]
		with open('editartempdata/{}.txt'.format(cid), 'w') as f:
			f.write("")
		eventos[cid][editartemp[cid]][3] = 0
		if newDate < datetime.datetime.now():
			for k in range(len(eventos[cid])):
				for i in range(1, len(eventos[cid]) - k):
					if eventos[cid][i][1] < eventos[cid][i-1][1]:
						eventos[cid][i], eventos[cid][i-1] = eventos[cid][i-1], eventos[cid][i]
			funcoes.salvar_edicao(eventos, cid)
			bot.send_message(cid, "Data editada com sucesso!")
			passoUsuario[cid] = 0
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("0")
			bot.send_message(cid, "O que deseja fazer?", reply_markup=selecionarComando)
		else:
			bot.send_message(cid, "Data editada com sucesso!\nDeseja colocar um lembrete?", reply_markup=sim_ou_não)
			passoUsuario[cid] = 15
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("15")
	except (ValueError, IndexError):
		bot.send_message(cid, "Horário inválido! Digite o horário no formato HH:MM !\nExemplo: duas e quarenta e cinco da tarde são 14:45")

# Terceira parte da data o que o bot faz caso a resposta seja 'sim' ou 'não'
@bot.message_handler(func=lambda message: passo_do_usuario(message.chat.id) == 15)
def editar_horario2(m):
	cid = m.chat.id
	if m.text == "SIM":
		agora = datetime.datetime.now()
		if (eventos[cid][editartemp[cid]][1]-agora).days >= 1:
			bot.send_message(cid, "Quantos dias antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((eventos[cid][editartemp[cid]][1]-agora).days), reply_markup=esconderTeclado)
			editartempcaso[cid] = 4
			with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
				f.write("4")
			passoUsuario[cid] = 13
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("13")
		elif eventos[cid][editartemp[cid]][1] < agora:
			bot.send_message(cid, "Não é mais possível criar um lembrete.")
			for k in range(len(eventos[cid])):
				for i in range(1, len(eventos[cid]) - k):
					if eventos[cid][i][1] < eventos[cid][i-1][1]:
						eventos[cid][i], eventos[cid][i-1] = eventos[cid][i-1], eventos[cid][i]
			funcoes.salvar_edicao(eventos, cid)
			bot.send_message(cid, "Edição concluída!\nO que deseja fazer?", reply_markup=selecionarComando)
			passoUsuario[cid] = 0
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("0")
		else:
			bot.send_message(cid, "Quantos horas antes do evento você deseja ser lembrado?\n(O número máximo que você pode digitar é: {})".format((eventos[cid][editartemp[cid]][1]-agora).total_seconds()//3600) , reply_markup=esconderTeclado)
			editartempcaso[cid] = 5
			with open('editartempcaso/{}.txt'.format(cid), 'w') as f:
				f.write("5")
			passoUsuario[cid] = 13
			with open('passo/{}.txt'.format(cid), 'w') as v:
				v.write("13")
	elif m.text == "NÃO" or eventos[cid][editartemp[cid]][1] < datetime.datetime.now():
		for k in range(len(eventos[cid])):
			for i in range(1, len(eventos[cid]) - k):
				if eventos[cid][i][1] < eventos[cid][i-1][1]:
					eventos[cid][i], eventos[cid][i-1] = eventos[cid][i-1], eventos[cid][i]
		funcoes.salvar_edicao(eventos, cid)
		bot.send_message(cid, "Edição concluída!\nO que deseja fazer?", reply_markup=selecionarComando)
		passoUsuario[cid] = 0
		with open('passo/{}.txt'.format(cid), 'w') as v:
			v.write("0")
	else:
		bot.send_message(cid, "Por favor selecione uma das opções", reply_markup=sim_ou_não)

bot.polling() # Executa o bot