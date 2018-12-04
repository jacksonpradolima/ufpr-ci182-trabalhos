# -*- coding: utf-8 -*-

nomes = []  # listas vazias que serão utilizadas para inserir os dados dos animais
racas = []
idades = []
pesos = []
# pede o valor da arroba para cálculo com base na cotação do dia
A = float(input("Cotação da Arroba Hoje:"))
n = int(input("Número de animais no lote:"))  # criará o laço de repetição
i = 0  # contador para o while
while i < n:  # validador para solicitação de dados, inserindo apenas a quantia de animais desejada pelo usuário
    nome = input("Nome:")
    raca = input("Raça (N para Nelore; C para Canchim; B para Brangus):")
    idade = input("Idade (em meses):")
    peso = input("Peso (em Kg):")
    nomes.append(str(nome))  # adiciona os nomes na lista de nomes
    racas.append(str(raca))  # adiciona as raças na lista de raças
    idades.append(float(idade))  # adiciona as idades na lista de idade
    pesos.append(float(peso))  # adiciona os pesos na lista de pesos
    i = i+1  # faz o while caminhar
# solicita a área para criação dos piquete
area = float(input("Insira a área disponível (em m^2):"))
# cálculo comum para manejo em piquetes, utilizando 30 dias de descanso e 2 de ocupação para cada piquete
nropiquete = (30/2)+1
tamanhopiquete = area/nropiquete  # calcula a área por piquete
# exibe ao usuário com 2 casas decimais
print("Tamanho dos Piquetes: {0:.2f} m^2".format(tamanhopiquete))
# calcula o número de animais que cabe em cada piquete
nroanimaispiquete = (tamanhopiquete*6)/10000
print("Número de animais que podem ser alocados por piquete: {0:.1f}".format(
    nroanimaispiquete))  # exibe aos usuários
expectativa = 0  # inicia o contador para o "lucro" que será gerado por arroba de cada boi enviado para o abate
j = 0  # contador para o While
while j < (len(pesos)):  # while para interromper a avaliação dos animais quando acabarem os indivíduos da lista
    # "pesa o animal", armazena numa variável o peso do animal em análise
    balanca = (pesos[j])
    if (racas[j]) == 'N':  # valida se animal é da raça Nelore
        parametro = 19*15
        if balanca >= parametro:  # valida se animal está pronto para o abate
            # exibe ao usuário
            print("Animal "+(nomes[j])+" pronto para o abate")
            # soma o valor esperado a se receber ao montante do dia, após calcular quanto se receberá com aquele indivíduo (animais enviados para o abate)
            expectativa = ((balanca/15)*A)+expectativa
            nomes.pop(j)  # remove o animal enviado para o abate de cada lista
            racas.pop(j)  # aqui não se faz necessário "andar com o contador", pois ao excluir o animal das listas, o próximo animal tomará seu lugar, ocupando a posição que o eliminado estava
            idades.pop(j)
            pesos.pop(j)
        else:
            # calcula quantidade de dias em que o animal deve atingir o peso ideal, considerando o ganho de 1Kg/dia
            nrodias = (parametro-balanca)/1
            # exibe as instruções ao proprietário, dando uma expectativa de quantos dias para o abate
            print(
                "Animal "+(nomes[j]) + "deve passar para o próximo piquete, devendo estar pronto em aproximadamente {0:.1f} dias.".format(nrodias))
            j = j+1  # aqui há necessidade de andar com o contador, pois não houve exclusão da lista
    elif (racas[j]) == 'C':  # valida se o animal é da raça Canchim
        parametro = 23*15  # multiplica o número de arrobas pelo valor em Kg da arroba, para que possa ser comparado com o peso em Kg do animal
        if balanca >= parametro:  # valida se animal está pronto para o abate
            print("Animal "+(nomes[j])+" pronto para o abate")
            # soma o valor esperado a se receber ao montante do dia, após calcular quanto se receberá com aquele indivíduo (animais enviados para o abate)
            expectativa = ((balanca/15)*A)+expectativa
            nomes.pop(j)  # retira o animal das listas
            racas.pop(j)  # aqui não se faz necessário "andar com o contador", pois ao excluir o animal das listas, o próximo animal tomará seu lugar, ocupando a posição que o eliminado estava
            idades.pop(j)
            pesos.pop(j)
        else:
            # calcula quantidade de dias em que o animal deve atingir o peso ideal, considerando o ganho de 1Kg/dia
            nrodias = (parametro-balanca)/1
            print(
                "Animal "+(nomes[j])+" deve passar para o próximo piquete, devendo estar pronto em aproximadamente {0:.1f} dias.".format(nrodias))
            j = j+1
    elif (racas[j]) == 'B':  # verifica se o animal é da raça Brangus
        parametro = 21*15  # multiplica o número de arrobas pelo valor em Kg da arroba, para que possa ser comparado com o peso em Kg do animal
        if balanca >= parametro:  # valida se animal está pronto para o abate
            print("Animal "+(nomes[j])+" pronto para o abate")
            # soma o valor esperado a se receber ao montante do dia, após calcular quanto se receberá com aquele indivíduo (animais enviados para o abate)
            expectativa = ((balanca/15)*A)+expectativa
            nomes.pop(j)
            racas.pop(j)
            idades.pop(j)
            pesos.pop(j)
        else:
            # calcula quantidade de dias em que o animal deve atingir o peso ideal, considerando o ganho de 1Kg/dia
            nrodias = (parametro-balanca)/1
            print(
                "Animal "+(nomes[j])+" deve passar para o próximo piquete, devendo estar pronto em aproximadamente {0:.1f} dias.".format(nrodias))
            j = j+1
    else:
        print("Raça não compatível com o sistema, será eliminado da lista")
        nomes.pop(j)  # remove o "intruso"
        racas.pop(j)
        idades.pop(j)
        pesos.pop(j)
print("Ganho esperado com os animais enviados para o abate: {0:.2f}".format(
    expectativa))
