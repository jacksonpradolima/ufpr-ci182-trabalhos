
# -*- coding: utf-8 -*-
"""
=======================
CALCULADORA TOPOGRÁFICA
=======================

"""
print(__doc__)
# Bibliotecas
import os
import time
import math
# Comandos de documentação do código
__autores__ = "" #colocar os nomes e grr
time.sleep(4)
def calculadora_coordenadas():#função que calcula coordenadas
    print("Digite os valores de X e Y do ponto A:")#pede os valores ao usuário
    xa=float(input("X:"))#valor de x da coordenada inicial
    ya=float(input("Y:"))#valor de y da coordenada inicial
    r=input("Você possui as variações DeltaX e DeltaY?(S para sim, N para não)")#dá ao usuário a opção de inserir valores calculados ou calcular no próprio programa
    if r == 'S':#validação da escolha do usuário
        DeltaX=float(input("DeltaX (em metros): "))#variação de metragem entre os pontos na coordenada x
        DeltaY=float(input("DeltaY (em metros): "))#variação de metragem entre os pontos na coordenada Y
        xb=DeltaX+xa#calcula a coordenada desejada em x
        yb=DeltaY+ya#calcula a coordenadad desejada em y
        print("Xb= {0:.3f} ; Yb= {1:.3f}".format(xb,yb))#exibe ao usuário
    elif r == 'N':#validação da possivel escolha do usuário
        g=int(input("Graus: "))#solicita os graus; int porque não admite grau decimal
        m=int(input("Minutos: "))#solicita os minutos; int porque não existe minuto decimal
        s=int(input("Segundos: "))# solicita os segundos, int porque não admite segundo decimal
        g1=(g+(m/60)+(s/3600))#conversor de grau decimal
        Dh=float(input("Distância Horizontal (em metros): "))#solicita a distânica inclinada que será usada no próximo cálculo
        DeltaX=(math.sin(math.radians(g1)))*Dh#calcula DeltaX
        DeltaY=(math.cos(math.radians(g1)))*Dh#calcula DeltaY
        print("DeltaX={0:.3f} e DeltaY={1:.3f}".format(DeltaX,DeltaY))#imprime as variações ao usuário
        xb=DeltaX+xa#calcula a coordenada desejada em x
        yb=DeltaY+ya#calcula a coordenada desejada em y
        print("Xb= {0:.3f} ; Yb= {1:.3f}".format(xb,yb))#exibe ao usuário
    else :#rejeita respostas fora do permitido
        print("Erro - resposta deve ser apenas S ou N")
def calculadora_de_area(): #função que calcula área
    x=[]#lista vazia para os valores de x
    y=[]#lista vazia para os valores de y
    print("Insira uma lista de metragens de coordenadas X, ou digite x para finalizar a inserção.")#pede ao usuário os valores de X
    linha=input(">")#primeira solicitação de valores
    while linha != 'x':#laço para validar a continuação ou não da lista
        x.append(float(linha))#insere o que for digitdao na lista x
        linha=(input(">"))#reinicia o processo
    x.append(float(x[0]))#repete o primeiro valor digitado, necessário para conta
    print("Insira uma lista de metragens de coordenadas Y, ou digite x para finalizar a inserção.")#pede aos usuários os valores de y
    linha=input(">")#primeira solicitação de valores
    while linha != 'x':#laço para validar a continuação ou não da lista
        y.append(float(linha))#insere o que for digitdao na lista y
        linha=(input(">"))#reinicia o processo
    y.append(float(y[0]))#repete o primeiro valor digitado, necessário para conta
    i=0#contador, faz a lista "andar"
    somatoriox=0#armazena os valores multiplicados de x
    somatorioy=0#armazena os valores multiplicados de y
    while (i+1) < (len(x)):#calcula para todos os valores existentes na lista
        m=y[i]*x[(i+1)]#multiplicador em cruz
        somatoriox=somatoriox+m#soma
        i=i+1#movimenta o contador
    print("Somatório em x: {0:.3f}".format(somatoriox))#exibe o resultado
    i=0#zera o contador para que possa ser reaproveitado
    while (i+1) < (len(y)):#calcula para todos os valores existentes na lista
        m=x[i]*y[(i+1)]#multiplicador em cruz
        somatorioy=somatorioy+m#armazena
        i=i+1#anda com a lista
    print("Somatório em y: {0:.3f}".format(somatorioy))#resultado parcial
    a=(somatoriox-somatorioy)*0.5#finaliza a conta de área com a fórmula
    print("Área (em m^2): {0:.3f}".format(a))#exibe o valor em metros quadrados
    print("Área (em Hectares): {0:.3f}".format(a/10000))# e em hectares
def calculadora_de_nivelamento():#função que calcula os nivelamentos
    print("NIVELAMENTO - Insira os valores em metros:")
    fsr=float(input("Fio Superior de Ré:"))#recebe os valores
    fir=float(input("Fio Inferior de Ré:"))#recebe os valores
    fmr=float(input("Fio Médio de Ré:"))#recebe os valores
    h=(fsr+fir)/2#tira a média dos fios superior e inferior de ré
    if fmr>(h+0.002) or fmr<(h-0.002):#verifica a tolerânica de +- 2 mm
        print("Fora da Tolerância!Realizar Nova Leitura de Fio Médio de Ré!")
    else:
        print("Fio Médio de Ré OK!")
        dr=(fsr-fir)*100#calcula distância horizontal de ré
        fsv=float(input("Fio Superior de Vante:"))#recebe os valores
        fiv=float(input("Fio Inferior de Vante:"))#recebe os valores
        fmv=float(input("Fio Médio de Vante:"))#recebe os valores
        j=(fsv+fiv)/2#média dos fios superior e inferior de vante
        if fmv>(j+0.002) or fmv<(j-0.002):#verifica a tolerancia de +- 2 mm
            print("Fora da Tolerância!Realizar Nova Leitura de Fio Médio de Vante!")
        else:
            print("Fio Médio de Vante OK!")
            dv=(fsv-fiv)*100#calcula a distância horizontal de vante
            dsnvl=fmr-fmv#calcula do desnível do nivelamento
            print("CONTRANIVELAMENTO - Insira os valores em metros:")
            cfsr=float(input("Fio Superior de Ré:"))#recebe os valores
            cfir=float(input("Fio Inferior de Ré:"))#recebe os valores
            cfmr=float(input("Fio Médio de Ré:"))#recebe os valores
            ch=(cfsr+cfir)/2#média dos fios inferior e superio de ré do contranivelamento
            if cfmr>(ch+0.002) or cfmr<(ch-0.002):#verifica a tolerancia de +-2mm
                print("Fora da Tolerância!Realizar Nova Leitura de Fio Médio de Ré!")
            else:
                print("Fio Médio de Ré OK!")
                cdr=(cfsr-cfir)*100#calcula distância horizontal de ré do contranivelamento
                cfsv=float(input("Fio Superior de Vante:"))#recebe os valores
                cfiv=float(input("Fio Inferior de Vante:"))#recebe os valores
                cfmv=float(input("Fio Médio de Vante:"))#recebe os valores
                cj=(cfsv+cfiv)/2#média dos fios superior e inferior de vante
                if cfmv>(cj+0.002) or cfmv<(cj-0.002):#verifica a Tolerância de +-2mm
                    print("Fora da Tolerância!Realizar Nova Leitura de Fio Médio de Vante!")
                else:
                    print("Fio Médio de Vante OK!")
                    cdv=(cfsv-cfiv)*100#calcula a distância de vante do contranivelamento
                    cdsnvl=cfmr-cfmv#Desnível do contranivelamento
                    ep=(sqrt(((dr+dv)+(cdr+cdv)/2)/1000))*10#calcula o erro permitido - média das distâncias somadas de ré e vante do contra e Nivelamento, convertidas em kilômetros
                    ec=((abs(dsnvl))-(abs(cdsnvl)))#calcula o erro cometido
                    if ec<ep:#compara erro permitido e cometido
                        desnivelmedio=((abs(dsnvl)+abs(cdsnvl))/2)#desnivelmedio calculado pq passou no erro permitido
                        disr=(dr+cdr)/2#média das distâncias de ré
                        disv=(dv+cdv)/2#média das Distâncias de Vante
                        print("Distância de Ré: {0:.3f}".format(disr))#exibe ao usuário
                        print("Distância de Vante: {0:.3f}".format(disv))#exibe ao usuário
                        print("Desnível médio entre os pontos:+-{0:.3f}".format(desnivelmedio))#exibe ao usuário
                    else:
                        print("Retorne a campo, desnível fora da Tolerância")#fora da tolerancia, novo levantamento deve ser feito
def menu():#Função que contém o menu do programa
#Aparecem as opções pro usuário na tela
    print('Menu:')
    print('\t1 - Calculadora de Coordenadas')
    print('\t2 - Calculadora de Área')
    print('\t3 - Calculadora de Nivelamento')
    print('\t4 - Sair')
    return int(input('Digite a opção desejada: '))# Retorna o que o usuário digitar
def main():#Programa principal ~"O cara", manda-chuva, cérebro....
    os.system('cls' if os.name == 'nt' else 'clear')# Limpa a tela do terminal para ficar mais "elegante" a apresentação
    opcao = menu()# chama a função menu que mostra o menu e solicita uma opção ao usuário, através de uma variável a ser validada
    while opcao != 4:# enquanto o usuário não digitar a opção 4, que fecha o programa
        if opcao == 1:# Se for a opção: 1 - calculadora de coordenadas
            calculadora_coordenadas()# chama a função que calcula Coordenadas
            time.sleep(7)#tempo que os prints ficarão na tela, atens de desaparecer novamente
        elif opcao == 2:# Se for a opção: 2 - Calculadora de Área,chama a função que calcula a área
            calculadora_de_area()# passando o vetor que contém as amostras
            time.sleep(7)#tempo que os prints ficarão na tela, atens de desaparecer novamente
        elif opcao == 3:# Se for a opção: 3 - Calculadora de Nivelamento, chama a função que calcula o Nivelamento
            calculadora_de_nivelamento()
            time.sleep(7)
        elif opcao == 4:
            break
        else:# Se digitou uma opção de menu inválida
            print("\nOpção inválida! Por favor, informe uma opção válida.\n")#sinal ao usuário que ele fez coisa errada
            time.sleep(2)# Faz o programa esperar 2 segundos e depois continua
        os.system('cls' if os.name == 'nt' else 'clear')# Limpa a tela do terminal
        opcao = menu()# Mostra ao usuário o menu novamente e aguarda ele escolher uma opção
import os.path
if __name__ == "__main__":
    main()  # Chama a função main


