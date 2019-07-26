#Trabalho introdução a programação
#apresentação
print("-="*42,"BEM VINDO","=-"*42)
#introdução do programa
print("-="*30,"CALCULADORA NUTRIONAL DE OVELHAS DE CORTE EM CONFINAMENTO","=-"*30)
print(" \n ")
#dados referentes aos diferentes tipo de animais em confinamento para um produção de corte de ovino
#matrizes em lactação em gestação a ingestão de alimento deve ser maior pela perda de peso constante que o animal sofre
classes=["MANTENÇA","FLUSHING","INICIO DA GESTAÇÃO COM UM CORDEIRO","INICIO DA GESTAÇÃO COM DOIS CORDEIROS","FINAL DA GESTAÇÃO COM UM CORDEIRO","FINAL DA GESTAÇÃO COM DOIS CORDEIROS","INICIO DA LACTAÇÃO COM UM CORDEIRO","INICIO DA LACTAÇÃO COM DOIS CORDEIROS"]
#matrizes com pesos; cada linha representa um animal, e cada coluna sua faixa de peso, dentro do sistema confinado
pesos=[[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80],[40,50,60,70,80]]
#lista de matrizes, cada matriz é correspondente a classe do animal, cada linha seria o peso e as colunas as necessidades
#dados retirar das tabela da ncr de 2016
valores=[[[0.77,0.55,0.040,0.41,1.8,1.3,19.5,7.8],[0.91,0.5875,0.47,0.49,2,1.5,27.5,11.0],[1.05,0.6625,0.53,0.56,2.2,1.8,39.5,15.8],[1.18,0.075,0.6,0.62,2.4,2.0,49.5,19.6],[1.30,0.825,0.66,0.69,2.6,2.2,49.5,19.6]],[[0.85,0.0575,0.046,0.45,2.1,1.5,49.5,19.6],[1.01,0.06875,0.055,0.53,2.4,1.8,49.5,19.6],[1.15,0.0775,0.055,0.53,2.4,1.8,27.5,11.0],[1.30,0.0875,0.70,0.69,2.9,2.4,27.5,11.0],[1.43,0.09625,0.77,0.76,3.1,2.7,27.5,11.0]],[[0.99,0.06875,0.055,0.52,3.4,2.4,27.5,11.0],[1.16,0.08,0.064,0.61,3.8,2.8,27.5,11.0],[1.31,0.09125,0.073,0.70,4.2,3.2,27.5,11.0],[1.46,0.10125,0.081,0.78,4.5,3.5,76.0,30 ],[1.61,0.11125,0.089,0.85,4.9,3.9,76.0,30 ]],[[1.15,0.08375,0.067,0.61,4.8,3.2,19.5,7.8 ],[1.31,0.095,0.076,0.70,5.4,3.7,27.5,11.0],[1.51,0.10875,0.087,0.80,5.9,4.2,40.5,16.2 ],[1.69,0.12125,0.097,0.89,6.5,4.6,48.5,19.4],[1.84,0.13125,0.105,0.98,7.0,5.1,48.5,19.4]],[[1,0.085,0.068,0.66,4.3,2.6,42.0,16.8 ],[1.45,0.10625,0.085,0.77,5.1,3.5,48.0,19.2 ],[1.63,0.11375,0.095,0.86,5.7,4.0,59.5,23.8 ],[1.80,0.13125,0.105,0.96,6.1,4.4,61.0,24.4],[1.98,0.1425,0.114,1.05,6.6,4.8,61.0,24.4]],[[1.06,0.1075,0.086,8.5,6.3,3.4,17.5,7.0],[1.47,0.13,0.104,0.97,7.3,4.3,28.0,11.2],[1.65,0.145,0.116,1.09,8.1,4.8,44.5,18.8],[1.83,0.16125,0.129,1.21,8.8,5.3,55.0,22.0],[1.99,0.17375,0.139,1.32,9.4,5.8,55.0,22.0]],[[1.09,0.13125,0.105,0.72,4.1,3.1,18.0,7.2 ],[1.26,0.14875,0.119,0.83,4.6,3.9,28.0,11.2 ],[1.77,0.17625,0.141,0.94,5.4,5.0,45.5,18.2 ],[1.96,0.1925,0.154,1.04,5.9,5.5,56.5,22.6 ],[2.13,0.20875,0.167,2.67,6.3,5.9,35.0,14.0]],[[1.40,0.1875,0.150,3.51,6.0,5.0,35.0,14.0],[1.61,0.2125,0.170,3.22,6.7,5.7,38.8,15.5],[1.80,0.23625,0.189,3.01,7.3,6.3,42.0,16.8],[1.98,0.25625,0.205,2.83,7.9,6.9,45.5,18.2],[2.15,0.2775,0.222,2.69,8.9,7.4,48.8,19.5]]]
#pergunta referente a primeira entrada
print("QUAL E A CLASSE DO ANIMAL?")
print("DIGITE O NUMERO DA OPCAO DESEJADA EM KG")
#lista vazia que ira receber as necessidades do animal escolhido de acordo com sua classe e peso, gerando uma lista de dados
necessidades=[]
alimento=[]
clas=0
# entrada: classe escolhida, tipo do alimento, alimento volumoso, e concentrado(com seus dados)
#esta função faz com que o sistema acesse as listagens que foram compiladas.
for c in range((len(classes))):
    print("({})-{}".format(c,classes[c]))
clas=int(input(">"))
print("ESCOLHA A FAIXA DE PESO EM QUE O ANIMAL SE ENCONTRA(APROXIMADAMENTE), DIGITANDO SEU NUMERO CORRESPONDENTE")
pes=0
for p in range((len(pesos[clas]))):
    print("({})-{}".format(p,pesos[clas][p]))
pes=int(input(">"))
for n in range ((len(valores[clas][pes]))):
    necessidades.append(valores[clas][pes][n])
#caracterização do tipo de alimentação para determinação das porções de concentrado e volumoso. Para cada tipo de alimentação foram colocados os valores que referenciam a matéria seca(%), proteína bruta (%), proteína digestiva(%), fibra digestiva (%), nutrientes digestíveis totais (NDT)(%), cálcio(%) e fósforo(%), respectivamente.
fenos=["ARROZ PALHA","AVEIA FENO","AVEIA FENO","CEVADA FENO","CENTEIO PALHA","FEIJAO FENO","FEIJAO GUANDU FENO CAPIM","JARAGUA FENO CAPIM","MILHO PALHA","SORGO GRANIFERO PALHA","SOJA FENO","SOJA CASCA"]
forragens=["ALFAFA MEDIA","AVEIA ANTES DE ESPIGAR","AZEVEM ITALIANO","BERMUDA PASTO","CAPIM COLONIAO","PASTO CORNICHAO","CAMPIM GUATEMALA","CAPIM IMPERIAL","CAPIM DE RHODES","MANDIOCA RAMA RAIZ","SORGO","TREVO BRANCO"]
silagens=["ALFAFA MELACO","ALFAFA PARTE AEREA","AVEIA","CAPIM ELEFANTE","ERVILHA","MILHO MADURO","MILHO LEITOSO","MILHO ESPIGA","MILHO GRAO DURO","MILHO PE SEM ESPIGA","MILHO<30%MS","SORGO"]
alimentos_vol=[[[91.5, 3.8, 0.6, 32.1, 45.0, 0.22, 0.08],[88.2, 8.1, 3.9, 27.3, 54.0, 0.23, 0.21],[88.2, 8.1, 3.9, 27.3, 54.0, 0.23, 0.21],[87.3, 7.8, 4.4, 23.0, 50.0, 0.18, 0.26],[88.9, 2.7, 0.0, 42.3, 28.0, 0.25, 0.09],[90.5, 16.6, 11.7, 24.7, 57.0, 1.21, 0.29],[81.2, 7.4, 2.8, 25.9, 45.2, 0.22, 0.09],[81.0, 5.8, 1.4, 30.9, 36.7, 0.46, 0.10],[88.9, 3.1, 0.3, 30.7, 67.0, 0.15, 0.12],[85.1, 4.5, 1.5, 27.7, 49.0, 0.34, 0.09],[89.2, 14.5, 9.0, 28.6, 46.0, 1.15, 0.20],[91.3, 12.5, 8.0, 35.5, 41.0, 0.54, 0.16]],[[30.0, 5.4, 3.1, 9.0, 14.0, 1.61, 0.38],[14.1, 3.2, 2.4, 2.8, 9.2, 0.06, 0.09],[24.3, 4.0, 2.4, 5.2, 15.0, 0.16, 0.08],[36.7, 4.2, 2.9, 9.5, 23.0, 0.19,  0.08],[16.7, 2.1, 1.6, 5.1, 0.0, 0.08, 0.02],[20.0, 5.6, 4.6, 2.6, 15.0, 0.44, 0.05],[22.7, 1.9, 1.1, 7.9, 12.6, 0.04, 0.03],[15.4, 1.7, 0.0, 4.2, 0.0, 0.11, 0.08],[24.0, 2.3, 1.3, 8.0, 15.0, 0.10, 0.09],[13.7, 4.4, 0.0, 7.7, 17.9, 0.27, 0.09],[24.9, 1.5, 0.8, 7.0, 17.3, 0.09, 0.03],[16.6, 4.1, 3.3, 2.5, 12.4, 0.21, 0.07]],[[32.2, 5.6, 3.9, 9.3, 19.0, 0.56, 0.10],[30.4, 5.4, 3.6, 9.2, 17.0, 0.49, 0.12],[31.7, 3.1, 1.7, 10.0, 19.0, 0.12, 0.10],[27.1, 1.1, 0.3, 11.8, 11.9, 0.0, 0.0],[24.5, 3.2, 1.9, 7.3, 14.0, 0.32, 0.06],[27.4, 2.2, 1.2, 6.7, 18.1, 0.10, 0.06],[23.1, 1.7, 0.8, 6.3, 16.0, 0.06, 0.06],[43.4, 3.8, 2.1, 5.1, 31.0, 0.03, 0.12],[25.6, 2.2, 1.0, 6.6, 17.0, 0.04, 0.04],[27.2, 2.0, 0.8, 8.7, 16.0, 0.10, 0.05],[27.9, 2.3, 1.4, 7.3, 20.0, 0.08, 0.06],[28.9, 2.3, 0.8, 7.8, 16.0, 0.10, 0.06]]]
nutrientes_fornecidos=[]
tipo_alimento=input("DETERMINE O TIPO DE ALIMENTO VOLUMOSO QUE SERA OFERECIDO AO ANIMAL (FENO, FORRAGEM OU SILAGEM):")
print("QUAL SERA O ALIMENTO?(DIGITE SEU NUMERO CORRESPONDENTES)")

#As condicionais trazem as três listas dos diferentes tipos de alimentação que constam no programa, ao qual na decorrência do código irá formar as recomendações.
if tipo_alimento=="feno":
    ali=0
    for f in range((len(fenos))):
        print("({})-{}".format(f,fenos[f]))
    ali=int(input(">"))
    for c in range((len(alimentos_vol[0][ali]))):
        nutrientes_fornecidos.append(alimentos_vol[0][ali][c])
    for g in fenos:
        alimento.append(g)
elif tipo_alimento=="forragem":
    ali=0
    for f in range((len(forragens))):
        print("({})-{}".format(f,forragens[f]))
    ali=int(input(">"))
    for c in range((len(alimentos_vol[1][ali]))):
        nutrientes_fornecidos.append(alimentos_vol[1][ali][c])
    for g in forragens:
        alimento.append(g)
elif tipo_alimento=="silagem":
    ali=0
    for f in range((len(silagens))):
        print("({})-{}".format(f,silagens[f]))
    ali=int(input(">"))
    for c in range((len(alimentos_vol[2][ali]))):
        nutrientes_fornecidos.append(alimentos_vol[2][ali][c])
    for g in silagens:
        alimento.append(g)
#expeller = alimento animal com o óleo extraido
#esta parte faz as conversões da quantidade de concentrados que serão necessários aos animais.
alimentos_c=["ALGODÃO TORTA EXPELLER","ARROZ FARELO","ARROZ GRAO","AVEIA GRAO","CENTEIO GRAO","CEVADA GRAO","LINHACA TORTA EXPELLER","MILHO AMARELO GRAO","GIRASSOL TORTA EXPELLER","SORGO GRAO","SOJA SEMENTE","TRIGO SARRACENO"]
porcentagens=[[92.4,28.0,19.60,21.4,52,0.17,0.64],[91.0,13.5,8.70,11.0,60,0.06,1.82],[89.0,7.3,5.50,9.0,71,0.04,0.26],[89.0,11.8,8.80,11.0,68,0.10,0.35],[89.0,11.9,9.40,2.0,76,0.06,0.34],[89.0,11.6,8.70,5.0,74,0.08,0.42],[91.0,35.3,31.00,9.0,74,0.87,0.79],[86.0,8.8,6.50,2,0,78,0.03,0.27],[93.0,41.0,36.40,13.0,65,0.43,1.04],[89.0,11.1,6.30,2.0,74,0.04,0.31],[90.0,37.9,34.10,5.0,85,0.25,0.59],[88.0,11.1,6.70,9.0,69,0.11,0.33]]
print("AGORA ESCOLHA UM ALIMENTO CONCENTRADO")
conc=0
for c in range((len(alimentos_c))):
    print("({})-{}".format(c,alimentos_c[c]))
conc=int(input(">"))
nutrientes_concentrados=[]
for num in range((len(porcentagens[conc]))):
    nutrientes_concentrados.append(porcentagens[conc][num])
#calculo, utilizando regra de tres composta, para saber a quantidade de cada alimento, baseando-se na proteína bruta e NDT
volumoso_pb=(nutrientes_fornecidos[1])/100
volumoso_ndt=(nutrientes_fornecidos[4])/100
concentrado_pb=(nutrientes_concentrados[1])/100
concentrado_ndt=(nutrientes_concentrados[4])/100
necessidade_pb=(necessidades[1])
necessidade_ndt=(necessidades[3])
novo_vpb=volumoso_pb*volumoso_ndt
novo_vndt=volumoso_ndt*volumoso_pb
novo_n_pb=necessidade_pb*volumoso_ndt
novo_n_ndt=necessidade_ndt*volumoso_pb
novo_cpb=concentrado_pb*volumoso_ndt
novo_cndt=concentrado_ndt*volumoso_pb
novo_vpb=novo_vpb-novo_vndt
novo_cpd=abs(novo_cpb-novo_cndt)
novo_n_pb=abs(novo_n_pb-novo_n_ndt)
kg_c=(novo_n_pb)/novo_cpb
kg_v=(((necessidade_pb)-(kg_c*concentrado_pb))/volumoso_pb)
kg_v=abs(kg_v)
#cálculo de suplementação animal em relação ao fósforo e calcário
#a suplementação de calcário para ovinos lactantes é de extrema importância
sup=["Acido fosfórico H3PO4","Calcáreo CaCO3"]
suplementos_100=[0.361,0.385]
sup_p=0
sup_ca=0
ca_vol=kg_v*((nutrientes_fornecidos[5])/100)
ca_c=kg_c*((nutrientes_concentrados[5])/100)
p_vol=kg_v*((nutrientes_fornecidos[6])/100)
p_c=kg_c*((nutrientes_concentrados[6])/100)
p_fornecido=p_vol+p_c
ca_fornecido=ca_vol+ca_c
p_faltante=(necessidades[5])-p_fornecido
ca_faltante=(necessidades[4])-ca_fornecido
sup_p=p_faltante/(suplementos_100[0])
sup_ca=ca_faltante/(suplementos_100[1])
print(" \n ")
print("A classe de animal confinado escolhido devera receber {:.2f}kg de alimento volumoso ({}) e {:.2f}kg de alimento concentrado({})".format(kg_v,alimento[ali],kg_c,alimentos_c[conc]))
if sup_p>0:
    print(" \n  ")
    print("Com os alimentos escolhidos será necessária a suplementacao de fósforo(P), com {:.2f}g de {}".format(sup_p,sup[0]))
if sup_ca>0:
    if sup_p>0:
        print("  \n ")
        print("Além disso será necessária a suplementação de cálcio(Ca), com {:.2f}g de {}".format(sup_ca,sup[1]))
    else:
        print(" \n  ")
        print("Com os alimentos de confinamento escolhidos sera necessária a suplementação de cálcio(Ca), com {:.2f}g de {}".format(sup_ca,sup[1]))
print(" \n  ")
fim=input("Digite qualquer tecla para finalizar o programa")