acervo=[]#lista que vai guardar o "acervo" da biblioteca, a ser inserido pelo usuário
nome=(str(input("Insira seu nome:")))
GRR=(str(input("GRR (Apenas números):")))
classe=(str(input("Você é (G para Graduando, M para Mestre ou D para Doutor):")))
usuario=[]#lista de livros sob posse do usuario
print("Bem vindo(a) "+nome)#menu
print("\t 1 - Inserir uma Obra")
print("\t 2 - Procurar  e Alugar uma Obra do Acervo")
print("\t 3 - Renovar Empréstimo")
print("\t 4 - Sair")
opçao=int(input("Digite a Opção Desejada:"))#permite ao usuário escolher o que quer fazer
while opçao != 4:#valida se o usuário quer continuar usando o programa
    if opçao==1:#se selecionou a opção 1
        c=0#contador
        n=int(input("Número de Obras a serem inseridas:"))
        while c<n:#verifica se já foram inseridas o numero de obras informado pelo usuario
            novaobra=[]#lista que vai armazenar os dados da obra a entrar no acervo
            tipo=str(input("Tipo da Obra (L para Livro, P para Periódico):"))
            if tipo=='L':#se livro:
                titulo=str(input("Título:"))
                novaobra.append(titulo)#append pra colocar cada um dos dados do livro na lista nova obra
                autor=str(input("Autor(es):"))
                novaobra.append(autor)
                ano=int(input("Ano de Publicação:"))
                novaobra.append(ano)
                editora=str(input("Editora:"))
                novaobra.append(editora)
                nexemplares=int(input("Número de exemplares:"))
                novaobra.append(nexemplares)
                acervo.append(novaobra)#coloca a lista com os dados do livro dentro do acervo da biblioteca
                c=c+1#conta que um livro já foi
            elif tipo=='P':#se periódico:
                titulo=str(input("Título:"))#mesmo coisa que encima, só que com os dados de periódico
                novaobra.append(titulo)
                volume=int(input("Volume:"))
                novaobra.append(volume)
                mes=int(input("Mês(apenas números):"))
                novaobra.append(mes)
                ano=int(input("Ano de Publicação:"))
                novaobra.append(ano)
                nexemplares=int(input("Número de exemplares:"))
                novaobra.append(nexemplares)
                acervo.append(novaobra)#coloca os dados do periodico no acervo
                c=c+1#conta que um periodico já foi
            else:#caso a pessoa digite um tipo de obra inválido
                print("Erro - Tipo da Obra Inválido! Tente novamente.")
    elif opçao==2:#se a opção escolhida for a 2
        tipo=str(input("Tipo de Obra (L para Livro, P para Periódico):"))
        if tipo=='L':#livro
            titulo=str(input("Digite o título (x para não sei):"))#possibilidade de buscar pelo autor
            if titulo=='x':
                autor=str(input("Digite o autor:"))
                i=0
                while i<=(len(acervo)):#vai verificar todas as obras (i) na posição 1 (que contém os autores)
                    if (acervo[i][1])==autor:#se o autor bater com o da obra
                        print(str(acervo[i][0])+" possui "+str(acervo[i][4])+" exemplares.")#exibe o nome da obra e quantos exemplares tem
                        usuario.append(acervo[i][0])#coloca a obra na lista do usuário
                        print("Livro Alugado com Sucesso")
                        break#encerra o laço de busca
                    else:
                        i=i=1#vai para a próxima obra caso não tenha encontrado o autor
            else:
                i=0
                while i<=(len(acervo)):#faz a busca por título
                    if (acervo[i][0])==titulo:#titulo se encontra na posição 0, busca em todas as obras
                        print(str(acervo[i][0])+" possui "+str(acervo[i][4])+" exemplares.")#print composto
                        usuario.append(acervo[i][0])#coloca na lista do usuário
                        print("Livro Alugado com Sucesso")
                        break#termina a busca
                    else:
                        i=i=1#manda comparar com a próxima obra
        elif tipo=='P':
            titulo=str(input("Digite o título:"))#faz a busca por titulo em periódicos, semelhante à acima
            i=0
            while i<=(len(acervo)):
                if (acervo[i][0])==titulo:
                    print(str(acervo[i][0])+" possui "+str(acervo[i][4])+" exemplares.")
                    usuario.append(acervo[i][0])
                    print("Livro Alugado com Sucesso")
                    break
                else:
                    i=i=1
        else:
            print("Tipo de Obra Inválida. Por Favor Tente de Novo.")#caso não seja digitado l ou p
    elif opçao==3:# opção 3
        if classe=='G':#para graduando
            print(usuario)#mostra a lista de livros que a pessoa tem alugados
            obra=(str(input("Qual obra das acima você quer renovar?")))
            if obra in usuario:#verifica se a obra realmente já foi alugada
                numero_emprestimos=usuario.count(obra)#conta se não foi renovada mais vezes (cada renovação adiciona novamente o livro na lista do usuário)
                if numero_emprestimos<=3:#se não tiver atingido o limite de aluguéis
                    usuario.append(obra)#coloca mais uma vez na lista do usuário
                    print("Renovado! Você terá mais 10 dias a partir de hoje!")#print com prazo
                else:
                    print("Você não pode mais renovar essa obra, pois já renovou 3 vezes.")#caso já tenha chegado ao limite
            else:
                print("Você não alugou esta obra, impossível renovar. Acesse opção 2.")#caso a obra não esteja na lista do usuário
        elif classe=='M':#funcionamento igual ao de cima, apenas com 15 dias por ser um mestre
            print(usuario)
            obra=(str(input("Qual obra das acima você quer renovar?")))
            numero_emprestimos=usuario.count(obra)
            if obra in usuario:
                if numero_emprestimos<=3:
                    usuario.append(obra)
                    print("Renovado! Você terá mais 15 dias a partir de hoje!")
                else:
                    print("Você não pode mais renovar essa obra, pois já renovou 3 vezes.")
            else:
                print("Você não alugou esta obra, impossível renovar. Acesse opção 2.")
        elif classe=='D':#funcionamento igual ao primeiro, apenas com 20 dias por ser doutor
            print(usuario)
            obra=(str(input("Qual obra das acima você quer renovar?")))
            if obra in usuario:
                numero_emprestimos=usuario.count(obra)
                if numero_emprestimos<=3:
                    usuario.append(obra)
                    print("Renovado! Você terá mais 20 dias a partir de hoje!")
                else:
                    print("Você não pode mais renovar essa obra, pois já renovou 3 vezes.")
            else:
                print("Você não alugou esta obra, impossível renovar. Acesse opção 2.")
        else:
            print("Classe Inválida. Favor Inserir Nova.")#caso o usuário tenha digitado errado, permite mudar a "classe", pra renovar é só acessar a opção de renovação de novo
            classe=(str(input("Você é (G para Graduando, M para Mestre ou D para Doutor):")))
    else:
        print("Opção Inválida! Tente Novamente.")#opção errada, outra que não seja 1,2,3 ou 4
    print("\t 1 - Inserir uma Obra")#apresenta o menu novamente
    print("\t 2 - Procurar  e Alugar uma Obra do Acervo")
    print("\t 3 - Renovar Empréstimo")
    print("\t 4 - Sair")
    opçao=int(input("Digite a Opção Desejada:"))#permite continuar no sistema, até digitar 4, que invalida o while inicial e encerra o programa
