import datetime
def validar_data(dia, mes, ano):
	try:
		datetime.date(ano, mes, dia)
		return True
	except ValueError:
		return False

def dois_digitos(n):
	if n < 10:
		return "0"+str(n)
	else:
		return str(n)

def texto_para_datetime(texto):
	'''
	Converte o texto no formato "DD/MM/AAAA HH:MM" para um datetime.
	'''
	dataT = texto.split()
	data = [int(n) for n in dataT[0].split("/")]
	hora = [int(n) for n in dataT[1].split(":")]
	return datetime.datetime(data[-1], data[-2], data[-3], hora[0], hora[1])

def datetime_para_texto(dt):
	'''
	Converte um datetime para um texto no formato "DD/MM/AAAA HH:MM"
	'''
	return "{}/{}/{} {}:{}".format(dois_digitos(dt.day), dois_digitos(dt.month), dt.year, dois_digitos(dt.hour), dois_digitos(dt.minute))

def salvar_edicao(eventos, cid):
	'''
	Salva uma edição feita no dicionário para o arquivo.
	'''
	linhas_salvar = []
	for linha in eventos[cid]:
		linhas_salvar.append(linha[0]+"\n")
		linhas_salvar.append(datetime_para_texto(linha[1])+"\n")
		linhas_salvar.append(linha[2]+"\n")
		if linha[3] == 0:
			linhas_salvar.append("0\n")
		else:
			linhas_salvar.append(datetime_para_texto(linha[3])+"\n")
	with open('eventos/{}.txt'.format(cid), 'w') as f:
		f.writelines(linhas_salvar)