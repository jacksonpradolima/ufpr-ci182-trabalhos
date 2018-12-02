def imprime_matriz(m):
 #Essa função ira imprimir as matrizes necessárias para a brincadeira acontecer.
    linha = len(m) # Número de linhas da matriz m
    coluna = len(m[0]) # Número de colunas da matriz m
     # Nas próximas linhas iremos percorrer todos os elementos da matriz para podermos imprimi-los em tela.
    for i in range(linha):
        for j in range(coluna):
            print(m[i][j], " ", end="")        
        print("\n")

# Mensagem inicial
print('''Olá usuário, vamos adivinhar a sua idade.
Para isso, responda apenas 's' para sim ou 'n' para não e tecle enter.
Preste muita atenção para não errar e deixar passar algum número!''')

# A seguir, iremos denotar as matrizes que serão utilizadas
m1 = [[1, 3, 5, 7, 9, 11, 13, 15],[17, 19, 21, 23, 25, 27, 29, 31],[33, 35, 37, 39, 41, 43, 45, 47],[49, 51, 53, 55, 57, 59, 61, 63]]
m2 = [[2, 3, 6, 7, 10, 11, 14, 15],[18, 19, 22, 23, 26, 27, 30, 31],[34, 35, 38, 39, 42, 43, 46, 47],[50, 51, 54, 55, 58, 59, 62, 63]]
m3 = [[4, 5, 6, 7, 12, 13, 14, 15],[20, 21, 22, 23, 28, 29, 30, 31],[36, 37, 38, 39, 44, 45, 46, 47],[52, 53, 54, 55, 60, 61, 62, 63]]
m4 = [[8, 9, 10, 11, 12, 13, 14, 15],[24, 25, 26, 27, 28, 29, 30, 31],[40, 41, 42, 43, 44, 45, 46, 47],[56, 57, 58, 59, 60, 61, 62, 63]]
m5 = [[16, 17, 18, 19, 20, 21, 22, 23],[24, 25, 26, 27, 28, 29, 30, 31],[48, 49, 50, 51, 52, 53, 54, 55],[56, 57, 58, 59, 60, 61, 62, 63]]
m6 = [[32, 33, 34, 35, 36, 37, 38, 39],[40, 41, 42, 43, 44, 45, 46, 47],[48, 49, 50, 51, 52, 53, 54, 55],[56, 57, 58, 59, 60, 61, 62, 63]]
answer_end="s" # Esse será nosso controle para entrarmos no laço de repetição e finalizarmos o programa no futuro
while answer_end!="n" or answer_end=="s": # laço de repetição para reiniciar a bricadeira.
	soma=0 # Variável para a idade
	imprime_matriz(m1) 
	# Imprimimos a primeira matriz para o usuário 
	answer = input("Sua idade está na tabela acima? ")
    #O usuário deverá procurar o número correspondente a sua idade na matriz
	#Caso o usuário digite algo diferente de "s" ou "n", ele acabará vindo para esse laço
	while not (answer=="s" or answer=="n"): 
		print("Por favor, responda a pergunta com s ou n.\n") 
		# Onde repassamos a informação de que as respostas devem ser da forma que desejamos
		answer=input("Sua idade está na tabela? ")
	# caso a resposta seja "s", iremos adicionar à variável "soma" o elemento que corresponde a posição [0][0] da matriz
	if answer=="s":
		soma+=1 
	print("\n\n\n")
	#caso a resposta seja "n", nada acontece 
	
	#Esse processo acabará se repetindo com todas as matrizes 
	
	imprime_matriz(m2)
	answer = input("Sua idade está na tabela acima? ")
	while not (answer=="s" or answer=="n"):
		print("Por favor, responda a pergunta com s ou n.\n")
		answer=input("Sua idade está nesta tabela? ")
	if answer=="s":
		soma+=2
	print("\n\n\n")
	
	imprime_matriz(m3)
	answer = input("Sua idade está na tabela acima? ")
	while not (answer=="s" or answer=="n"):
		print("Por favor, responda a pergunta com s ou n.\n")
		answer=input("Sua idade está nesta tabela? ")
	if answer=="s":
		soma+=4
	print("\n\n\n")
	
	imprime_matriz(m4)
	answer = input("Sua idade está na tabela acima? ")
	while not (answer=="s" or answer=="n"):
		print("Por favor, responda a pergunta com s ou n.\n")
		answer=input("Sua idade está nesta tabela? ")
	if answer=="s":
		soma+=8
	print("\n\n\n")
	
	imprime_matriz(m5)
	answer = input("Sua idade está na tabela acima? ")
	while not (answer=="s" or answer=="n"):
		print("Por favor, responda a pergunta com s ou n.\n")
		answer=input("Sua idade está nesta tabela? ")
	if answer=="s":
		soma+=16
	print("\n\n\n")

	imprime_matriz(m6)
	answer = input("Sua idade está na tabela acima? ")
	while not (answer=="s" or answer=="n"):
		print("Por favor, responda a pergunta com s ou n.\n")
		answer=input("Sua idade está nesta tabela? ")
	if answer=="s":
		soma+=32
	print("\n\n\n")
	
	# Aqui mostraremos para o usuário o resultado final da "soma" que corresponde ao número escolhido, junto a uma mensagem.
	print("Você tem {0} anos".format(soma)) 

	#O usuário pode escolher se deseja brincar novamente ou não.
	#Caso a resposta seja "s", voltamos ao primeiro laço de repetição.

	answer_end=input("Deseja fazer novamente? ")  
	while not (answer_end=="s" or answer_end=="n"): #respostas diferentes são redirecionadas 
		print("Por favor, responda a pergunta com s ou n.\n")
		answer_end=input("Deseja fazer novamente? ")

print("Agradecemos por usar o nosso programa.") # Caso seja "n", encerramos o programa.
