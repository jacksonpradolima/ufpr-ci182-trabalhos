def lucrodiario(quem, numerohoras, dia):
    if dia == 1:  # se dia normal
        if quem == 3:
            lucro = numerohoras*7  # 7 reais ahora
        else:
            lucro = numerohoras*5  # 5 reais p idosos/defici
    else:  # se fim de semana
        if quem == 3:
            lucro = numerohoras*9  # pra outros
        else:
            lucro = numerohoras*7  # idosos/deficientes
    return lucro


def quantoapagar(horaentrada, horasaida, quem, dia):
    varquanto = horasaida-horaentrada
    if dia == 1:  # se dia normal
        if quem == 3:
            varquanto *= 7  # 7 reais ahora
        else:
            varquanto *= 5  # 5 reais p idosos/defici
    else:  # se fim de semana
        if quem == 3:
            varquanto *= 9  # pra outros
        else:
            varquanto *= 7
    return varquanto


lucro = 0  # estou usando na def
moto = []  # lista para saber quantas vagas disponiveis a motos
carro = []  # lista para saber quantas vagas disponiveis a carros
caminhonete = []  # lista para saber quantas vagas disponiveis a caminhonetes
cont = 0
cont2 = 0
var = 0  # não mechop para receber o valor da def de lucro diario
soma = 0  # não mecho soma é de somatorio dos lucros
sim = input("gostaria de saber o lucro do dia?s/n>:\n>")

while sim == "s":
    dia = int(input("(1)(dia util)\n(2)(fim de semana)\n"))
    quem = int(input("(1)idoso\n(2)com deficiência\n(3)outros\n>"))
    categoria = int(input("categoria:\n(1)carro\n(2)moto\n(3)caminhonete\n>"))
    numerohoras = int(input("horas permanência: "))
    var = lucrodiario(quem, numerohoras, dia)
    soma = soma+lucrodiario(quem, numerohoras, dia)
    sim = input("próximo cliente?s/n:\n>")

print(soma)

horasaida = 0
varquanto = 0
quanto = 0
horaentrada = 0
cadastro = [0, 0, 0]
chegada = []
matriz = []
categoria = 0
agendamento = int(
    input("(1)cadastrar um horista \n(2)cadastrar um mensalista\n>"))
if agendamento == 1:  # CADASTRO DE HORISTA
    for v in range(1):  # PREENCHE A LISTA
        chegada.append(str(input("placa: ")))
        dia = int(input("(1)(dia util)\n(2)(fim de semana)\n"))
        quem = int(input("(1)idoso\n(2)com deficiência\n(3)outros\n>"))
        categoria = int(
            input("categoria:\n(1)carro\n(2)moto\n(3)caminhonete\n>"))
        horaentrada = int(input("hora de entrada: "))
        horasaida = int(input("hora de saida: "))
        quanto = quantoapagar(horaentrada, horasaida, quem, dia)
        chegada.append(quem)
        chegada.append(horaentrada)
        chegada.append(horasaida)
        chegada.append(quanto)
        matriz.append(chegada)  # PREENCHE A MATRIZ
        if categoria == 1:
            carro.append(1)
        elif categoria == 2:
            moto.append(1)
        else:
            caminhonete.append(1)

    pergunta = (
        str(input("gostaria de ver o numero de vagas disponiveis?s/n:\n>")).lower())
    if pergunta == "s":
        pergunta2 = int(input(
            "(1)total de vagas\n(2)apenas carro\n(3)apenas moto\n(4)apenas caminhonete\n>"))
        if pergunta2 == 1:
            # print(100-(len(moto)+len(carro)+len(caminhonete)))#numero total de vagas fixo
            print(100-(len(matriz)))
        elif pergunta2 == 2:
            print(40-(len(carro)))
        elif pergunta2 == 3:
            print(20-(len(moto)))
        else:
            print(40-(len(caminhonete)))


else:  # para mensalistas

    horasaida = 0
    varquanto = 0
    quanto = 0
    horaentrada = 0
    cadastro2 = [0, 0, 0]
    chegada2 = []
    matriz2 = []  # não mecho
    carro2 = []
    moto2 = []
    caminhonete2 = []

    for v in range(1):
        chegada2.append(str(input("placa: ")))
        dia = int(input("(1)(dia util)\n(2)(fim de semana)\n"))
        quem = int(input("(1)idoso\n(2)com deficiência\n(3)outros\n>"))
        categoria = int(
            input("categoria:\n(1)carro\n(2)moto\n(3)caminhonete\n>"))
        horaentrada = int(input("hora de entrada: "))
        horasaida = int(input("hora de saida: "))
        chegada2.append(quem)
        chegada2.append(horaentrada)
        chegada2.append(horasaida)
        chegada2.append(quanto)
        matriz2.append(chegada)
        if categoria == 1:
            carro2.append(1)
        elif categoria == 2:
            moto2.append(1)
        else:
            caminhonete2.append(1)

pergunta = (
    str(input("gostaria de ver o numero de vagas disponiveis?s/n:\n>")).lower())
if pergunta == "s":
    pergunta2 = int(input(
        "(1)total de vagas\n(2)apenas carro\n(3)apenas moto\n(4)apenas caminhonete\n>"))
    if pergunta2 == 1:
            # print(100-(len(moto)+len(carro)+len(caminhonete)))#numero total de vagas fixo
        print(60-(len(matriz2)))
    elif pergunta2 == 2:
        print(30-(len(carro2)))
    elif pergunta2 == 3:
        print(15-(len(moto2)))
    else:
        print(15-(len(caminhonete2)))
