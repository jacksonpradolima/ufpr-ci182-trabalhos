import os
import random
class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.progresso = "  " 

    def aumenta_pontos_progresso(self):
        self.progresso = self.progresso + "#"
        self.pontos = self.pontos + 1
    def diminui_pontos_progresso(self):
        if self.pontos >0:
            self.pontos = self.pontos - 1
            self.progresso = "#" * self.pontos


def imprime_barra():
    print("-"*40)
    print("PONTUAÇÃO \n")
    for i in range(num_jog):
        print(jogadores[i].nome," ",jogadores[i].progresso)
        print("\n")
    print("-"*40)
      
jogadores=[]
perguntas = []
azar = []
sorte = []

#Para cada "verdadeiro" dará um passo, indicando que é privilegiado.
perguntas.append("Você estudou em colégio particular durante maior parte da sua vida. ")
perguntas.append("Você não depende de transporte público. ")
perguntas.append("Sempre morou com seus pais até ser capaz de se sustentar. ")
perguntas.append("Sua família esteve presente em sua infância e adolescência. ")
perguntas.append("Sua casa nunca encheu de água ou nunca perdeu algum bem por morar em área de risco. ")
perguntas.append("Nunca ouviu piadas por conta da cor da sua pele ou tipo de cabelo. ")
perguntas.append("Tem sua liberdade de ir e vir sem medo de sofrer abuso ou violência sexual. ")
perguntas.append("Você nunca recebeu um diagnóstico de doença mental ou física. ")
perguntas.append("Você nunca passou fome na vida. ")
perguntas.append("Você nunca precisou ajudar seus pais a pagar as contas de casa. ")

#Ações de azar que podem acontecer.
azar.append("Você acabou de perder o emprego.")
azar.append("Uma pessoa que você ama morreu.")
azar.append("Você está com uma doença que não tem cura.")
azar.append("Sua casa foi assaltada. Você perdeu tudo que tinha.")
azar.append("As pessoas não querem ficar com você por causa da cor da sua pele.")

#Ações de sorte que podem acontecer.
sorte.append("Você acabou de ser promovido no emprego. Sua renda subiu.")
sorte.append("Você ganhou na loteria. Parabéns!")
sorte.append("Você acabou de ser curado. Vai viver por mais tempo.")
sorte.append("Você vai conseguir pagar seu aluguel. Não vai ser despejado.")
sorte.append("Você encontrou o amor da sua vida.")
bk=0

#PROGRAMA PRINCIPAL
while True:
    print("OLÁ, BEM-VINDO(A) AO JOGO DOS PRIVILÉGIOS!")
    print('-'*40)
    print("INSTRUÇÕES:")
    print("1. Afirmações surgirão na tela e você deve responder de acordo com a sua realidade.")
    print("2. Responda \"V\" se a afirmação for verdadeira, ou \"F\" se for falso.")
    print("3. Para cada resposta você poderá ganhar um ponto ou nenhum.")
    print("4. A pontuação será indicado por \"#\".")
    print("5. É permitido mais de um jogador ao mesmo tempo.")
    print('-'*40)
    print("\n")
    num_jog = int(input("Quantos jogadores? "))
    for i in range(num_jog):
        print("Nome do jogador ",i+1,":")
        nome_jog = input("")
        jogadores.append(Jogador(nome_jog))

    print("Vamos começar!")
    for i in range(len(perguntas)):
        input("Pressione enter para continuar...")
        print("\n")
        os.system("cls")
        imprime_barra()
        for j in range(len(jogadores)):
            print(jogadores[j].nome, ", responda (V)erdadeiro ou (F)also: ")
            resp = input(perguntas[i]).lower()
            if resp == 'v':
                jogadores[j].aumenta_pontos_progresso()
                if jogadores[j].pontos == (len(perguntas)-2):
                    imprime_barra()
                    print("*"*5, jogadores[j].nome, "você completou o jogo.", "*"*5)
                    print("Isso significa que, por fatores que em sua maioria não dependeram de você, você venceu. \n Os demais jogadores nao tiveram a mesma sorte.")
                    print("Não seria melhor se todos pudessem ganhar juntos?")
                    print("-"*40)
                    print("PONTUAÇÃO FINAL:")
                    for p in range(len(jogadores)):
                        print(jogadores[p].nome, ": ", jogadores[p].pontos)
                    print("")
                    #colocar quantos pontos a pessoa fez print(jogadores[j].pontos)
                    bk = 1

                    break
        if bk ==1:
            break
        elif random.choice([True, True, False,False,False,False,False,False,False,False]):
            r = random.randint(0,len(jogadores)-1)
            s = random.randint(0,1)
            print("\n")
            print(jogadores[r].nome,", na vida acontecem situações que não temos controle... \n ")
            if s == 1:
                print("*"*5, "SORTE!", "*"*5)
                t = random.randint(0,len(sorte)-1)
                print(sorte[t]) 
                jogadores[r].aumenta_pontos_progresso()
                
                
            elif s == 0:
                print("*"*5, "AZAR!", "*"*5)
                t = random.randint(0,len(azar)-1)
                print(azar[t])
                jogadores[r].diminui_pontos_progresso()
            

    aux = input("Querem jogar novamente: (s)im ou (n)ão?").lower()
    if aux == "n":
        os.system("cls")
        print("Adeus!")
        break 
    elif aux == "s":
        jogadores = []
        input("Pressione enter para continuar...")
        os.system("cls")

