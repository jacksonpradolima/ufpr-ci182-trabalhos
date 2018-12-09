import os
import math
import time


# Comandos de documentação do código
__author__ = "Hard prog"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Hard prog"  # A pessoa que mantém o código
# Status tipicamentente é: Prototype, Development ou Production
__status__ = "Prototype"

def mastraOpcoes():
    '''
    Função que contém o menu do programa
    '''
    print("""Olá, bem vindo, digite a opção desejada para o cálculo
            \t1 - Á partir da  área. 
            \t2 - á partir do numero de aves. 
            \t0 - Sair
            """)
    # Retorna o que o usuário digitar
    return int(input('Digite a opção desejada: '))

def calculaAreaApartirAves(numero_aves):
    return float(numero_aves * 0.008)

def definiNumeroValido(n):
    if(n>0):
        return True
    if(n <= 0):
        print('Valor Inválido')
        return False
     

def imprime_Resultado_Final(area, totalAves, machos, femeas, calculo_alimentacao, custo_eletricidade, custo_agua, precoOvos):

    preco = precoOvos
    print("===========================================================")
    print("Total de Machos:")
    print("%.2f" % round(machos,2))
    print("===========================================================")
    print("Total de Femeas:")
    print("%.2f" % round(femeas,2))
    print("===========================================================")
    print("Total de Femeas com Perca:")
    femeasComPerca = femeas * 0.1
    totalFemeas = femeas - femeasComPerca
    print("%.2f" % round( totalFemeas,2))
    print("===========================================================")
    print("Total de Aves:")
    print("%.2f" % round(totalFemeas,2))
    print("===========================================================")
    print("Área Necessária:")
    print("%.2f" % round(area,2))
    print("===========================================================")

    print("Previsão de Quantidade de Ovos Mensal:")
    qtdOvosMensal = (totalFemeas / 30) 
    print("%.2f" % round(qtdOvosMensal,2))
    print("===========================================================")

    print("Previsão de Produção mensal R$ (Lucro Bruto):")
    lucro_bruto = (totalFemeas / 30) * preco
    print("%.2f" % round(lucro_bruto,2))


    print("==================CUSTOS===================================")
    print("Custo água:", round(custo_agua,2))
    print("Custo Eletricidade:", round(custo_eletricidade,2))
    print("calculo_alimentação:", round(calculo_alimentacao,2))
    print("===========================================================")


    totalCusto =  round( (custo_agua +  custo_eletricidade + calculo_alimentacao), 2 )

    lucroLiquido  = round((lucro_bruto - totalCusto),2)

    print("LUCRO LIQUIDO:", lucroLiquido)

    matrizResultado = []


def imprime_lucro_liquido():
        print(lucro_liquido)    

#funcao que calcula custo com agua de acordo com o numero de aves.
def despezas_agua(numeroAves):

    print("qual a quantidade de agua por lote m³")
    qa=float(input(">"))#qa=quantidade de água por lote

    print("custo de agua por m³(R$)")
    pa=float(input(">"))#custo da água por m³

    aves=numeroAves

    custo_agua=(qa*pa)/aves 
    return custo_agua
    

    
def despezas_eletricidade(numeroDeAves):

    print("qual o seu consumo de energia eletrica por lote")
    cl=float(input(">"))# cl= consumo de energia por lote 

    print("qual o custo do kw/h")
    pe=float(input(">"))#custo do kw/h

    aves = numeroDeAves
    custo_eletricidade = (cl*pe) / aves

    return custo_eletricidade             
    
    
    
       
        
def calculo_alimentacao(numeroAves):

    print("Digite o valor da ração em R$")
    racao = float(input(">"))# em R$

    aves = numeroAves
    racao = racao

    custo_alimentacao = (racao / aves )

    return custo_alimentacao

def calculaArea():

    print("Qual a quantidade de aves fêmeas com que pretende trabalhar?")

    femeas = int(input(">"))


    #verifica se o valor informado é valido, se não for pergunta novamente....
    isValid = definiNumeroValido(femeas)

    while (isValid == False):
        calculaArea()



    print("Digite o valor estipulado para venda para uma caixa de 30 ovos.")
    preco = float(input(">"))

    machos = (femeas / 3)
    
    totalAves = femeas + machos

    area = calculaAreaApartirAves(totalAves)
    
    valor_alimentacao= calculo_alimentacao(totalAves) 
    

    custo_eletricidade = despezas_eletricidade(totalAves)

    custo_agua = despezas_agua(totalAves)


    # chama a funcao que exibe os resultados
    imprime_Resultado_Final(area, totalAves, machos, femeas, valor_alimentacao, custo_eletricidade, custo_agua, preco)

    time.sleep(5)


    print("""Deseja fazer outra simulação?
            \t1 - Sim. 
            \t2 - Não(finalizar simulação). 
            """)

    # Retorna o que o usuário digitar
    opcaoIteracao =  int(input('Digite a opção desejada: '))

    # se o usuario selecionar qualquer coisa diferente do que 1 ele finaliza a simulçao.
    while opcaoIteracao == 1:
           #Solicita novamente os dados pro usuario 
          calculaArea()

    #finaliza o programa
    print("Simulacao Finalizada")
    return

def apartirDaArea():
    
    print("Digite a área M²:")
    area = float(input(">"))
    totalAves = float(area * 0.008)

    print("Digite o valor estipulado para venda para uma caixa de 30 ovos.")
    preco = float(input(">"))
    print("===========================================================")

    machos = totalAves / 3

    femeas = totalAves - machos



    valor_alimentacao= calculo_alimentacao(totalAves )

    custo_eletricidade = despezas_eletricidade(totalAves)

    custo_agua = despezas_agua(totalAves)



    imprime_Resultado_Final(area, totalAves, machos, femeas, valor_alimentacao, custo_eletricidade, custo_agua, preco)

    time.sleep(5)


    print("""Deseja fazer outra simulação?
            \t1 - Não(finalizar simulação). 
            \t2 - Sim. 
            """)
    # Retorna o que o usuário digitar
    opcaoIteracao =  int(input('Digite a opção desejada: '))


    while opcaoIteracao != 1:
          apartirDaArea()

    print("Simulacao Finalizada")
    return

def main():
    
    '''
    Programa Hard Prog 
    '''

    # chama a função menu que mostra o menu e solicita uma opção ao usuário
    option = mastraOpcoes()
    
    # Se for a opção: 1 - a partir da área
    if option == 1:
        apartirDaArea()
    elif option == 2:
        calculaArea()
        time.sleep(5)
        # Se digitou uma opção de menu inválida
    else:
        print("\nOpção inválida! Por favor, informe uma opção válida.\n")
        # Faz o programa esperar 1 segundo e depois continua
        time.sleep(2)
        
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')


main()

