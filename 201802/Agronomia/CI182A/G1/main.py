#título do programa
print("-="*30,"CALCULO NUTRICIONAL DE GADO DE CORTE CONFINADO","=-"*30)
print(" \n ")
#dados referentes as classes dos animais, opcoes de escolha
classes=["acabento_terminacao_bezerros","acabamento_terminacao_bezerros_sobreano","acabamento_terminacao_m_2a","acabamento_terminacao_bezerras","acabamento_terminacao_bezerras_sobreano","crescimento_machos","crescimento_femeas","vacas_adultas_secas_eou_gestacao","vaca_lactacao_3ou4meses_posparto","touros_crescimento_manutencao"]
#matriz com pesos, cada linha representa um animal, e cada coluna sua faixa de peso
pesos=[[150,200,300,400,500],[250,300,400,500],[350,400,500,550],[150,200,300,400],[250,300,400,450],[150,200,300,400],[150,200,300,400],[350,400,450,500,550,600],[350,400,450,500],[400,600,700,900]]
#lista de matrizes, cada matriz é correspondente a classe do animal, cada linha seria o peso e as colunas as necessidades
valores=[[[3.5,0.45,0.30,2.7,21,15,19.5,7.8],[5.0,0.61,0.41,3.7,23,17,27.5,11.0],[7.1,0.87,0.58,5.3,26,19,39.5,15.8],[8.8,0.98,0.62,6.5,25,20,49.5,19.6],[9.4,1.04,0.67,6.9,21,21,52.0,20.8]],[[7.2,0.80,0.51,5.2,29,20,40.0,16.0],[8.3,0.92,0.92,6.0,29,21,46.0,18.4],[10.3,1.14,0.73,7.4,28,23,57.0,22.8],[11.5,1.28,0.82,8.3,26,26,64.0,25.6]],[[10.3,1.14,0.73,7.3,30,24,57.0,22,8 ],[11.3,1.25,0.80,8.0,30,25,63.0,25,2 ],[13.4,1.49,0.95,9.5,30,30,74.5,29,8 ],[13.7,1.52,0.97,9.7,30,30,76.0,30,4 ]],[[3.5,0.45,0.30,2.7,18,13,19.5,7.8 ],[5.0,0.61,0.41,3.7,21,15,27.5,11.0],[7.3,0.89,0.59,5.4,23,18,40.5,16.2 ],[8.7,0.97,0.62,6.4,23,19,48.5,19.4]],[[7.6,0.84,0.54,5.5,27,20,42.0,16.8 ],[8.6,0.95,0.61,6.2,27,20,48.0,19.2 ],[10.7,1.19,0.76,7.7,30,24,59.5,23.8 ],[11.0,1.22,0.78,7.9,24,24,61.0,24.4]],[[3.2,0.43,0.29,2.5,17,13,17.5,7.0],[5.0,0.56,0.36,3.5,18,14,28.0,11.2],[8.0,0.89,0.47,5.0,17,15,44.5,18.8],[9.9,0.88,0.51,6.3,18,18,55.0,22.0]],[[3.2,0.39,0.26,2.3,12,10,18.0,7.2 ],[5.0,0.56,0.36,3.2,13,10,28.0,11.2 ],[8.2,0.82,0.50,4.7,15,15,45.5,18.2 ],[10.2,0.91,0.53,5.8,18,18,56.5,22.6 ]],[[5.8,0.34,0.16,2.8,9,9,35.0,14.0],[6.4,0.38,0.18,3.2,10,10,38.8,15.5],[6.8,0.40,0.19,3.4,12,12,42.0,16.8],[7.6,0.44,0.21,3.8,12,12,45.5,18.2],[8.0,0.47,0.22,4.0,12,12,48.8,19.5],[8.6,0.50,0.24,4.3,13,13,52.0,20.8]],[[8.6,0.79,0.46,4.9,25,20,83.0,33.2],[9.3,0.86,0.50,5.3,25,21,90.0,36.0],[9.9,0.91,0.53,5.6,28,22,96.2,38.5],[10.5,0.97,0.57,6.0,28,23,102.5,41.0]],[[10.0,1.33,0.90,6.5,19,18,85.0,34,0],[11.6,1.42,0.94,6.9,21,21,113.0,45,2],[12.7,1.41,0.90,7.2,23,23,123,5,49.5],[10.7,1.07,0.65,6.1,19,19,104.0,41.6]]]
#pergunta referente a primeira entrada
print("Qual e a classe do animal?")
print("Digite o numero da opcao desejada")
#lista vazia que ir� receber as necessidades do animal escolhido de acordo com sua classe e pes
necessidades=[]
alimento=[]
clas=0
# entrada: classe escolhida, tipo do alimento, alimento volumoso, e concentrado(com seus dados)
for c in range((len(classes))):
    print("({})-{}".format(c,classes[c]))
clas=int(input(">"))
print("Escolha a faixa de peso em que o animal se encontra(aproximadamente), digitando seu numero correspondente")
pes=0
for p in range((len(pesos[clas]))):
    print("({})-{}".format(p,pesos[clas][p]))
pes=int(input(">"))
for n in range ((len(valores[clas][pes]))):
    necessidades.append(valores[clas][pes][n])
fenos=["arroz_palha","aveia_feno","amendoim_casca","cevada_feno","centeio_palha","citrs_poupa","fava_feno","guandu_feno_capim","jaragua_feno_capim","milho_palha","sorgo_granifero_palha","soja_feno","soja_casca"]
forragens=["alfafa_media","aveia_antes_espigar","azevem_italiano","batata_doce_raiz","pasto_bermuda","cenoura_raiz","cornichao_pasto","guatemala_capim","rhodes_capim","mandioca_raiz","sorgo","trevo_branco"]
silagens=["aveia","capim_elefante","ervilha","milho_maduro","milho_leitoso","milho_espiga","capim_pangola","sorgo","alfafa_melaco","citrus_polpa","alfafa_parte_aerea","milho_pe_sem_espiga"]
alimentos_vol=[[[91.5,3.8,0.6,32.1,45.0,0.22,0.08],[88.2,8.1,3.9,27.3,54.0,0.23,0.21],[92.3,6.8,3.0,60.4,7.0,0.23,0.06],[87.3,7.8,4.4,23.0,50.0,0.18,0.26],[88.9,2.7,0.0,42.3,28.0,0.25,0.09],[90.0,6.6,2.9,13.0,75.0,1.96,0.12],[88.2,17.6,11.6,25.1,55.0,1.20,0.30],[81.2,7.4,2.8,25.9,45.2,0.22,0.09],[81.0,5.8,1.4,30.9,36.7,0.46,0.10],[88.9,3.1,0.3,30.7,67.0,0.15,0.12],[85.1,4.5,1.5,27.7,49.0,0.34,0.09],[89.2,14.5,9.0,28.6,46.0,1.15,0.20],[91.3,12.5,8.0,35.5,41.0,0.54,0.16]],[[30.0,5.4,3.1,9.0,14.0,1.61,0.38],[14.1,3.2,2.4,2.8,9.2,0.06,0.09],[24.3,4.0,2.4,5.2,15.0,0.16,0.08],[31.8,1.6,0.2,1.9,25.6,0.03,0.04],[36.7,4.2,2.9,9.5,23.0,0.19,0.08],[11.9,1.2,0.9,1.1,10.3,0.05,0.04],[20.0,5.6,4.6,2.6,15.0,0.44,0.05],[22.7,1.9,1.1,7.9,12.6,0.04,0.03],[24.0,2.3,1.3,8.0,15.0,0.10,0.09],[32.6,1.1,0,1.4,25.7,0,0.04],[24.9,1.5,0.8,7.0,17.3,0.09,0.03],[16.6,4.1,3.3,2.5,12.4,0.21,0.07]],[[31.7,3.1,1.7,10.0,19.0,0.12,0.10],[27.1,1.1,0.3,11.8,11.9,0,0],[24.5,3.2,1.9,7.3,14.0,0.32,0.06],[27.4,2.2,1.2,6.7,18.1,0.10,0.06],[23.1,1.7,0.8,6.3,16.0,0.06,0.06],[43.4,3.8,2.1,5.1,31.0,0.03,0.12],[28.4,1.4,0,8.6,14.5,0,0],[28.9,2.3,0.8,7.8,16.0,0.10,0.06],[32.2,5.6,3.9,9.3,19.0,0.56,0.10],[9.5,1.4,0.4,3.1,17.0,0,0],[30.4,5.4,3.6,9.2,17.0,0.49,0.12],[27.2,2.0,0.8,8.7,16.0,0.10,0.05]]]
nutrientes_fornecidos=[]
tipo_alimento=input("Determine o tipo de alimento volumoso que sera oferecido ao animal (feno, forragem ou silagem):")
print("Qual sera o alimento?(Digite seu numero correspondentes)")

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
alimentos_c=["Algodao_Torta_expeller","Amendoim_Torta_Sovente","Arroz_grao","Aveia_grao","Centeio_grao","Cevada_grao","Linhaca_torta_expeller","Milho_amarelo_grao","Peixe_farinha","Sorgo_grao","Soja_semente","Trigo_sarraceno"]
porcentagens=[[92.4,28.0,19.60,21.4,52,0.17,0.64],[92.0,47.4,42.70,13.0,71,0.20,0.65],[89.0,7.3,5.50,9.0,71,0.04,0.26],[89.0,11.8,8.80,11.0,68,0.10,0.35],[89.0,11.9,9.40,2.0,76,0.06,0.34],[89.0,11.6,8.70,5.0,74,0.08,0.42],[91.0,35.3,31.00,9.0,74,0.87,0.79],[86.0,8.8,6.50,2,0,78,0.03,0.27],[92.0,63.2,58.80,1.0,0,7.86,3.61],[89.0,11.1,6.30,2.0,74,0.04,0.31],[90.0,37.9,34.10,5.0,85,0.25,0.59],[88.0,11.1,6.70,9.0,69,0.11,0.33]]
print("Agora escolha um alimento concentrado")
conc=0
for c in range((len(alimentos_c))):
    print("({})-{}".format(c,alimentos_c[c]))
conc=int(input(">"))
nutrientes_concentrados=[]
for num in range((len(porcentagens[conc]))):
    nutrientes_concentrados.append(porcentagens[conc][num])
#calculo, utilizando regra de tres composta, para saber a quantidade de cada alimento, baseando-se na proteína bruna e ndt
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
#calculo de suplementação
sup=["Acido fosforico H3PO4","Calcáreo CaCO3"]
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
print("O animal escolhido devera receber {:.2f}kg de volumoso ({}) e {:.2f}kg de alimento concentrado({})".format(kg_v,alimento[ali],kg_c,alimentos_c[conc]))
if sup_p>0:
    print(" \n  ")
    print("Com os alimentos escolhidos sera necessaria a suplementacao de fosforo(P), com {:.2f}g de {}".format(sup_p,sup[0]))
if sup_ca>0:
    if sup_p>0:
        print("  \n ")
        print("Alem disso sera necessaria a suplementacao de calcio(Ca), com {:.2f}g de {}".format(sup_ca,sup[1]))
    else:
        print(" \n  ")
        print("Com os alimentos escolhidos sera necessaria a suplementacao de calcio(Ca), com {:.2f}g de {}".format(sup_ca,sup[1]))
print(" \n  ")
fim=input("Digite qualquer tecla para finalizar o programa")
