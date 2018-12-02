import sys, termios, tty, os, time, fcntl, timeit, random

def linha(n):
	#lista que criamos para usar ao longo do programa
	#linha(n) é a lista com as posições de todas as linhas de um sudoku nxn
	linha = []
	for k in range(n):
		#formula da k-ésima linha
		l = []
		for p in range(n): #p é cada elemento da k-ésima linha
			l += [(k*n) + p] #deduzimos a fórmula para cada elemento da k-ésima linha
		linha += [l]
	return linha


def coluna(n):
	#coluna(n) é a lista com as posições de todas as colunas de um sudoku nxn
	coluna = []
	for k in range(n): #fórmula da k-ésima coluna
		c = []
		for p in range(n): #p é cada elemento da k-ésima coluna
			c += [k + (p*n)] #deduzimos essa fórmula pra cada elemento da k-ésima coluna
		coluna += [c]
	return coluna

def quadrado(n):
	#quadrado(n) é a lista com as posições de todos os quadrados de um sudoku nxn
	quadrado = []
	j = int(n**(1/2)) #porque o sudoku terá sempre j "linhazonas"
	for a in range(j): #pegamos as linhazonas
		for k in range(j): #pegamos os quadrados
			q = []
			prim_el = (j**3)*a + j*k #fórmula encontrada para o primeiro elemento do k-ésimo quadrado
			for p in range(j): #pegamos a linha do quadrado
				l = [] #lista vazia para cada linha p do quadrado
				for i in range(j): #i é cada elemento do quadrado
					l += [prim_el + i] #a linha será sempre o primeiro elemento + i
				prim_el += n #para encontrar o primeiro elemento da próxima linha
				q += l
			quadrado += [q] 
	return quadrado

def op(sudoku):
#opcoes para cada casa do sudoku
	m = len(sudoku)
	n = int(m**(1/2))
	#vamos chamar as funções linha, coluna e quadrado
	linhaa =  linha(n)
	colunaa =  coluna(n)
	quadradoo = quadrado(n)
	i = 0 
	op = [] #op = opcoes

	while i < m: #i é cada posição dos elementos do sudoku
		if sudoku[i] != "": #se não tem aspas é pq a casa já está preenchida com um numero, então não tem opção nenhuma
			op += [""] #aspas pq é convenção
		else:
			usados = set() #usados será o conjunto de elementos já usados na mesma linha, coluna e quadrado de cada elemento
		#set() é conjunto vazio 
			l = c = q = 0
		#l é qual linha o i está, c coluna e q quadrado
			while not(i in linhaa[l]): #queremos achar a linha em que o i está
				l+=1
			while not(i in colunaa[c]): #queremos achar a coluna em que o i está
				c+=1
			while not(i in quadradoo[q]): #queremos achar a quadrado em que o i está
				q+=1
			for k in range(n): #esse for serve para variar os elementos de cada linha, coluna e quadrado que o elemento está
				s=sudoku[linhaa[l][k]] #encontramos o elemento que está na posição linhaa[l][k]
				usados.add(s)
				usados.add(sudoku[colunaa[c][k]])#encontramos o elemento que está na posição colunaa[l][k]
				usados.add(sudoku[quadradoo[q][k]])#encontramos o elemento que está na posição quadradoo[l][k]
			u={str(i+1) for i in range(n)} #todas as possibilidades para preencher uma casa (sem contar outras casas já preenchidas) (TOTALZÃO)
			#{'1','2',...,'n'}
			op_i = u-(usados) #op_i = opções para cada entrada i
			op += [op_i] #op será uma lista com m listas, onde cada lista i terá as opções para a posição i
		i+=1
	return op


def qt_op(op):
#QUANTIDADE de opções para cada entrada do sudoku
	qt = []
	for k in op:
		if k == "":
			qt+= [1000]
			#colocamos 1000 no lugar de "" porque depois vamos procurar a entrada com menos opções aplicando min(qt_op(op))
		else:
			qt += [len(k)] #contamos o número de opções de cada entrada k 
	return qt


def validacao(sudoku):
	#valida o sudoku inserido pelo usuário
	n = len(sudoku)**(1/2)
	n = int(n)
	m = (n**2)

	linhaa =  linha(n)
	colunaa =  coluna(n)
	quadradoo = quadrado(n)
	if type(sudoku) != type([]): 
		return "Favor inserir um vetor!"
	num_entradas = len(sudoku)**(1/4) #o sudoku sempre deve sempre ter um quadrado perfeito de um quadrado perfeito entradas
	#o sudoku é um quadrado cheio de quadrados dentro, então a dimensão tem que ser o quadrado de um quadrado
	#len é int mas quando tira raiz quarta fica float
	if num_entradas != int(num_entradas):
		#no python, 3.0 == 3
		return "Número de entradas não corresponde a de um sudoku."
	marina = [""]
	for a in range(1, n+1):	#vamos verificar se a entrada é válida
		marina.append(str(a)) #marina = ["","1","2",...,"n"]
	#for k in sudoku:
	#	if k not in marina:
	#		return "Entrada inválida!" #se não é "" ou se não é nenhum número no range(1, n+1), a entrada é inválida

	for k in range(n): #agora, vamos ver se há dois num iguais na mesma linha/coluna/quadrado
		col = []
		li = []
		qua = []
		for j in range(n):
			li += [sudoku[linhaa[k][j]]] #elemento da pos linhaa[k][j]
			col += [sudoku[colunaa[k][j]]]#elemento da pos colunaa[k][j]
			qua += [sudoku[quadradoo[k][j]]]#elemento da pos quadradoo[k][j]

		for i in li:
			if i!="" and i!="#":
				if li.count(i) > 1:
					return """Sudoku inválido.
Dois números iguais na mesma linha!"""
		for i in col:
			if i!="":
				if col.count(i) > 1:
					return """Sudoku inválido.
Dois números iguais na mesma coluna!"""
		for i in qua:
			if i!="":
				if qua.count(i) > 1:
					return """Sudoku inválido.
Dois números iguais no mesmo quadrado!"""
	return "Sudoku válido."

def salve(v): #pra não estragar o vetor
	k=[i for i in v]
	return k

def resolversudoku(sudoku): #da uma solução para o sudoku inserido pelo usuário
	#primeiro vamos validar:
	if validacao(sudoku) != "Sudoku válido.":
		return validacao(sudoku)
	#segundo vamos chamar as funções:
	opc = op(sudoku)
	qt_opc = qt_op(opc)
	if not("" in sudoku):
		return sudoku
	elif 0 in qt_opc:
		return "Sudoku impossível"
	elif 1 in qt_opc:
		#primeiro precisamos ver onde está o 1, pra isso serve o seguinte index:
		j = qt_opc.index(1)
		num = opc[j].pop() 
		#pop tira um aleatorio de um conjunto
		sudoku[j] = num
		if not("" in sudoku):
			return sudoku
		else:
			return resolversudoku(sudoku)
	else:
		#escreva(sudoku)
		k=salve(sudoku)
		minimo = min(qt_opc) # por isso que usamos aquele 1000
		j = qt_opc.index(minimo) #achar a posição do minimo
		min_op = opc[j]
		#vai ser o conjunto com as opções da entrada com menos opções
		b = min_op.pop()
		#pegamos um carinha aleatório entre as opções para tentar resolver o sudoku
		min_op -= {b}
		#tiramos o cara aleatorio porque, se não conseguirmos resolver o sudoku com ele, tentaremos com os outros caras
		sudoku[j] = b
		#o j antes era "", agora trocamos as aspas por b, que é um cara aleatório para tentar resolver com esse cara
		rvs = resolversudoku(sudoku)
		while type(rvs)==type("") and min_op!=set():
			#set() é conjunto vazio
			b = min_op.pop()
			min_op -= {b}
			sudoku[j] = b
			rvs = resolversudoku(sudoku)
			if type(rvs)!= type([ ]):
				sudoku=salve(k)
			else:
				return rvs
		return rvs

def getch(): #serve para podermos dar input sem precisar apertar enter
#essa função foi pega na internet.
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

fd = sys.stdin.fileno()
fl = fcntl.fcntl(fd, fcntl.F_GETFL)

def escreva(v): #função que printa bonitinho
	#os.system('clear')
	i=0
	lista=[]
	n=len(v)
	m=pow(n,1/2)
	q=pow(m,1/2)
	if type(v)==type(lista):
		print("┌",end="")
		l=0
		for j in range(int(q)):
			if l==0:
				print("—"*(int(q*3-1)),end="┬")
			elif l==int(q-1):
				print("—"*(int(q*3)),end="┐")
				print("")
				print("│",end="")
			else:
				print("—"*(int(q*3)),end="┬")
			l+=1	
		print("",end="")#até aqui printamos o cantinho de cima do sudoku __________________________________
		while i<n:
			if (i+1)%q!=0:
				if v[i]=="":
					print("#",end="  ")
				elif v[i]=="_":
					print("_",end="  ")
				else:		
					if int(v[i])<10:
						print(v[i],end="  ")
					else:
						print(v[i],end=" ")
			else:
				if v[i]=="":
					print("#",end=" ")
				elif v[i]=="_":
					print("_",end=" ")
				else:		
					if int(v[i])<10:
						print(v[i],end=" ")
					else:
						print(v[i],end="")
			if ((i+1)/m)%q==0 and i+1!=n:
				print("│")
				print("├",end="")
				l=0
				for j in range(int(q)):
					if l==0:
						print("—"*(int(q*3-1)),end="┼")
					elif l==int(q-1):
						print("—"*(int(q*3)),end="┤")
						print("")
						print("│",end="")
					else:
						print("—"*(int(q*3)),end="┼")
					l+=1	
				print("",end="")
			elif (i+1)%m==0 and (i+1)!=n:
				print("│")
				print("│",end="")
			elif (i+1)%q==0 and i+1!=n:
				print("│",end=" ")
			i+=1
		print("│")
		print("└",end="")
		l=0
		for j in range(int(q)):
			if l==0:
				print("—"*(int(q*3-1)),end="┴")
			elif l==int(q-1):
				print("—"*(int(q*3)),end="┘")
				print("")
			else:
				print("—"*(int(q*3)),end="┴")
			l+=1	
		print("",end="")
	else:
		print(v)
	print("\n")

def replace(v,i,j): #troca o elemento i com o elemento j do vetor v
	v[i],v[j]=v[j],v[i]

def digitev():
	print("\tResolver Sudoku\nDigite o tamanho do Sudoku:\n1. 4x4\n2. 9x9\n3. 16x16\n4. Voltar\n ")
	n=getch()
	if n=="1":
		n=2
	elif n=="2":
		n=3
	elif n=="3":
		n=4
	elif n=="4":
		os.system('cls' if os.name == 'nt' else 'clear')
		menu()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		return digitev()
	n=int(n)
	m=n**2
	n=m**2
	ns=[]
	for i in range(m):
		ns+=[str(i+1)]
	i=1
	u=["_"]
	while i<n:
		u+=[""]
		i+=1
	a=12355939
	k=0
	r=[]
	escreva(u)
	while a!="x":
		os.system('cls' if os.name == 'nt' else 'clear')
		escreva(u)
		if m==16:
			a=input()
		else:
			a=getch() #input sem dar enter
		if a=="d": #se aperta d vai pra direita
		#para "andar" pelo sudoku, em geral, permutamos duas entradas
			i=1
			while u[m*int(k/m)+(k+i)%m]!="" and i<n:
				i+=1
			replace(u,k,m*int(k/m)+(k+i)%m)
			k=m*int(k/m)+(k+i)%m
		elif a=="w":  #se aperta w vai pra cima
			i=m
			while u[(k-i)%n]!="" and i<4*n:
				i+=m
			replace(u,k,(k-i)%n)
			k=(k-i)%n
		elif a=="s": #se aperta s vai pra baixo
			i=m
			while u[(k+i)%n]!="" and i<4*n:
				i+=m
			replace(u,k,(k+i)%n)
			k=(k+i)%n
		elif a=="a":  #se aperta a vai pra esquerda
			i=1
			while u[m*int(k/m)+(k-i)%m]!="" and i<n:
				i+=1
			replace(u,k,m*int(k/m)+(k-i)%m)
			k=m*int(k/m)+(k-i)%m
		elif a in ns:
			if not "" in u:
				del u[k]
				u.insert(k,int(a))
				break
			i=k+1
			p=0
			while u[i%n]!="" and p<=n:
				i+=1
				p+=1
			replace(u,i%n,k%n)
			del u[k%n]
			u.insert(k%n,a)
			r+=[k%n]
			i,k=k,i
			k=k%n
		elif a=="r" and r!=[]:
			del u[r[-1]]
			u.insert(r[-1],"")
			del r[-1]
		elif a=="b":
			os.system('cls' if os.name == 'nt' else 'clear')
			return digitev()
	del u[k%n]
	u.insert(k%n,"")
	os.system('cls' if os.name == 'nt' else 'clear')
	escreva(u)
	return u


def jogar(u):
	n=len(u)
	m=int(n**(1/2))
	ns=[]
	for i in range(m):
		ns+=[str(i+1)]
	i=1
	k=0
	r=[]
	k=u.index("")
	u[k]="_"
	a=123
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		escreva(u)
		if m == 16:
			a=input()
		else:
			a=getch()
		if a=="d":
			i=1
			while u[(k+i)%n]!="" and i<n:
				i+=1
			replace(u,k,(k+i)%n)
			k=(k+i)%n
		elif a=="w":
			i=m
			while u[(k-i)%n]!="" and i<4*n:
				i+=m
			replace(u,k,(k-i)%n)
			k=(k-i)%n
		elif a=="s":
			i=m
			while u[(k+i)%n]!="" and i<4*n:
				i+=m
			replace(u,k,(k+i)%n)
			k=(k+i)%n
		elif a=="a":
			i=1
			while u[m*int(k/m)+(k-i)%m]!="" and i<n:
				i+=1
			replace(u,k,m*int(k/m)+(k-i)%m)
			k=m*int(k/m)+(k-i)%m
		elif a in ns:
			if not "" in u:
				del u[k]
				u.insert(k,int(a))
				os.system('cls' if os.name == 'nt' else 'clear')
				escreva(u)
				break
			i=k+1
			p=0
			while u[i%n]!="" and p<=n:
				i+=1
				p+=1
			replace(u,i%n,k%n)
			del u[k%n]
			u.insert(k%n,a)
			r+=[k%n]
			i,k=k,i
			k=k%n
		elif a=="r" and r!=[]:
			del u[r[-1]]
			u.insert(r[-1],"")
			del r[-1]
		elif a=="b":
			os.system('cls' if os.name == 'nt' else 'clear')
			return menu() 
	if validacao(u) != "Sudoku válido.":
		return validacao(u)
	else:
		return "Parabéns! Você conseguiu!!!!"

def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("	Menu\n1. Jogar\n2. Resolver sudoku\n3. Tutorial\n4. Sair\n ")
	escolha = getch()


	if escolha == "1":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\tJogar\nDigite o tamanho do sudoku:\n1. 4x4\n2. 9x9\n3. 16x16\n4. Voltar\n ")
		p = getch()
		while p not in {"1", "2", "3", "4"}:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("\tJogar\nDigite o tamanho do sudoku:\n1. 4x4\n2. 9x9\n3. 16x16\n4. Voltar\n ")
			p = getch()

		if p == "1":
			with open('Jogo 4x4.txt','r') as f:#abrir o arquivo com os jogos 4x4
				u=random.choice(f.readlines())#sortear uma linha (jogo) para jogar
				u=u.split()
				u = [k if k!="#" else "" for k in u]
				#del u[-1]#apareceu um "\n" no final, sei la o que é, mas tiramos ne
			print(jogar(u))
		elif p == "2":
			with open('Jogo 9x9.txt','r') as f:#abrir o arquivo com os jogos 9x9
				u=random.choice(f.readlines())#sortear uma linha (jogo) para jogar
				u=u.split()
				u = [k if k!="#" else "" for k in u]
				#del u[-1]#apareceu um "\n" no final, sei la o que é, mas tiramos ne
			print(jogar(u))
		elif p == "3":
			with open('Jogo 16x16.txt','r') as f:#abrir o arquivo com os jogos 16x16
				u=random.choice(f.readlines())#sortear uma linha (jogo) para jogar
				u=u.split()
				u = [k if k!="#" else "" for k in u]
				#del u[-1]#apareceu um "\n" no final, sei la o que é, mas tiramos ne
			print(jogar(u))
		elif p == "4":
			os.system('cls' if os.name == 'nt' else 'clear')
			menu()
		a = input("\nPressione enter para voltar para o menu.")
		os.system('cls' if os.name == 'nt' else 'clear')
		menu()



	elif escolha == "2":
		os.system('cls' if os.name == 'nt' else 'clear')#apaga a tela para recomeçar
		u = digitev()
		escreva(resolversudoku(u))
		a = input("Pressione enter para voltar. ")
		menu()

	elif escolha == "3":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\tTutorial\n\n1. Comandos:\n(a) esquerda\n(d) direita\n(w) cima\n(s) baixo\n(x) confirma\n(r) apaga\n(b) voltar\n\n2. Objetivos:\n A ideia do jogo é bem simples: No 9x9, por exemplo,\n completar todas as 81 células usando números de 1 a 9,\n sem repetir os números numa mesma linha, coluna ou grade (3x3).\n\n\nOBS.: Nos sudokus 4x4 e 9x9 não é necessário o uso do enter no input, \nporém, por motivos decimais, no 16x16 é preciso.\n")
		a = input("Pressione enter para voltar. ")
		menu()

	elif escolha == "4":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Tem certeza?\n1. Sim\n2. Não\n ")
		bla = getch()
		if bla == "1":
			os._exit(45)
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			menu()


	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		menu()

menu()

