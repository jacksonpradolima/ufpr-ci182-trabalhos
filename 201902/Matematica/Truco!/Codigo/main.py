import random
import pydealer.tools
from truco_ranks import *
from pydealer.const import DEFAULT_RANKS

print("\n")
def bem_vindo():
    print("Bem vindo ao jogo do FODASE!!!")
    print("Caso você não conheça o jogo, segue as instruções abaixo!!!")


def instruções():
    print("Cartas disponíveis no baralho: A, 2, 3, 4, 5, 6, 7, Q, J e K")
    print("Naipes: Paus, Copas, Ourous e Espadas")
    print("A ordem dos naipes e dos valores das cartas segue do Truco!!!")
    print("Cada jogador deve informar a quantidade de jogos que faz!!!")
    print("OBSERVAÇÃO: A quantidade total de jogos não pode ser igual "
          "ao número de cartas da pessoa que tiver mais cartas.")
    print("A seleção de cartas deve ser feita digitando o valor que aparecer nas alternativas.")
    print("Só ganha ponto o jogador que fizer a quantidade de jogos que disse que faria!!!")

bem_vindo()
print("\n")
instruções()
print("\n")


#Definindo Jogadores
jogador = input("Digite seu nome: ")
P2 = "Player 2"
P3 = "Player 3"
P4 = "Player 4"
P5 = "Player 5"
print("\n")

placar = [0, 0, 0, 0, 0]
#Lista de jogadores
jogadores = ["Player 2", "Player 3", "Player 4", "Player 5", "Você"]


#Lista da ordem fixa de jogadores
ordem = ["Player 2", "Player 3", "Player 4", "Player 5", jogador]
#Listas das 5 ordens possiveis
ordem1 = ["Player 2", "Player 3", "Player 4", "Player 5", "Você"]
ordem2 = ["Player 3", "Player 4", "Player 5", "Voce", "Player 2"]
ordem3 = ["Player 4", "Player 5", "Você", "Player 2", "Player 3"]
ordem4 = ["Player 5", "Você", "Player 2", "Player 3", "Player 4"]
ordem5 = ["Voce", "Player 2", "Player 3", "Player 4", "Player 5"]

#Palpites a serem selecionados aleatoriamente pelos computadores
jogos = [ "0", "0", "0", "1", "1", "2", "1", "1", "0", "1", "0", "0", "1", "1", "0" ]

#Define o primeiro jogador e a ordem
primeiro = random.choice(ordem)
if primeiro == "Player 2":
    placar = [ 0, 0, 0, 0, 0 ]
    #Manten varias rodadas ate que alguem faça 5 pontos
    while placar [ 0 ] != 5 and placar [ 1 ] != 5 and placar [ 2 ] != 5 and placar [ 3 ] != 5 and placar [4] != 5 :
        #Pontos de cada jogador de cada rodada
        pontos = [ 0, 0, 0, 0, 0 ]
        print("O primeiro jogador a dizer quantos jogos faz é", primeiro)
        #Definindo o baralho tendo como ordem de valores e naipes as ordens padroes
        baralho = pydealer.Deck(ranks=DEFAULT_RANKS)
        print("\n")
        print("Embaralhando as cartas...\n")
        baralho.shuffle()
        print("Dando cartas...")
        print("\n")
        #Distribuindo 4 cartas para todos os jogadores
        P2 = baralho.deal(4)
        P3 = baralho.deal(4)
        P4 = baralho.deal(4)
        P5 = baralho.deal(4)
        voce = baralho.deal(4)
        #Transforma todos os jogadores (Stack) em listas para facilitaçao dos comandos
        voce = list(voce)
        P2 = list(P2)
        P3 = list(P3)
        P4 = list(P4)
        P5 = list(P5)
        #Define o Vira
        vira = baralho.deal(1)
        #Retorna o valor da carta na classe de Card
        valor = vira [ 0 ].value

        print("O vira é ")
        print(vira)
        print("\n")

        #Ordem padrao de valores e naipes
        ranking = DEFAULT_RANKS
        #Define o vira com base no valor da carta
        if valor == "4" :
                baralho = pydealer.Deck(ranks=RANK1)
                ranking = RANK1
        elif valor == "5" :
                ranking = RANK2
                baralho = pydealer.Deck(ranks=RANK2)
        elif valor == "6" :
            ranking = RANK3
            baralho = pydealer.Deck(ranks=RANK3)
        elif valor == "7" :
                ranking = RANK4
                baralho = pydealer.Deck(ranks=RANK4)
        elif valor == "Q" :
            ranking = RANK5
            baralho = pydealer.Deck(ranks=RANK5)
        elif valor == "J" :
                ranking = RANK6
                baralho = pydealer.Deck(ranks=RANK6)
        elif valor == "K" :
                ranking = RANK7
                baralho = pydealer.Deck(ranks=RANK7)
        elif valor == "A" :
                ranking = RANK8
                baralho = pydealer.Deck(ranks=RANK8)
        elif valor == "2" :
                ranking = RANK9
                baralho = pydealer.Deck(ranks=RANK9)
        else :
                ranking = RANK10
                baralho = pydealer.Deck(ranks=RANK10)
        #Formata na tela as opçoes de cartas e as cartas do usuario
        print("Suas cartas são: ")
        for i in range(len(voce)) :
            print("{0} - {1} ".format(str(i + 1), voce [ i ]))

        print("\n")
        #qnt = quantidade de cartas que cada jogador possui menos a sua
        qnt = [ len(P2), len(P3), len(P4), len(P5) ]
        #j = Os jogos que cada jogador diz que faria
        j = []
        #soma de todos os jogos
        soma = 0
        ordem = [ "Player 2", "Player 3", "Player 4", "Player 5" ]
        #Para cada jogador (computador) escolha na lista jogos a quantidade que cada um vai fazer e adiciona na lista j
        # e soma
        for k in range(len(ordem)) :
            numero = random.choice(jogos)
            print(ordem [ k ], " faz {}".format(numero))
            numero = int(numero)
            j.append(numero)
            soma += numero

        seus = int(input("Quantos jogos você faz? "))
        #Enquanto a soma fechar na 4 digite novamente um valor no qual a soma nao feche em 4
        while soma + seus == max(qnt) :
            print("Sua escolha tem que ser diferente de {}".format(max(qnt) - soma))
            seus = int(input("Quantos jogos você faz? "))

        j.append(seus)
        soma += seus
        print("\n")
        print("A quantidade de jogos fechou em", soma)
        print("\n")
        #Define as rodadas onde cada jogador ira jogar a sua carta
        rodada = 1
        #Como sao 4 rodadas criamos um laço ate dar 4
        while rodada < 5 :
            print("\n")
            print("Vira: ")
            print(vira)
            print("\n")

            print("Suas cartas são: ")
            for i in range(len(voce)) :
                print("{0} - {1} ".format(str(i + 1), voce [ i ]))

            print("Joguem suas cartas...\n")
            #Cada jogador sua uma carta que é removida da mao do mesmo
            carta_mesa2 = random.choice(P2)
            P2.remove(carta_mesa2)
            carta_mesa3 = random.choice(P3)
            P3.remove((carta_mesa3))
            carta_mesa4 = random.choice(P4)
            P4.remove(carta_mesa4)
            carta_mesa5 = random.choice(P5)
            P5.remove(carta_mesa5)
            #printa na tela as cartas jogadas
            print("Player 2 jogou ", carta_mesa2)
            print("Player 3 jogou ", carta_mesa3)
            print("Player 4 jogou ", carta_mesa4)
            print("Player 5 jogou ", carta_mesa5)

            print("\n")

            opção = int(input("Qual carta você escolhe? "))
            if opção == 1 :
                sua_carta = voce [ 0 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 2 :
                sua_carta = voce [ 1 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 3 :
                sua_carta = voce [ 2 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            else :
                sua_carta = voce [ 3 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)

            print("\n")
            #Usanmos a funçao .gt() que compara duas cartas se uma e maior que a outra
            #Se a carta do Player 2 for maior que todas entao Player dois ganha um ponto da rodada
            if carta_mesa2.gt(carta_mesa3, ranking) and carta_mesa2.gt(carta_mesa4, ranking) and carta_mesa2.gt(carta_mesa5, ranking) and carta_mesa2.gt(sua_carta, ranking) :
                print("Player 2 ganhou a rodada!")
                pontos[0] += 1

            elif carta_mesa3.gt(carta_mesa2, ranking) and carta_mesa3.gt(carta_mesa4, ranking) and carta_mesa3.gt(carta_mesa5, ranking) and carta_mesa3.gt(sua_carta, ranking) :
                print("Player 3 ganhou a rodada")
                pontos[1] += 1

            elif carta_mesa4.gt(carta_mesa2, ranking) and carta_mesa4.gt(carta_mesa3, ranking) and carta_mesa4.gt(carta_mesa5, ranking) and carta_mesa4.gt(sua_carta, ranking) :
                print("Player 4 ganhou a rodada!")
                pontos[2] += 1

            elif carta_mesa5.gt(carta_mesa2, ranking) and carta_mesa5.gt(carta_mesa3, ranking) and carta_mesa5.gt(carta_mesa4, ranking) and carta_mesa5.gt(sua_carta, ranking) :
                print("Player 5 ganhou a rodada!")
                pontos[3] += 1

            elif sua_carta.gt(carta_mesa2, ranking) and sua_carta.gt(carta_mesa4, ranking) and sua_carta.gt(carta_mesa3,ranking) and sua_carta.gt(carta_mesa5, ranking) :
                print("Você ganhou a rodada!")
                pontos[4] += 1

            print("\n")
            print("[P2, P3, P4, P5, {}]".format(jogador))
            print("Tabela de Jogos")
            print(j, "\n")
            print("Tabela de Jogos da Rodada")
            print(pontos, "\n")
            rodada += 1


        for k in range(5):
            if j[k] == pontos[k] and pontos[k]>0:
                placar[k] += pontos[k]
            elif j[k] != pontos[k]:
                placar[k] = placar[k]
            else:
                placar[k] += 1

        print("\n")
        print("O placar é:", placar)

elif primeiro == "Player 3":
    placar = [ 0, 0, 0, 0, 0 ]
    while placar [ 0 ] != 5 and placar [ 1 ] != 5 and placar [ 2 ] != 5 and placar [ 3 ] != 5 and placar [ 4 ] != 5 :
        pontos = [ 0, 0, 0, 0, 0 ]

        print("O primeiro jogador a dizer quantos jogos faz é", primeiro)
        baralho = pydealer.Deck(ranks=DEFAULT_RANKS)
        print("\n")
        print("Embaralhando as cartas...\n")
        baralho.shuffle()
        print("Dando cartas...")
        print("\n")

        P2 = baralho.deal(4)
        P3 = baralho.deal(4)
        P4 = baralho.deal(4)
        P5 = baralho.deal(4)
        voce = baralho.deal(4)

        voce = list(voce)
        P2 = list(P2)
        P3 = list(P3)
        P4 = list(P4)
        P5 = list(P5)

        vira = baralho.deal(1)
        valor = vira [ 0 ].value

        print("O vira é ")
        print(vira)
        print("\n")

        ranking = DEFAULT_RANKS
        if valor == "4" :
            baralho = pydealer.Deck(ranks=RANK1)
            ranking = RANK1
        elif valor == "5" :
            ranking = RANK2
            baralho = pydealer.Deck(ranks=RANK2)
        elif valor == "6" :
            ranking = RANK3
            baralho = pydealer.Deck(ranks=RANK3)
        elif valor == "7" :
            ranking = RANK4
            baralho = pydealer.Deck(ranks=RANK4)
        elif valor == "Q" :
            ranking = RANK5
            baralho = pydealer.Deck(ranks=RANK5)
        elif valor == "J" :
            ranking = RANK6
            baralho = pydealer.Deck(ranks=RANK6)
        elif valor == "K" :
            ranking = RANK7
            baralho = pydealer.Deck(ranks=RANK7)
        elif valor == "A" :
            ranking = RANK8
            baralho = pydealer.Deck(ranks=RANK8)
        elif valor == "2" :
            ranking = RANK9
            baralho = pydealer.Deck(ranks=RANK9)
        else :
            ranking = RANK10
            baralho = pydealer.Deck(ranks=RANK10)

        print("Suas cartas são: ")
        for i in range(len(voce)) :
            print("{0} - {1} ".format(str(i + 1), voce [ i ]))

        print("\n")

        qnt = [ len(P3), len(P4), len(P5), len(jogador) ]
        j = [ ]
        soma = 0
        #Diminuimos a quantidade de jogadores
        ordem = [ "Player 3", "Player 4", "Player 5"]
        #Para o jogador Player 3 e Player 4 escolha numeros aleatorio como visto anteriormente
        #Quando k = 2 pergunte ao usuario pois ele e o terceiro nesta ordem
        #Para o Player 5 segue igual ao outros
        for k in range(len(ordem)) :
            numero = random.choice(jogos)
            if ordem[k] == ordem[2] :
                seus = int(input("Quantos jogos você faz? "))
                soma += seus
                j.append(seus)
            print(ordem[k], " faz {}".format(numero))
            numero = int(numero)
            j.append(numero)
            soma += numero
        #Para o ultimo escolhe um numero aleatorio para a quantidade de jogos que ele ira fazer
        escolhap2 = random.choice(jogos)
        escolhap2 = int(escolhap2)
        #Restringindo como anteriormente so que enquanto ele escolher um numero cuja a soma fecha em 4, escolha novamente
        #Ate a soma ser != 4 ou de forma geral como explicado anteriomente
        while soma + escolhap2 == max(qnt):
            escolhap2 = random.choice(jogos)
            escolhap2 = int(escolhap2)
        print("Player 2 faz {}".format(escolhap2))
        j.append(escolhap2)
        soma += escolhap2
        print("\n")
        print("A quantidade de jogos fechou em", soma)
        print("\n")
        rodada = 1
        while rodada < 5 :
            print("\n")
            print("Vira: ")
            print(vira)
            print("\n")

            print("Suas cartas são: ")
            for i in range(len(voce)) :
                print("{0} - {1} ".format(str(i + 1), voce [ i ]))

            print("Joguem suas cartas...\n")

            carta_mesa2 = random.choice(P2)
            P2.remove(carta_mesa2)
            carta_mesa3 = random.choice(P3)
            P3.remove((carta_mesa3))
            carta_mesa4 = random.choice(P4)
            P4.remove(carta_mesa4)
            carta_mesa5 = random.choice(P5)
            P5.remove(carta_mesa5)

            print("Player 3 jogou ", carta_mesa3)
            print("Player 4 jogou ", carta_mesa4)
            print("Player 5 jogou ", carta_mesa5)
            opção = int(input("Qual carta você escolhe? "))
            if opção == 1 :
                sua_carta = voce [ 0 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 2 :
                sua_carta = voce [ 1 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 3 :
                sua_carta = voce [ 2 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            else :
                sua_carta = voce [ 3 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)

            print("Player 2 jogou ", carta_mesa2)
            print("\n")


            if carta_mesa2.gt(carta_mesa3, ranking) and carta_mesa2.gt(carta_mesa4, ranking) and carta_mesa2.gt(carta_mesa5, ranking) and carta_mesa2.gt(sua_carta, ranking) :
                print("Player 2 ganhou a rodada!")
                pontos[4] += 1

            elif carta_mesa3.gt(carta_mesa2, ranking) and carta_mesa3.gt(carta_mesa4, ranking) and carta_mesa3.gt(carta_mesa5, ranking) and carta_mesa3.gt(sua_carta, ranking) :
                print("Player 3 ganhou a rodada")
                pontos[0] += 1

            elif carta_mesa4.gt(carta_mesa2, ranking) and carta_mesa4.gt(carta_mesa3, ranking) and carta_mesa4.gt(carta_mesa5, ranking) and carta_mesa4.gt(sua_carta, ranking) :
                print("Player 4 ganhou a rodada!")
                pontos[1] += 1

            elif carta_mesa5.gt(carta_mesa2, ranking) and carta_mesa5.gt(carta_mesa3, ranking) and carta_mesa5.gt(carta_mesa4, ranking) and carta_mesa5.gt(sua_carta, ranking) :
                print("Player 5 ganhou a rodada!")
                pontos[2] += 1

            elif sua_carta.gt(carta_mesa2, ranking) and sua_carta.gt(carta_mesa4, ranking) and sua_carta.gt(carta_mesa3,ranking) and sua_carta.gt(carta_mesa5, ranking) :
                print("Você ganhou a rodada!")
                pontos[3] += 1

            print("\n")
            print("[P3, P4, P5, {}, P2]".format(jogador))
            print("Tabela de Jogos")
            print(j, "\n")
            print("Tabela de Jogos da Rodada")
            print(pontos, "\n")
            rodada += 1

        for k in range(5):
            if j[k] == pontos[k] and pontos[k]>0:
                placar[k] += pontos[k]
            elif j[k] != pontos[k]:
                placar[k] = placar[k]
            else:
                placar[k] += 1

        print("\n")
        print("O placar é:", placar)

elif primeiro == "Player 4":
    placar = [ 0, 0, 0, 0, 0 ]
    while placar [ 0 ] != 5 and placar [ 1 ] != 5 and placar [ 2 ] != 5 and placar [ 3 ] != 5 and placar [ 4 ] != 5 :
        pontos = [ 0, 0, 0, 0, 0 ]
        print("O primeiro jogador a dizer quantos jogos faz é", primeiro)
        baralho = pydealer.Deck(ranks=DEFAULT_RANKS)
        print("\n")
        print("Embaralhando as cartas...\n")
        baralho.shuffle()
        print("Dando cartas...")
        print("\n")

        P2 = baralho.deal(4)
        P3 = baralho.deal(4)
        P4 = baralho.deal(4)
        P5 = baralho.deal(4)
        voce = baralho.deal(4)

        voce = list(voce)
        P2 = list(P2)
        P3 = list(P3)
        P4 = list(P4)
        P5 = list(P5)

        vira = baralho.deal(1)
        valor = vira [ 0 ].value

        print("O vira é ")
        print(vira)
        print("\n")

        ranking = DEFAULT_RANKS
        if valor == "4" :
            baralho = pydealer.Deck(ranks=RANK1)
            ranking = RANK1
        elif valor == "5" :
            ranking = RANK2
            baralho = pydealer.Deck(ranks=RANK2)
        elif valor == "6" :
            ranking = RANK3
            baralho = pydealer.Deck(ranks=RANK3)
        elif valor == "7" :
            ranking = RANK4
            baralho = pydealer.Deck(ranks=RANK4)
        elif valor == "Q" :
            ranking = RANK5
            baralho = pydealer.Deck(ranks=RANK5)
        elif valor == "J" :
            ranking = RANK6
            baralho = pydealer.Deck(ranks=RANK6)
        elif valor == "K" :
            ranking = RANK7
            baralho = pydealer.Deck(ranks=RANK7)
        elif valor == "A" :
            ranking = RANK8
            baralho = pydealer.Deck(ranks=RANK8)
        elif valor == "2" :
            ranking = RANK9
            baralho = pydealer.Deck(ranks=RANK9)
        else :
            ranking = RANK10
            baralho = pydealer.Deck(ranks=RANK10)

        print("Suas cartas são: ")
        for i in range(len(voce)) :
            print("{0} - {1} ".format(str(i + 1), voce [ i ]))

        print("\n")

        qnt = [ len(P2), len(P3), len(P4), len(P5) ]
        j = [ ]
        soma = 0
        ordem = [ "Player 4", "Player 5", "Player 2"]
        for k in range(len(ordem)) :
            numero = random.choice(jogos)
            if ordem[k] == ordem[2] :
                seus = int(input("Quantos jogos você faz? "))
                soma += seus
                j.append(seus)
            print(ordem[k], " faz {}".format(numero))
            numero = int(numero)
            j.append(numero)
            soma += numero
        escolhap3 = random.choice(jogos)
        escolhap3 = int(escolhap3)
        while soma + escolhap3 == max(qnt):
            escolhap3 = random.choice(jogos)
            escolhap3 = int(escolhap3)

        j.append(escolhap3)
        soma += escolhap3
        print("Player 3 faz {}".format(escolhap3))
        print("\n")
        print("A quantidade de jogos fechou em", soma)
        print("\n")
        rodada = 1
        while rodada < 5 :
            print("\n")
            print("Vira: ")
            print(vira)
            print("\n")

            print("Suas cartas são: ")
            for i in range(len(voce)) :
                print("{0} - {1} ".format(str(i + 1), voce [ i ]))

            print("Joguem suas cartas...\n")

            carta_mesa2 = random.choice(P2)
            P2.remove(carta_mesa2)
            carta_mesa3 = random.choice(P3)
            P3.remove((carta_mesa3))
            carta_mesa4 = random.choice(P4)
            P4.remove(carta_mesa4)
            carta_mesa5 = random.choice(P5)
            P5.remove(carta_mesa5)

            print("Player 4 jogou ", carta_mesa4)
            print("Player 5 jogou ", carta_mesa5)
            opção = int(input("Qual carta você escolhe? "))
            if opção == 1 :
                sua_carta = voce [ 0 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 2 :
                sua_carta = voce [ 1 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 3 :
                sua_carta = voce [ 2 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            else :
                sua_carta = voce [ 3 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)

            print("Player 2 jogou ", carta_mesa2)
            print("Player 3 jogou ", carta_mesa3)
            print("\n")

            if carta_mesa2.gt(carta_mesa3, ranking) and carta_mesa2.gt(carta_mesa4, ranking) and carta_mesa2.gt(carta_mesa5, ranking) and carta_mesa2.gt(sua_carta, ranking) :
                print("Player 2 ganhou a rodada!")
                pontos[3] += 1

            elif carta_mesa3.gt(carta_mesa2, ranking) and carta_mesa3.gt(carta_mesa4, ranking) and carta_mesa3.gt(carta_mesa5, ranking) and carta_mesa3.gt(sua_carta, ranking) :
                print("Player 3 ganhou a rodada")
                pontos[4] += 1

            elif carta_mesa4.gt(carta_mesa2, ranking) and carta_mesa4.gt(carta_mesa3, ranking) and carta_mesa4.gt(carta_mesa5, ranking) and carta_mesa4.gt(sua_carta, ranking) :
                print("Player 4 ganhou a rodada!")
                pontos[0] += 1

            elif carta_mesa5.gt(carta_mesa2, ranking) and carta_mesa5.gt(carta_mesa3, ranking) and carta_mesa5.gt(carta_mesa4, ranking) and carta_mesa5.gt(sua_carta, ranking) :
                print("Player 5 ganhou a rodada!")
                pontos[1] += 1

            elif sua_carta.gt(carta_mesa2, ranking) and sua_carta.gt(carta_mesa4, ranking) and sua_carta.gt(carta_mesa3,ranking) and sua_carta.gt(carta_mesa5, ranking) :
                print("Você ganhou a rodada!")
                pontos[2] += 1

            print("\n")
            print("[P4, P5, {}, P2, P3]".format(jogador))
            print("Tabela de Jogos")
            print(j, "\n")
            print("Tabela de Jogos da Rodada")
            print(pontos, "\n")
            rodada += 1

        for k in range(5) :
            if j [ k ] == pontos [ k ] and pontos [ k ] > 0 :
                placar [ k ] += pontos [ k ]
            elif j [ k ] != pontos [ k ] :
                placar [ k ] = placar [ k ]
            else :
                placar [ k ] += 1

        print("\n")
        print("O placar é:", placar)

elif primeiro == "Player 5" :
    placar = [ 0, 0, 0, 0, 0 ]
    while placar [ 0 ] != 5 and placar [ 1 ] != 5 and placar [ 2 ] != 5 and placar [ 3 ] != 5 and placar [ 4 ] != 5 :
        pontos = [ 0, 0, 0, 0, 0 ]
        print("O primeiro jogador a dizer quantos jogos faz é", primeiro)
        baralho = pydealer.Deck(ranks=DEFAULT_RANKS)
        print("\n")
        print("Embaralhando as cartas...\n")
        baralho.shuffle()
        print("Dando cartas...")
        print("\n")

        P2 = baralho.deal(4)
        P3 = baralho.deal(4)
        P4 = baralho.deal(4)
        P5 = baralho.deal(4)
        voce = baralho.deal(4)

        voce = list(voce)
        P2 = list(P2)
        P3 = list(P3)
        P4 = list(P4)
        P5 = list(P5)

        vira = baralho.deal(1)
        valor = vira [ 0 ].value

        print("O vira é ")
        print(vira)
        print("\n")

        ranking = DEFAULT_RANKS
        if valor == "4" :
            baralho = pydealer.Deck(ranks=RANK1)
            ranking = RANK1
        elif valor == "5" :
            ranking = RANK2
            baralho = pydealer.Deck(ranks=RANK2)
        elif valor == "6" :
            ranking = RANK3
            baralho = pydealer.Deck(ranks=RANK3)
        elif valor == "7" :
            ranking = RANK4
            baralho = pydealer.Deck(ranks=RANK4)
        elif valor == "Q" :
            ranking = RANK5
            baralho = pydealer.Deck(ranks=RANK5)
        elif valor == "J" :
            ranking = RANK6
            baralho = pydealer.Deck(ranks=RANK6)
        elif valor == "K" :
            ranking = RANK7
            baralho = pydealer.Deck(ranks=RANK7)
        elif valor == "A" :
            ranking = RANK8
            baralho = pydealer.Deck(ranks=RANK8)
        elif valor == "2" :
            ranking = RANK9
            baralho = pydealer.Deck(ranks=RANK9)
        else :
            ranking = RANK10
            baralho = pydealer.Deck(ranks=RANK10)

        print("Suas cartas são: ")
        for i in range(len(voce)) :
            print("{0} - {1} ".format(str(i + 1), voce [ i ]))

        print("\n")

        qnt = [ len(P2), len(P3), len(P4), len(P5) ]
        j = [ ]
        soma = 0
        ordem = [ "Player 5", "Player 2", "Player 3" ]
        for k in range(len(ordem)) :
            numero = random.choice(jogos)
            if ordem [ k ] == ordem [ 1 ] :
                seus = int(input("Quantos jogos você faz? "))
                soma += seus
                j.append(seus)
            print(ordem [ k ], " faz {}".format(numero))
            numero = int(numero)
            j.append(numero)
            soma += numero
        escolhap4 = random.choice(jogos)
        escolhap4 = int(escolhap4)
        while soma + escolhap4 == max(qnt) :
            escolhap4 = random.choice(jogos)
            escolhap4 = int(escolhap4)

        j.append(escolhap4)
        soma += escolhap4
        print("Player 4 faz {}".format(escolhap4))
        print("\n")
        print("A quantidade de jogos fechou em", soma)
        print("\n")

        rodada = 1
        while rodada < 5 :
            print("\n")
            print("Vira: ")
            print(vira)
            print("\n")

            print("Suas cartas são: ")
            for i in range(len(voce)) :
                print("{0} - {1} ".format(str(i + 1), voce [ i ]))

            print("Joguem suas cartas...\n")

            carta_mesa2 = random.choice(P2)
            P2.remove(carta_mesa2)
            carta_mesa3 = random.choice(P3)
            P3.remove((carta_mesa3))
            carta_mesa4 = random.choice(P4)
            P4.remove(carta_mesa4)
            carta_mesa5 = random.choice(P5)
            P5.remove(carta_mesa5)

            print("Player 5 jogou ", carta_mesa5)
            opção = int(input("Qual carta você escolhe? "))
            if opção == 1 :
                sua_carta = voce [ 0 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 2 :
                sua_carta = voce [ 1 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 3 :
                sua_carta = voce [ 2 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            else :
                sua_carta = voce [ 3 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)

            print("Player 2 jogou ", carta_mesa2)
            print("Player 3 jogou ", carta_mesa3)
            print("Player 4 jogou ", carta_mesa4)
            print("\n")
            if carta_mesa2.gt(carta_mesa3, ranking) and carta_mesa2.gt(carta_mesa4, ranking) and carta_mesa2.gt(
                    carta_mesa5, ranking) and carta_mesa2.gt(sua_carta, ranking) :
                print("Player 2 ganhou a rodada!")
                pontos [ 2 ] += 1

            elif carta_mesa3.gt(carta_mesa2, ranking) and carta_mesa3.gt(carta_mesa4, ranking) and carta_mesa3.gt(
                    carta_mesa5, ranking) and carta_mesa3.gt(sua_carta, ranking) :
                print("Player 3 ganhou a rodada")
                pontos [ 3 ] += 1

            elif carta_mesa4.gt(carta_mesa2, ranking) and carta_mesa4.gt(carta_mesa3, ranking) and carta_mesa4.gt(
                    carta_mesa5, ranking) and carta_mesa4.gt(sua_carta, ranking) :
                print("Player 4 ganhou a rodada!")
                pontos [ 4 ] += 1

            elif carta_mesa5.gt(carta_mesa2, ranking) and carta_mesa5.gt(carta_mesa3, ranking) and carta_mesa5.gt(
                    carta_mesa4, ranking) and carta_mesa5.gt(sua_carta, ranking) :
                print("Player 5 ganhou a rodada!")
                pontos [ 0 ] += 1

            elif sua_carta.gt(carta_mesa2, ranking) and sua_carta.gt(carta_mesa4, ranking) and sua_carta.gt(carta_mesa3,
                                                                                                            ranking) and sua_carta.gt(
                    carta_mesa5, ranking) :
                print("Você ganhou a rodada!")
                pontos [ 1 ] += 1

            print("\n")
            print("[P5, {}, P2, P3, P4]".format(jogador))
            print("Tabela de Jogos")
            print(j, "\n")
            print("Tabela de Jogos da Rodada")
            print(pontos, "\n")
            rodada += 1

        for k in range(5) :
            if j [ k ] == pontos [ k ] and pontos [ k ] > 0 :
                placar [ k ] += pontos [ k ]
            elif j [ k ] != pontos [ k ] :
                placar [ k ] = placar [ k ]
            else :
                placar [ k ] += 1

        print("\n")
        print("O placar é:", placar)

else:
    placar = [ 0, 0, 0, 0, 0 ]
    while placar [ 0 ] != 5 and placar [ 1 ] != 5 and placar [ 2 ] != 5 and placar [ 3 ] != 5 and placar [ 4 ] != 5 :
        pontos = [ 0, 0, 0, 0, 0 ]
        print("O primeiro jogador a dizer quantos jogos faz é", primeiro)
        baralho = pydealer.Deck(ranks=DEFAULT_RANKS)
        print("\n")
        print("Embaralhando as cartas...\n")
        baralho.shuffle()
        print("Dando cartas...")
        print("\n")

        P2 = baralho.deal(4)
        P3 = baralho.deal(4)
        P4 = baralho.deal(4)
        P5 = baralho.deal(4)
        voce = baralho.deal(4)

        voce = list(voce)
        P2 = list(P2)
        P3 = list(P3)
        P4 = list(P4)
        P5 = list(P5)

        vira = baralho.deal(1)
        valor = vira [ 0 ].value

        print("O vira é ")
        print(vira)
        print("\n")

        ranking = DEFAULT_RANKS
        if valor == "4" :
            baralho = pydealer.Deck(ranks=RANK1)
            ranking = RANK1
        elif valor == "5" :
            ranking = RANK2
            baralho = pydealer.Deck(ranks=RANK2)
        elif valor == "6" :
            ranking = RANK3
            baralho = pydealer.Deck(ranks=RANK3)
        elif valor == "7" :
            ranking = RANK4
            baralho = pydealer.Deck(ranks=RANK4)
        elif valor == "Q" :
            ranking = RANK5
            baralho = pydealer.Deck(ranks=RANK5)
        elif valor == "J" :
            ranking = RANK6
            baralho = pydealer.Deck(ranks=RANK6)
        elif valor == "K" :
            ranking = RANK7
            baralho = pydealer.Deck(ranks=RANK7)
        elif valor == "A" :
            ranking = RANK8
            baralho = pydealer.Deck(ranks=RANK8)
        elif valor == "2" :
            ranking = RANK9
            baralho = pydealer.Deck(ranks=RANK9)
        else :
            ranking = RANK10
            baralho = pydealer.Deck(ranks=RANK10)

        print("Suas cartas são: ")
        for i in range(len(voce)) :
            print("{0} - {1} ".format(str(i + 1), voce [ i ]))

        print("\n")

        qnt = [ len(P2), len(P3), len(P4), len(P5) ]
        j = [ ]
        soma = 0
        ordem = [ "Player 2", "Player 3", "Player 4" ]
        seus = int(input("Quantos jogos você faz? "))
        soma += seus
        j.append(seus)
        for k in range(len(ordem)) :
            numero = random.choice(jogos)
            print(ordem [ k ], " faz {}".format(numero))
            numero = int(numero)
            j.append(numero)
            soma += numero
        escolhap5 = random.choice(jogos)
        escolhap5 = int(escolhap5)
        while soma + escolhap5 == max(qnt) :
            escolhap5 = random.choice(jogos)
            escolhap5 = int(escolhap5)

        j.append(escolhap5)
        soma += escolhap5
        print("Player 5 faz {}".format(escolhap5))
        print("\n")
        print("A quantidade de jogos fechou em", soma)
        print("\n")
        rodada = 1
        while rodada < 5 :
            print("\n")
            print("Vira: ")
            print(vira)
            print("\n")

            print("Suas cartas são: ")
            for i in range(len(voce)) :
                print("{0} - {1} ".format(str(i + 1), voce [ i ]))

            print("Joguem suas cartas...\n")

            carta_mesa2 = random.choice(P2)
            P2.remove(carta_mesa2)
            carta_mesa3 = random.choice(P3)
            P3.remove((carta_mesa3))
            carta_mesa4 = random.choice(P4)
            P4.remove(carta_mesa4)
            carta_mesa5 = random.choice(P5)
            P5.remove(carta_mesa5)
            opção = int(input("Qual carta você escolhe? "))
            if opção == 1 :
                sua_carta = voce [ 0 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 2 :
                sua_carta = voce [ 1 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            elif opção == 3 :
                sua_carta = voce [ 2 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            else :
                sua_carta = voce [ 3 ]
                voce.remove(sua_carta)
                print(jogador, "jogou ", sua_carta)
            print("Player 2 jogou ", carta_mesa2)
            print("Player 3 jogou ", carta_mesa3)
            print("Player 4 jogou ", carta_mesa4)
            print("Player 5 jogou ", carta_mesa5)
            print("\n")
            if carta_mesa2.gt(carta_mesa3, ranking) and carta_mesa2.gt(carta_mesa4, ranking) and carta_mesa2.gt(
                    carta_mesa5, ranking) and carta_mesa2.gt(sua_carta, ranking) :
                print("Player 2 ganhou a rodada!")
                pontos [ 1 ] += 1

            elif carta_mesa3.gt(carta_mesa2, ranking) and carta_mesa3.gt(carta_mesa4, ranking) and carta_mesa3.gt(
                    carta_mesa5, ranking) and carta_mesa3.gt(sua_carta, ranking) :
                print("Player 3 ganhou a rodada")
                pontos [ 2 ] += 1

            elif carta_mesa4.gt(carta_mesa2, ranking) and carta_mesa4.gt(carta_mesa3, ranking) and carta_mesa4.gt(
                    carta_mesa5, ranking) and carta_mesa4.gt(sua_carta, ranking) :
                print("Player 4 ganhou a rodada!")
                pontos [ 3 ] += 1

            elif carta_mesa5.gt(carta_mesa2, ranking) and carta_mesa5.gt(carta_mesa3, ranking) and carta_mesa5.gt(
                    carta_mesa4, ranking) and carta_mesa5.gt(sua_carta, ranking) :
                print("Player 5 ganhou a rodada!")
                pontos [ 4 ] += 1

            elif sua_carta.gt(carta_mesa2, ranking) and sua_carta.gt(carta_mesa4, ranking) and sua_carta.gt(carta_mesa3,
                                                                                                            ranking) and sua_carta.gt(
                carta_mesa5, ranking) :
                print("Você ganhou a rodada!")
                pontos [ 0 ] += 1

            print("\n")
            print("[{}, P2, P3, P4, P5]".format(jogador))
            print("Tabela de Jogos")
            print(j, "\n")
            print("Tabela de Jogos da Rodada")
            print(pontos, "\n")
            rodada += 1

        for k in range(5) :
            if j [ k ] == pontos [ k ] and pontos [ k ] > 0 :
                placar [ k ] += pontos [ k ]
            elif j [ k ] != pontos [ k ] :
                placar [ k ] = placar [ k ]
            else :
                placar [ k ] += 1

        print("\n")
        print("O placar é:", placar)

#Printando o vencedor dependendo da ordem definida anteriormente
for i in range(len(placar)):
    if primeiro == "Player 2":
        if placar[i] == 5:
            #Printa o jogador na respectiva ordem do jogo
            print("O vencedor é", ordem[i])
    elif primeiro == "Player 3":
        if placar[i] == 5:
            print("O vencedor é", ordem2[i])
    elif primeiro == "Player 4":
        if placar[i] == 5:
            print("O vencedor é", ordem3[i])
    elif primeiro == "Player 5":
        if placar[i] == 5:
            print("O vencedor é", ordem4[i])
    else:
        if placar[i] == 5:
            print("O vencedor é", ordem5[i])












