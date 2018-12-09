'''
TRABALHO FINAL DE PROGRAMA��O DE COMPUTADORES
Orientador: Prof. MSc. Jackson Prado
Alunos: Cleiton Past�rio, Gabriela Schmicheck e Julia Almeida

=======================
NUTRI��O ANIMAL DE GADO
=======================
'''
print(__doc__)

def menu():
    '''
    Fun��o que cont�m o menu do programa
    '''

    #mostra as op��es pro usu�rio
    print("Bem-Vindo ao menu!")
    print("Op��es:")
    print("\t1 - Iniciar")
    print("\t2 - Sair")

    #retornar� o que o usu�rio digitar
    return int(input("Digite a op��o desejada:"))

menu()

#se o usu�rio digitar sair, emite mensagem
if menu() == 2:
    print("At� logo!")
#se n�o (ou seja, o usu�rio digitar 1, da o in�cio do programa)
else:

    lista = []
    add = 0
    print("Considerando: Gado leitero: 1; Gado de corte: 2; Pastagem Brachiaria: 1; Pastagem Xara�s: 2; Pastagem Capim Moba�a: 3; �poca Seca: 1 e �poca de chuvas: 2")
    #a linha de cima � informa��es pro usu�rio
    
    #abaixo os dados solicitados do usu�rio
    t = int(input("Tipo de Gado:"))
    lista.append(t)
    q = int(input("Quantidade de Cabe�as:"))
    lista.append(q)
    p = int(input("Pastagem:"))
    lista.append(p)
    e = int(input("�poca:"))
    lista.append(e)

    #condicionais que retornar�o o tipo de gado e pastagem
    if (lista[0]) == 1 and (lista[2]) == 1:
        print("Gado leitero")
        print("Pastagem Brachiaria Ruziziensis")
    elif (lista[0]) == 1 and (lista[2]) == 2:
        print("Gado leitero")
        print("Pastagem Xara�s")
    elif (lista[0]) == 1 and (lista[2]) == 3:
        print("Gado leitero")
        print("Capim Moba�a")
    elif (lista[0]) == 2 and (lista[2]) == 1:
        print("Gado de corte")
        print("Pastagem Brachiaria Ruziziensis")
    elif (lista[0]) == 2 and (lista[2]) == 2:
        print("Gado de corte")
        print("Pastagem Xara�s")
    elif (lista[0]) == 2 and (lista[2]) == 3:
        print("Gado de corte")
        print("Capim Moba�a")

    #condicionais que retornar�o se ser� necess�ria a suplementa��o levando em conta o clima
    if (lista[3]) == 1:
        print("Suplementa��o com milho/soja ser� necess�ria")
        print("Fim!")
        print("At� logo!")
    else: 
        print("Suplementa��o com milho/soja ser� desnecess�ria")   
        print("Fim!")
        print("At� logo!")