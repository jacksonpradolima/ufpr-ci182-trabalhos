import datetime
import numpy as np
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def cadastrar():
	'''
	Esta função faz o cadastro de novos passageiros no banco de dados.
	'''
	cadastros = open('cadastros.txt','a')

	novo_cadastro = input('Deseja adicionar novo cadastro? (s/n) >')
	novo_cadastro = validar(novo_cadastro, 1)
	
	# Este laço de repetição serve para adicionar quantos cadastros forem necessários.
	while novo_cadastro == 's':

		nome = input('Digite Nome: ')
		rg = input('Digite o RG: ')
		telefone = input('Digite o Telefone: ')

		# Padroniza as informações dentro do arqquivo.
		cadastro = nome + ';' + rg + ';' + telefone + ';\n'
		cadastros.write(cadastro)
	
		novo_cadastro = input('Deseja adicionar novo cadastro? (s/n) >')
		novo_cadastro = validar(novo_cadastro, 1)

	cadastros.close()


def busca():
	'''
	Esta função realiza a busca de nomes dentro do bando de dados.
	'''
	while True:
		texto = input("Digite nome ou RG ou Telefone que deseja procurar: ")
		# Esta parte lê todo o arquivo e coloca as informações em uma lista.
		cadastros = open('cadastros.txt','r')
		lista = cadastros.readlines()
		lista.sort()
		cadastros.close()

		encontrados = []
		# Laço de repetição para procurar o texto informado pelo usuário na lista.	
		for x in lista:
			if texto in x:
				encontrados.append(x)

		# Esta parte separa em casos de acordo com a quantidade de cadastros encontrados.
		if len(encontrados) == 0:
			print('Não foi encontrado cadastro para "{0}"'.format(texto))

		elif len(encontrados) == 1:
			formatar_texto_saida(encontrados)
			relatorio = input("Deseja adicionar à lista de embarque? (s/n) >")
			relatorio = validar(relatorio, 1)

			if relatorio == 's':
				add_lista_embarque(encontrados)

		else:
			print('Foram encontrados os seguintes cadastros: \n')
			formatar_texto_saida(encontrados)

		busca = input('Deseja procurar outro cadastro? (s/n) >')
		busca = validar(busca, 1)

		if busca == 'n':
				break

def add_lista_embarque(cliente):
	'''
	Esta função recebe como argumento o cliente encontrado na busca
	(quando apenas um é encontrado) e o adiciona na lista de embarque.
	'''

	# Esta parte solicita ao usuário uma informação importante para a lista de embarque.
	print('''
	Onde será o embarque?
	(g) p/ Garagem
	(s) p/ Santa Marta
	(r) p/ Praça Rui Barbosa
	(h) p/ Habbib`s
	(t) p/ Tulio
	(o) p/ Outro
	''')

	embarque = input('>')
	embarque = validar(embarque, 3)

	if embarque == 'g':
		lugar = 'Garagem'
	elif embarque == 's':
		lugar = 'Santa Marta'
	elif embarque == 'r':
		lugar = 'Rui Barbosa'
	elif embarque == 'h':
		lugar = "Habbib's"
	elif embarque == 't':
		lugar = 'Tulio'
	elif embarque == 'o':
		lugar = input('Digite o lugar de embarque: ')

	# Esta parte formata a informação do cliente para ser adicionada à lista de embarque.
	aux1 = cliente[0].split(';')
	aux1[-1] = lugar
	aux1.pop(1)
	lista_embarque.append(aux1)
	lista_embarque.sort()

def visualiza_lista_embarque(lista_embarque):
	'''
	Esta função recebe a lista de embarque como argumento e cria um Data Frame (tabela)
	usando a biblioteca Pandas para visualização da lista antes de gerar o PDF para impressão.
	'''
	# Verifica se a lista não está vazia.
	if len(lista_embarque) > 0:
		df = pd.DataFrame(data=lista_embarque, index=range(1, len(lista_embarque)+1), columns=['Nome', 'Telefone', 'Embarque'])
		print(df)

		a = input('Deseja remover alguém da lista? (s/n) >')
		a = validar(a, 1)

		if a == 's':
			remover()
	else:
		print('Ainda não foi adicionado ninguém na lista de embarque.')



def remover():
	'''
	Esta função remove algum cliente da lista de embarque.
	'''
	remover_linha = int(input('Digite o número da linha que deseja remover :'))
	remover_linha = validar(remover_linha, 4)

	del lista_embarque[int(remover_linha)-1]

	# Esta parte verifica se a lista não está vazia e pergunta se o usuário deseja remover outro cliente
	# e gera novamente a Tabela para visualização da lista
	if len(lista_embarque) > 0:
		df = pd.DataFrame(data=lista_embarque, index=range(1, len(lista_embarque)+1), columns=['Nome', 'Telefone', 'Embarque'])
		print(df)

		a = input('Deseja remover mais alguém? (s/n) >')
		a = validar(a, 1)

		while a == 's':
			# Esta parte é igual a parte de cima, porém dentro do laço de repetição caso o usuário deseje remover mais de um cliente.
			remover_linha = int(input('Digite o número da linha que deseja remover :'))
			remover_linha = validar(remover_linha, 4)

			del lista_embarque[int(remover_linha)-1]

			if len(lista_embarque) > 0:
				df = pd.DataFrame(data=lista_embarque, index=range(1, len(lista_embarque)+1), columns=['Nome', 'Telefone', 'Embarque'])
				print(df)
				
				a = input('Deseja remover mais alguém? (s/n) >')
				a = validar(a, 1)
			else:
				print('Lista de embarque vazia.')
				break
	else:
		print('Lista de embarque vazia.')

def editar():
	'''
	Esta função permite editar as informações de algum cadastro no banco de dados.
	'''

	while True:
		# Abre o arquivo e copia os dados para dentro de uma lista.
		cadastros = open('cadastros.txt','r')
		lista = cadastros.readlines()
		cadastros.close()

		# Esta parte faz uma busca por texto informado pelo usuário de forma similar à função busca acima.
		texto = input("Qual cadastro deseja editar? >")
		encontrados = []
		
		for x in lista:
			if texto in x:
				encontrados.append(x)

		# Verifica se foi encontrado nenhum, um ou mais cadastros de acordo com o texto digitado.
		if len(encontrados) == 0:
			print('Não foi encontrado cadastro para "{0}"'.format(texto))

		elif len(encontrados) == 1:
			formatar_texto_saida(encontrados)
			# Pergunta qual informação o usuário deseja alterar.
			edit = input('Editar Nome, RG, Telefone ou buscar outro cadastro? (nome/rg/tel/outro) >')
			edit = validar(edit, 2)
			
			# Esta parte cria uma lista auxiliar para "segurar" as informações do cliente.
			aux = []
			aux = encontrados[0].split(';')
			aux.pop()

			if edit == 'outro':
				pass
			else:
				# Esta parte altera a informação desejada.
				if edit == 'nome':
					aux[0] = input('Nome: ')
				elif edit == 'rg':
					aux[1] = input('RG: ')
				elif edit == 'tel':
					aux[2] = input('Telefone: ')

				# Esta parte abre o arquivo do banco de dados, substitui as informações do cadastro editado e reescreve o arquivo.
				cadastros = open('cadastros.txt', 'w')
				pos = lista.index(encontrados[0])
				lista.pop(pos)
				aux = aux[0] + ';' + aux[1] + ';' + aux[2] + ';\n'
				lista.append(aux)
				lista.sort()

				cadastros.writelines(lista)

				cadastros.close()


		else:
			print('Foram encontrados os seguintes cadastros: \n')
			formatar_texto_saida(encontrados)

		busca = input('Deseja editar outro cadastro? (s/n) >')
		busca = validar(busca, 1)

		if busca == 'n':
				break


def imprimir(lista_embarque):
	'''
	Esta função gera um arquivo PDF contendo a lista de embarque para impressão.
	'''
	# Esta parte inicia a criação da lista de embarque na forma de uma tabela em PDF usando a biblioteca Reportlab.
	doc = SimpleDocTemplate("lista_embarque.pdf", pagesize=A4)
	elements = []

	# Laço de repetição para inserir índices em cada linha na lista de embarque.
	for x in range(len(lista_embarque)):
		i = str(x+1)
		lista_embarque[x].insert(0, i)

	# Esta parte utiliza a biblioteca DateTime para descobrir o dia que o documento está sendo gerado.
	hoje = datetime.datetime.now()
	hoje = hoje.strftime("%d/%m/%Y")
	# Cria um título para a tabela contendo um texto padrão e a data.
	titulo = 'LISTA DE EMBARQUE - VIAGEM DIA '+hoje

	# Insere na primeira linha da lista o título e na segunda linha os nomes das colunas.
	lista_embarque.insert(0, ['     ', 'Nome','Telefone','Embarque','Polt.','Pago'])
	lista_embarque.insert(0, [titulo])

	# Formatação da tabela pela biblioteca Reportlab.
	t=Table(lista_embarque)
	t.setStyle(TableStyle(
		[('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('SPAN', (0,0), (-1,0)),
		('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0), (-1,-1), 0.25, colors.black)]
	))
	elements.append(t)
	# Salva o documento criado na pasta que o programa está sendo executado.
	doc.build(elements)

def formatar_texto_saida(texto):
	'''
	Função auxiliar para formatar as informações do cadastro e imprimir na tela.
	'''
	for x in texto:
		aux = []
		aux = x.split(';')
		print('Nome: {0}, RG: {1}, Telefone: {2}\n'.format(aux[0], aux[1], aux[2]))


def validar(escolha, n):
	'''
	Esta função recebe dois argumentos, o primeiro é uma string digitada pelo usuário
	e a segunda é um inteiro para identificar uma categoria, e então garante que
	o usuário terá digitado corretamente a informação solicitada pelo programa.
	'''

	if n == 1:
		while escolha != 's' and escolha !='n':
			escolha = input('Comando inválido, digite "s" para sim ou "n" para não >')

	elif n == 2:
		while escolha != 'nome' and escolha != 'rg' and escolha != 'tel' and escolha != 'outro':
			print('''
	Comando inválido
	Digite "nome" para editar o Nome
	Digite "rg" para editar o RG
	Digite "tel" para editar o Telefone
	Digite "outro" para buscar outro cadastro
	''')
			escolha = input('>')

	elif n == 3:
		while escolha != 'g' and escolha != 's' and escolha != 'r' and escolha != 'h' and escolha != 't' and escolha != 'o':
			print('''
	Opção inválida, as opções disponíveis são as seguintes:
	(g) p/ Garagem
	(s) p/ Santa Marta
	(r) p/ Praça Rui Barbosa
	(h) p/ Habbib`s
	(t) p/ Tulio
	(o) p/ Outro)
	''')
			escolha = input('>')

	elif n == 4:
		while escolha > len(lista_embarque):
			escolha = int(input('A lista possui apenas {0} clientes, digite novamente o número da linha :'.format(len(lista_embarque))))

	return escolha
	
# Início do programa.
print('''
	Digite 'c' para adicionar novo cadastro
	Digite 'b' para buscar cadastro
	Digite 'e' para editar cadastro
	Digite 'v' para visualizar documento de impressão
	Digite 'i' para imprimir a lista de embarque
	Digite 's' para sair
''')

escolha = input('>')
lista_embarque = []

while True:

	if escolha == 'c':
		cadastrar()
		
	elif escolha == 'b':
		busca()

	elif escolha == 'e':
		editar()

	elif escolha == 'v':
		visualiza_lista_embarque(lista_embarque)
	
	elif escolha == 'i':
		print('''
	Tem certeza que deseja gerar lista de embarque para impressão e fechar o programa?
	Você pode escolher "n" e em seguida selecionar "v" para verificar se os dados na lista de embarque estão corretos antes de imprimir.
			''')
		certeza = input('(s/n) >')
		certeza = validar(certeza, 1)

		if certeza == 's':
			imprimir(lista_embarque)
			print('Lista de embarque gerada com sucesso!')
			print('Fim de execução!')
			break

	elif escolha == 's':		
		sair = input('Tem certeza que deseja sair? A lista de embarque será perdida! (s/n) >')
		sair = validar(sair, 1)

		if sair == 's':
			break

	else:
		print('Opção inválida, tente novamente!')

	print('''
	Digite 'c' para adicionar novo cadastro
	Digite 'b' para buscar cadastro
	Digite 'e' para editar cadastro
	Digite 'v' para visualizar documento de impressão
	Digite 'i' para imprimir a lista de embarque
	Digite 's' para sair
	''')

	escolha = input('>')
