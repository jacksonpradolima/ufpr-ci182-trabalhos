import math


def bhaskara(): #criação das funções que vão realizar as contas
    a = float(input("Digite o coeficiente a:"))
    b = float(input("Digite o coeficiente b:"))
    c = float(input("Digite o coeficiente c:"))
    x1 = ((-b + math.sqrt((pow(b,2)) - 4 * a * c)) / (2 * a))
    x2 = ((-b - math.sqrt((pow(b,2)) - 4 * a * c)) / (2 * a))
    print("X1 =",x1)
    print("X2 =",x2)


def potencia():
    num1 = float(input("Digite o número a ser elevado:"))
    num2 = float(input("Digite o expoente:"))
    pot = num1 ** num2
    print("O resultado é:", pot)


def subtracao():
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número"))
    sub = num1 - num2
    print("O resultado é:", sub)


def soma():
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número"))
    soma = num1 + num2
    print("O resultado é:", soma)


def multiplicacao():
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número"))
    mult = num1 * num2
    print("O resultado é:", mult)


def distancia(): #operações de física
    ponto1 = [float(i) for i in input("Digite as coordenadas do primeiro ponto:(X Y)").split()]
    ponto2 = [float(i) for i in input("Digite as coordenadas do segundo ponto:(X Y)").split()]
    x1 = ponto1[0]
    x2 = ponto2[0]
    y1 = ponto1[1]
    y2 = ponto2[1]

    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    print("A distância entre os dois pontos é:", d)

def velocidade():
    d = float(input("Digite a distância percorrida (m):"))
    t = float(input("Digite o tempo decorrido (s):"))
    v = d/t
    print("A velocidade média é:",v,"m/s")

def aceleracao():
    v = float(input("Digite a variação da velocidade (m/s):"))
    t = float(input("Digite o tempo decorrido (s):"))
    a = v/t
    print("A aceleração média é:",a,"m/s²")

def horariavelocidade():
    v0 = float(input("Digite a velocidade inicial (m/s):"))
    t = float(input("Digite o tempo decorrido (s):"))
    a = float(input("Digite a aceleração (m/s²):"))
    v = v0 + (a*t)
    print("A velocidade final é:",v,"m/s")

def torricelli():
    v0 = float(input("Digite a velocidade inicial (m/s):"))
    a = float(input("Digite a aceleração (m/s²):"))
    d = float(input("Digite a distância percorrida (m):"))
    v = math.sqrt((pow(v0,2)) + ((2*a) * d))
    print("A velocidade final é:",v,"m/s")

def horariadeslocamento():
    s0 = float(input("Digite a posição inicial:"))
    v = float(input("Digite a velocidade instantânea:"))
    t = float(input("Digite o tempo decorrido:"))
    s = s0 + v * t
    print("A posição final é:",s)

def molaridade(): #operações de química
    n = float(input("Digite o número de mols:"))
    V = float(input("Digite o volume:"))
    C = n/V
    print("A molaridade é:",C,"mol/L")

def concentracao():
    m = float(input("Digite a massa:"))
    V = float(input("Digite o volume:"))
    C = m/V
    print("A concentração é:",C,"g/L")

def titulo():
    m1 = float(input("Digite a massa 1:"))
    m2 = float(input("Digite a massa 2:"))
    T = m1/(m1+m2)
    print("O título da solução é:",T)

def mols():
    m = float(input("Digite a massa:"))
    M = float(input("Digite a massa molar:"))
    n = m/M
    print("O número de mols é:",n,"mols")


print("""BEM VINDO AO FORMULÁRIO!
Para começar, digite 1. Para sair, tecle qualquer coisa.""")
menu = input(">")

while menu == "1": #vai criar um laço a não ser que menu seja diferente de 1
    print("""Escolha uma opção:

    1 - Matemática
    2 - Física
    3 - Química""")
    disciplina = input(">")

    if disciplina == "1": #escolha das disciplinas por condicionais
        print("""Escolha uma operação a ser realizada:

            1 - Soma
            2 - Multiplicação
            3 - Potenciação
            4 - Bhaskara
            5 - Distância entre dois pontos""")
        op = input(">")
        if op == "1":
            soma()
        elif op == "2":
            multiplicacao()
        elif op == "3":
            potencia()
        elif op == "4":
            bhaskara()
        elif op == "5":
            distancia()
        else:
            print("Ops! Esta não é uma opção válida")

    elif disciplina == "2":
        print("""Escolha uma operação a ser realizada:

        1 - Velocidade média
        2 - Aceleração
        3 - Função horária da velocidade
        4 - Equação de Torricelli
        5 - Função horária do deslocamento""")
        op = input(">")
        if op == "1":
            velocidade()
        elif op == "2":
            aceleracao()
        elif op == "3":
            horariavelocidade()
        elif op == "4":
            torricelli()
        elif op == "5":
            horariadeslocamento()
        else:
            print("Ops! Esta não é uma opção válida")

    elif disciplina == "3":
        print("""Escolha uma operação a ser realizada:
        1 - Molaridade
        2 - Concentração comum
        3 - Título
        4 - Número de mols""")
        op = input(">")
        if op == "1":
            molaridade()
        elif op == "2":
            concentracao()
        elif op == "3":
            titulo()
        elif op == "4":
            mols()
        else:
            print("Ops! Esta não é uma opção válida")
    else:
        print("Ops! Esta não é uma opção válida") #caso haja algum erro

    menu = input("Aperte 1 para realizar uma nova operação. Digite qualquer coisa para sair.") #continuação do laço


