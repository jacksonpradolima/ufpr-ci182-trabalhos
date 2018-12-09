'''
Trabalho final referente à disciplina de Programação de Computadores.
Programa que calcula média de produtividade de grãos com base em valores informados pelo usuário.
Alunas: Bianca Chastalo e July Caroline.
'''



def produtividade_soja():
    '''
    Função que calcula produtividade de soja
    Dentro da função os dados necessários para a conta serão pedidos
    '''

    # Solicita alguns dados do usuário
    plantas10m = float(input("\nDigite a quantidade de plantas em dez metros: "))
    esp_m = float(input("Digite o espaçamento em metros: "))
    quantVag = float(input("Digite a quantidade total de vagens em dez plantas consecutivas: "))

    # Cálculo de médias com os valores informados
    plantasHa = ((plantas10m / 10) / esp_m) * 10
    mediaVagens = quantVag / 10

    # Conta para definir a quantidade de sacos/ha
    # Valores padrão - "2.5": valor (médio) de sementes por vagem/ "170": peso (médio) de mil grãos
    sacos = (plantasHa * mediaVagens * 2.5 * 170) / 60000

    print("\nCom base nos valores informados, a média de produtividade da soja será de {:.2f} sacos/ha.\n".format(sacos))

    # Chama função menu() para o usuário escolher fazer outro cálculo ou sair do programa
    menu()
    return sacos



def produtividade_milho():
    '''
    Função que calcula produtividade de milho
    Dentro da função os dados necessários para a conta serão pedidos
    '''

    # Mostra uma tabela para ajudar o usuário a informar os próximos dados
    print("\nEspaçamento(cm)\tComprimento para ter 4m²\n50\t\t\t\t8m\n60\t\t\t\t6,6m\n70\t\t\t\t5,7m\n80\t\t\t\t5m\n90\t\t\t\t4,4m\n100\t\t\t\t4m")

    espigas4m = float(input("\nUsando a tabela como referência, informe o número de espigas em 4m²:"))

    # Cria lista vazia
    graos = []

    while len(graos) != 3:
        graos = [float(g) for g in input("Com base em 3 espigas, informe a quantidade de grãos de cada uma, separando as quantidades por espaço:").split()]  # Quebra os valores e coloca na lista
        if len(graos) != 3:
            print("Você deve informar 3 valores!")

    somagraos = len(graos)  # Conta a quantidade de valores na lista
    mediaGraos = sum(graos) / somagraos   # Soma os valores da lista e calcula média


    # Mesma lógica da lista acima
    fileiras = []
    while len(fileiras) != 3:
        fileiras = [float(f) for f in input("Com base nas mesmas espigas, informe a quantidade de fileiras de cada uma, separando as quantidades por espaço:").split()]
        if len(fileiras) != 3:
            print("Você deve informar apenas 3 valores!")
    somafileiras = len(fileiras)
    mediaFileiras = sum(fileiras) / somafileiras

    # Conta para definir a média de produtividade
    # Valor padrão - "0.7": fator de correção da transformação de bushels/acre para kg/ha
    prod = espigas4m * mediaFileiras * mediaGraos * 0.7

    print("\nCom base nos dados informados, a média de produtividade do milho com 15,5% de umidade será de {:.2f} kg/ha.\n".format(prod))

    # Chama função menu() para o usuário escolher fazer outro cálculo ou sair do programa
    menu()
    return prod



def menu():
    '''
    Função do menu do programa
    '''

    # Mostra uma mensagem de boas-vindas e as opções
    print("Vamos estimar produtividade? Escolha a opção que corresponde ao grão plantado ou digite outro número para sair.\n\t1 - Soja\t\t2 - Milho")
    opcao = int(input("\nOpção:"))

    # Se a opcao for 1, chama a função produtividade_soja()
    if opcao == 1:
        produtividade_soja()
    # Se a opcao for 2, chama a função produtividade_milho()
    elif opcao == 2:
        produtividade_milho()
    # Se a opcao não for 1 nem 2, a mensagem será exibida e o programa encerrado
    else:
        print("Volte sempre!")



if __name__ == "__main__":
    '''
    Quando executar o programa Python esse trecho de código será executado
    '''

    # Chama a função menu
    menu()