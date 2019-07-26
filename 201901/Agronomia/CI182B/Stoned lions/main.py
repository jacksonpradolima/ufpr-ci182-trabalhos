cultivares=[]
print("=-"*27,"CALCULO DE PRODUÇÃO DO EXPERIMENTO","-="*27)
resposta="s"
repeticao=0
prog=0
def imprime_matriz(m):
    TAML = len(m)  # tamanho das linhas
    TAMC = len(m[0])  # tamanho das colunas

    for l in range(TAML):
        # TAMC = len(l)  # tamanho das colunas
        for c in range(TAMC):
            print(m[l][c], "      ", end="")
        print("\n")
while prog==0:
    opcoes=["Adicionar cultivares","Ver tabela de cultivares"]
    for c in range (len(opcoes)):
        print(f"{[c]}-{opcoes[c]}")
    opcao=int(input("Digite o número correspondente à opção"))
    if opcao==0:
        while resposta=="s" or resposta=="S":
            nome=(input("Nome do cultivar:"))
            mo=float(input("Digite a produção estimada(original):"))
            ms=float(input("Qual é a produção das melhores plantas?:"))
            vg=float(input("Qual foi a variação genotipica encontrada?:"))
            vf=float(input("e a variação fenotipica"))
            #calculo de herdabilidade
            h2=vg/vf
            print(f"A herdabilidade encontrada é de {h2:.2f}")
            #calculo da variação de ganho
            ds=ms-mo
            g=ds*h2
            #produção#
            mm=mo+g
            if ds>0:
                print(f"Neste cultivar houve uma melhora na produção, esta foi de {mm:.2f}")
            elif ds<=0:
                print(f"Neste cultivar houve diminuição da produção, esta foi de {mm:.2f}")
            #cultivares=[[nome do cultivar, variação do ganho, produção esperada]]
            cultivares.append([])
            cultivares[repeticao].append(nome)
            cultivares[repeticao].append(g)
            cultivares[repeticao].append(mm)
            if ds>0:
                cultivares[repeticao].append("ganho")
            elif ds<=0:
                cultivares[repeticao].append("perda")
            repeticao+=1
            resposta = input("Adicionar mais um cultivar?('s' para sim ou 'n' para não)")
    elif opcao==1:
        print("NOME DO CULTIVAR-=-VARIAÇÃO DE GANHO-=-PRODUÇÃO ESPERADA-=-RESULTADO")
        imprime_matriz(cultivares)

    prog=int(input("\nPara repetir o program digite 0 ou qualquer outro numero para finalizar"))