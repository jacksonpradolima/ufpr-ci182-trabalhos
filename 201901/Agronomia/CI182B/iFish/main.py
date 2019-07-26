totais = 0
raçao=0
gastoxi=0
lucro1=0
eqipa=0
fixos=0
tilápia=0
alevtila=0
alevinos=0
gastoxi=0
# gastos possíveis com o projeto.

oi = input("Olá você já conhece o nosso trabalho?")
if oi == "Sim" or oi == "sim":
    print("Bom, então vamos aos cálculos!")
else:
    print("Nós somos uma empresa que leva a você a possibilidade de cálcular o quanto você irá gastar na implantação do sistema de psicultura.")
estd = ["São Paulo", "Rio de Janeiro", "Paraná", "Minas Gerais", "Mato Grosso", "são paulo", "rio de janeiro", "paraná",
        "minas gerais", "Mato Grosso"]
estd0 = ["parana", "PR", "MT", "SP", "RJ", "MG", "pr", "mt", "sp", "rj"]
# Nesses Estados os cuidados são praticamente os memos o que facilitou o calculo, por isso optamos por esses estados.

local = input("De qual Estado você é? Por favor digite a sigla de seu estado:")
if local == "Acre" or local == "acre" or local == "AC":
    print("Nessa região o cálculo não está disponível e o mais recomendado para sua região é a criação de Dinossauros.")
    c=0
elif local == "Rio Grande do Sul" or local == "rio grande do sul" or local == "RG":
    print("Nessa região o clima nao é favoravel ")
    c=0
elif local in estd or local in estd0:
    print("O Cálculo está disponível.")
else:
    print("Devido a dificuldades essa região ainda não está disponível.")
    resp = input("Deseja efetuar contato para que um de nossos técnicos posso o atender para o cálculo?")
    if resp == "sim" or resp == "Sim":
        print("Ótimo, o número de nosso contato é (42)998052709")
        c=0
    else:
        print("Muito obrigado por usar nosso programa, caso precise de algo faça o contato com a gente pelo número (42)998052709.")

if local in estd or local in estd0:
    liç = input("Você ja possui licença ambiental?")
    if liç == "sim" or liç == "Sim":
        licença=0
    elif liç == "não" or liç == "Não" or liç == "nao":
        totais += 500
    else:
        print("Erro, por favor reinicie o programa.")

# começo a parte em que está relacionada ao cálculo do programa

while local in estd or local in estd0:
    tipo = input("Disponibilizamos dois tipos de produção, A=produão em tanques e a B=produção em caixas d´água. Qual tipo deseja?")
    # A principal forma de produção
    if tipo == "A" or tipo == "a":
        for i in range(0,1):
            print("O cálculo é feito para tanques de grande proporção a partir de 80m² até 120, pelos gastos que são específicos.Pode não bater para pequenos tanques")
            tamanho = float(input("Por recomendações de prdução o tanque deve ter 1.2 metros de profundidade.Informe o tamanho do tanque em m² : "))
            while tamanho<50 or tamanho>120:
                tamanho=float(input("digite o tamanho novamente"))
            m3 = (tamanho * 1.2)
            gastoxi += ((4220 * m3) / 12000)
            totais += gastoxi
            escv = ((m3 * 15000) / 12000)
            totais += escv
            # calculo de escavação segundo embrapa.
            # A escolha dessespeixes foi para facilitar o cálculo pois eles tem bom desenvolvimento na maioria das regiões e também são os mais comuns para criação
            c=1
        break
    elif tipo == "B" or tipo == "b":
        print("Cálculo nâo esta disponível, mas entre em contaco para calcularmos pra você. Fone:(42)998052707.")
        c=0
        break
    else:
        print("Ops, algo deu errado, por favor tente novamente e faça tudo corretamente.")

#so calculo de lucro e despesas para tilapia
if c!=0:
    print("Por enquanto nós apenas trabalhamos com o alevino de tilápia no programa.")
    # x é o valor do alevino desse peixe
    x = 0.35
    gast = float(m3 * x * 6)
    alevtila = int(m3 * 6)
    fixos += gast
    alevinos += gast
    raçao += float((m3 * 26000) / 12000)
    fixos += raçao

    # taxa de sobrevivencia
    tilápia = int(alevtila * 0.9)
    print("Irá produzir:", tilápia,"tilápias.")
    # luco obtido com o peixe
    lucro = float(tilápia * 1.3 * 7.50)
    # gastos de manutençao e funcionários anuais
    fixos = (raçao + alevinos + 1500)
    totais+=fixos
    eqipa = 9000
    totais += eqipa
    pri = (totais-lucro)
    seg = (lucro-fixos)
    print(fixos, totais,lucro)

    # relatorio dos gastos qeu o calculo apresentou
    print("Esses são os gastos:")
    print("Despesas totais, R$:", totais)
    print("Despesas do primeiro ano, R$:", (pri))
    print("Lucro do segundo, R$:", (seg))
    print("Muito obrigado por usar nosso programa, para dados mais detalhados ou para que um de nosso técnicos va ao seu local para fazer a instalação o fone é (42)998052706")