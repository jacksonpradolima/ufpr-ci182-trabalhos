# DEFINIÇÃO DOS TEMAS E LISTAS DE CADA TEMA
import random  # BIBLIOTECA QUE SELECIONA ITENS ALEATÓRIOS DE UMA LISTA
tema = int(input("""Digite o número referente ao tema escolhido:
Frutas - 1
Animais - 2
Cores - 3
Países - 4
Personagens - 5
>"""))

senha = 0
if tema == 1:
    senha = random.choice(["melancia", "banana", "laranja", "abacaxi",
                           "kiwi", "cereja", "lichia", "tomate", "uva", "abacate"])
elif tema == 2:
    senha = random.choice(["cachorro", "tartaruga", "cavalo", "vaca",
                           "elefante", "girafa", "cabra", "pinguim", "cobra", "gato"])
elif tema == 3:
    senha = random.choice(["rosa", "verde", "vermelho", "amarelo",
                           "azul", "roxo", "branco", "preto", "marrom", "cinza"])
elif tema == 4:
    senha = random.choice(["brasil", "argentina", "cuba", "inglaterra",
                           "egito", "china", "espanha", "portugal", "haiti", "uruguai"])
elif tema == 5:
    senha = random.choice(["pateta", "pikachu", "goku", "patolino",
                           "barbie", "elsa", "naruto", "ratatouille", "simba", "dory"])

espacos = ("_ "*len(senha))  # MOSTRA O TAMANHO DA SENHA

print(senha)

tentativas = 5
erros = 0

print("A palavra é:", espacos)


while tentativas > 0:
    jogo = input("Digite uma letra:")
    if jogo == senha:  # SE A PALAVRA FOR IGUAL A SENHA DO JOGO
        print("""Parabéns, você acertou a palavra e ganhou a capivara da sorte!
                 /)--/)
                 _/    \
               /     o  o
               |       p |
               |      -- )
               U-U------U-U""")
    elif jogo not in senha:  # SE A SENHA DO JOGO NÃO POSSUIR A LETRA. EX: "JOGO" não possui a letra "A"
        print("A palavra não possui a letra {0}" .format(jogo))
        erros = erros+1  # ADICIONA MAIS UM ERRO
        tentativas = tentativas-1  # VAI TIRAR UMA TENTATIVA

    else:  # SE A SENHA DO JOGO POSSUIR A LETRA, MAS NÃO FOR A PALAVRA COMPLETA AINDA. EX: "JOGO" possui a letra "G"
        print("Você acertou uma letra!")
        tentativas = tentativas-1
        # O JOGADOR ERRANDO OU ACERTANDO UMA LETRA PERDE UMA TENTATIVA, MAS SÓ GANHA ERROS SE DIGITAR UMA LETRA QUE NÃO ESTÁ NA SENHA
        # AO GANHAR UM ERRO, PERDE UMA VIDA
    print("Você ainda tem {0} vidas e {1} tentativas!" .format(
        5-erros, tentativas))
    # PARA IMPRIMIR AS VIDAS CONFORME OS ERROS (0 é coração inteiro, 1 é coração quebrado)
    if erros == 0:
        print("<3 <3 <3 <3 <3")
    elif erros == 1:
        print("</3 <3 <3 <3 <3")
    elif erros == 2:
        print("</3 </3 <3 <3 <3")
    elif erros == 3:
        print("</3 </3 </3 <3 <3")
    elif erros == 4:
        print("</3 </3 </3 </3 <3")
    else:
        print("</3 </3 </3 </3 </3")


if tentativas == 0 or erros == 5:
    print("Que pena, suas tentativas esgotaram!")
