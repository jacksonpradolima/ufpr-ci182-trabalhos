import telepot
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Este código abaixo é o token do bot do Telegram. É através dele que o Python comandará o bot.
bot = telepot.Bot("781465027:AAF61wjbH08clR3UIQCQWAoAnvb4HL_VpXM")
#print(bot.getUpdates())
'''
Esse print acima, quando executado, mostra todos os detalhes
e informações de uma mensagem enviada, do tipo da mensagem e do usuário que enviou.
Entretanto, aqui usaremos apenas a mensagem em si e o chatid do usuário.
'''
mensagem = ""
cid = 0

#Essa função recebe as mensagens que são enviadas para o bot
def recebendoMsg(msg):
	global mensagem
	global cid
	mensagem = msg['text'] # mensagem = mensagem enviada pelo usuário no telegram
	cid = msg['chat']['id'] # cid = chatid do usuário, é o número pelo qual o bot
							#chamará ele no telegram
	return mensagem
	return cid

'''
Nessa função, assim que a conversa for iniciada no telegram, ou seja,
o bot receber a mensagem "/start", o cliente poderá agendar a viagem,
seguindo o passo a passo do bot
'''
def conversa(m,chatid):
	if m == "/start" or m == "Agendar":
		bot.sendMessage(chatid,"Olá. Seja bem vindo ao TesteViagensBot.\nPreencha as informações abaixo para agendar uma viagem.")
		bot.sendMessage(chatid,"Nome:") 
		'''
		A função sendMessage pertence à biblioteca do telepot,
		e serve para que o bot mande uma mensagem. Nesse caso,
		ele está mandando uma mensagem para a pessoa com o id identificado
		na função recebendoMsg e o corpo da mensagem é "Nome:"

		O laço abaixo serve para que o bot só continue os comandos
		quando o usuário digitar a resposta da pergunta anterior
		'''
		while mensagem == "/start" or mensagem == "Agendar":
			pass
		nome = mensagem
		bot.sendMessage(chatid,"RG:")
		while mensagem == nome:
			pass
		rg = mensagem
		bot.sendMessage(chatid,"Telefone:")
		while mensagem == rg:
			pass
		telefone = mensagem
		bot.sendMessage(chatid,"E-mail:")
		while mensagem == telefone:
			pass
		email = mensagem
		bot.sendMessage(chatid,"Local de embarque: (Opções padrão: Garagem, Santa Maria, Praça Rui Barbosa, Habib's, Tulio)")
		while mensagem == email:
			pass
		local = mensagem
		bot.sendMessage(chatid,'Agendamento realizado.\nApós a confirmação da viagem, você receberá um e-mail com todas as informações necessárias.\nPara agendar outra viagem, digite "Agendar"')
		permitir(nome,rg,telefone,email,local)


def cadastrar(nome,rg,telefone): 
	'''
	Essa função será utilizada para cadastrar os dados que o usuário forneceu
	na função conversa, e eles serão guardados no arquivo .txt,
	que contém as informações sobre os clientes
	'''
	cadastros = open('cadastros.txt','a')
	cadastro = nome + ';' + rg + ';' + telefone + ';\n'
	cadastros.write(cadastro)
	cadastros.close()

def permitir(nome,rg,telefone,email,local):
	'''
	Para impedir flood e bagunça do arquivo .txt com a informação dos clientes,
	sempre que dados forem fornecidos para um agendamento, eles precisarão passar por
	aprovação do dono do bot. Assim, só serão cadastrados os clientes que são realmente reais,
	e não clientes fakes jogados no chat do bot para "inundar" o arquivo. 
	É um anti-spam, porém seletivo manualmente.
	'''
	bot.sendMessage(680275748, "Um cliente realizou um agendamento. Confira os dados da viagem:\nNome: {0}\nRG: {1}\nTelefone: {2}\nE-mail: {3}".format(nome,rg,telefone,email))
	bot.sendMessage(680275748, "Permitir o cadastro no arquivo de clientes? (Sim/Nao)")
	while mensagem == local:
		pass
	while mensagem != "Sim" and mensagem != "Nao" and cid == 680275748:
		nova = mensagem
		bot.sendMessage(680275748,"Digite Sim ou Nao para responder")
		while mensagem == nova:
			pass
	if mensagem == "Sim" and cid == 680275748:
		cadastrar(nome,rg,telefone)
		bot.sendMessage(680275748,"Cadastro adicionado com sucesso")
		bot.sendMessage(680275748,"Adicione as informações referentes à viagem:")
		bot.sendMessage(680275748,"Horário de embarque:")
		while mensagem == "Sim" and cid == 680275748:
			pass
		horario = mensagem
		bot.sendMessage(680275748,"Preço:")
		while mensagem == horario and cid == 680275748:
			pass
		preco = mensagem
		bot.sendMessage(680275748,"Feito. Viagem confirmada e um e-mail com as informações foi enviado para o cliente.")
		mandar_email(nome,rg,telefone,email,local,horario,preco)


	elif mensagem == "Nao" and cid == 680275748:
		bot.sendMessage(680275748, "Cadastro descartado")

def mandar_email(nome,rg,telefone,email,local,horario,preco):
	'''
	Nessa função, serão utilizados comandos das bibliotecas MIMEMultipart, MIMEText e smtp
	para enviar um e-mail ao cliente que agendou a viagem.
	As bibliotecas MIME cuidam da formatação do texto, e a smtp
	é responsável pela criação do servidor para envio automático do e-mail.
	'''
	msg = MIMEMultipart()

	message = "Olá. Sua viagem foi confirmada. Seguem abaixo as informações:\nNome: {0}\nRG: {1}\nTelefone: {2}\nLocal de embarque: {3}\nHorário de embarque: {4}\nPreço: {5}".format(nome,rg,telefone,local,horario,preco) 
 
	password = "telegram"
	msg['From'] = "paristurismocwb@gmail.com"
	msg['To'] = email
	msg['Subject'] = "Confirmação da viagem - Paris Turismo"
 
	msg.attach(MIMEText(message, 'plain'))
 
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls() #Este comando é importante para tornar a conexão segura
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()

#Esse comando deixa o recebimento de mensagens em loop enquanto o programa estiver rodando
bot.message_loop(recebendoMsg)

'''
Esse laço faz com que a função conversa sempre seja chamada
para qualquer mensagem enviada. Assim que a pessoa digitar /start,
a função faz seu papel
'''
while True:
	conversa(mensagem,cid)

'''
Esse laço faz com o que o programa fique rodando para sempre (loop infinito),
e assim o bot sempre receberá mensagens até que
o terminal seja fechado manualmente (Ctrl+C)
'''
while True:
	pass