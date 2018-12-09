'''
TRABALHO FINAL DE PROGRAMAÇÃO DE COMPUTADORES
Orientador: Prof. MSc. Jackson Prado
Alunos: Cleiton Pastório, Gabriela Schmicheck e Julia Almeida

=======================
NUTRIÇÃO ANIMAL DE GADO
=======================
'''
print(__doc__)

def menu():
    '''
    Função que contém o menu do programa
    '''

    #mostra as opções pro usuário
    print("Bem-Vindo ao menu!")
    print("Opções:")
    print("\t1 - Iniciar")
    print("\t2 - Sair")

    #retornará o que o usuário digitar
    return int(input("Digite a opção desejada:"))

menu()

#se o usuário digitar sair, emite mensagem
if menu() == 2:
    print("Até logo!")
#se não (ou seja, o usuário digitar 1, da o início do programa)
else:

    lista = []
    add = 0
    print("Considerando: Gado leitero: 1; Gado de corte: 2; Pastagem Brachiaria: 1; Pastagem Xaraés: 2; Pastagem Capim Mobaça: 3; Época Seca: 1 e Época de chuvas: 2")
    #a linha de cima é informações pro usuário
    
    #abaixo os dados solicitados do usuário
    t = int(input("Tipo de Gado:"))
    lista.append(t)
    q = int(input("Quantidade de Cabeças:"))
    lista.append(q)
    p = int(input("Pastagem:"))
    lista.append(p)
    e = int(input("Época:"))
    lista.append(e)

    #condicionais que retornarão o tipo de gado e pastagem
    if (lista[0]) == 1 and (lista[2]) == 1:
        print("Gado leitero")
        print("Pastagem Brachiaria Ruziziensis")
    elif (lista[0]) == 1 and (lista[2]) == 2:
        print("Gado leitero")
        print("Pastagem Xaraés")
    elif (lista[0]) == 1 and (lista[2]) == 3:
        print("Gado leitero")
        print("Capim Mobaça")
    elif (lista[0]) == 2 and (lista[2]) == 1:
        print("Gado de corte")
        print("Pastagem Brachiaria Ruziziensis")
    elif (lista[0]) == 2 and (lista[2]) == 2:
        print("Gado de corte")
        print("Pastagem Xaraés")
    elif (lista[0]) == 2 and (lista[2]) == 3:
        print("Gado de corte")
        print("Capim Mobaça")

    #condicionais que retornarão se será necessária a suplementação levando em conta o clima
    if (lista[3]) == 1:
        print("Suplementação com milho/soja será necessária")
        print("Fim!")
        print("Até logo!")
    else: 
        print("Suplementação com milho/soja será desnecessária")   
        print("Fim!")
        print("Até logo!")