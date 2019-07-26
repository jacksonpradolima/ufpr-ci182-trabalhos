def eh_numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def achar(item,lista):
    a=0
    for c in range(len(lista)):
        if item==lista[c]:

            a=c
            int(a)
    return a
print("=-"*30,"CALCULO DE ADUBAÇÃO COM BASE NA ANÁLISE DO SOLO","-="*30)
resposta="s"
while resposta=="s":
    #CORREÇÃO DO pH
    smp=input("Digite o nível smp do solo analisado:")
    teste0=0
    indice_smp = [4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2,6.3, 6.4, 6.5, 6.6, 6.7,6.8, 6.9, 7.0]
    while teste0==0:
        if eh_numero(smp) ==True:
            smp=float(smp)
        if eh_numero(smp)==False:
            print("A opção deve se um número 4.4 até 7")
            smp = (input("Digite uma opção válida:"))
        elif smp not in indice_smp:
            print("O indice deve ser de 4.4 até 7")
            smp = (input("Digite uma opção válida:"))
        elif eh_numero(smp)==True and smp in indice_smp:
            float(smp)
            informacao_ph=input("Mostrar recomendação de pH por cultura?(se sim digite 's' ou aperte enter para continuar)")
            if informacao_ph=="s":

                ph0=["abacaxi","batatinha",]
                ph1=["abacateiro","abóbora","alface","alho","amendoim","bananeira","batata doce","beterraba","brócolis","canola","cebola","cenoura","chicória","couve-flor","ervilha","feijão","fumo","girassol","melancia","melão","milho","moranga","morango","pepino","pimentão","rabanete","repolho"]
                ph2=["alfafa","aspargo"]
                ph3=["erva mate","mandioca"]
                print(f"Culturas com pH ótimo igual a 5,5:{ph0[0]},{ph0[1]}")
                print(f"Culturas com pH ótimo igual a 6,0:")
                i=0
                while i<(len(ph1)-1):
                    if i % 2 == 0:
                        print(ph1[i],",",ph1[(-1)-i],",",end="",)
                    else:
                        print(ph1[i], ph1[(-1) - i])
                    i+=1
                for c in range (len(ph0),0):
                    print(c)
                print(f"Culturas com pH ótimo igual a 6,5:{ph2[0]},{ph2[1]}")
                print(f"Culturas em que não se recomenda a calagem:{ph3[0]},{ph3[1]}")
            print("Qual é o pH que se deseja atingir?")
            ph = [5.5, 6.0, 6.5]
            for c in range(len(ph)):
                print([c],ph[c])
            ph_desejado = int(input("Digite o número correspondente:"))
            l=0
            while l==0:
                if ph_desejado==0 or ph_desejado==1 or ph_desejado==2:
                    l+=1
                else:
                    ph_desejado=int(input("Opção não existente, escolha outra:"))
            teste0 += 1
            t_ha_ph=[[15.0,12.5,10.9,9.6,8.5,7.7,6.6,6.0,5.3,4.8,4.2,3.7,3.2,2.8,2.3,2.0,1.6,1.3,1.0,0.8,0.6,0.4,0.2,0.0,0.0,0.0,0.0],[21.0,17.3,15.1,13.3,11.9,10.7,9.9,9.1,8.3,7.5,6.8,6.1,5.4,4.8,4.2,3.7,3.2,2.7,2.2,1.8,1.4,1.1,0.8,0.5,0.3,0.2,0.0],[29.0,24.0,20.0,17.5,15.7,14.2,13.3,12.3,11.3,10.4,9.5,8.6,7.8,7.0,6.3,5.6,4.9,4.3,3.7,3.1,2.6,2.1,1.6,1.2,0.8,0.5,0.2]]
            calagem=t_ha_ph[ph_desejado][achar(smp,indice_smp)]#CALCARIO

    #nitrogênio
    tipo_cultura=["graminea","leguminosa"]
    cultura=[["abacaxi","alho","cebola","milho"],["alfafa","aspargo","erva mate","mandioca","batatinha","abacateiro","abóbora","alface","amendoim","bananeira","batata doce","beterraba","brócolis","canola","cenoura","chicória","couve-flor","ervilha","feijão","fumo","girassol","melancia","melão","moranga","morango","pepino","pimentão","rabanete","repolho"]]
    informação_tipo=input("Quer exemplos das culturas e suas classificações?(se sim digite 's' ou aperte enter para continuar)")
    cultura=[["abacaxi","alho","cebola","milho"],["alfafa","aspargo","erva mate","mandioca","batatinha","abacateiro","abóbora","alface","amendoim","bananeira","batata doce","beterraba","brócolis","canola","cenoura","chicória","couve-flor","ervilha","feijão","fumo","girassol","melancia","melão","moranga","morango","pepino","pimentão","rabanete","repolho"]]
    if informação_tipo=="s":
        print(f"{tipo_cultura[0]}: {cultura[0]}")
        print(f"{tipo_cultura[1]}:")
        x=0
        while x < (len(cultura[1]) - 1):
            if x % 2 == 0:
                print(cultura[1][x], ",", cultura[1][(-1) - x], ",", end="", )
            else:
                print(cultura[1][x], cultura[1][(-1) - x])
            x += 1
    tipo=input(f"Qual é a classificação da cultura?({tipo_cultura[0]} ou {tipo_cultura[1]}):")
    z=0
    while z==0:
        if tipo in tipo_cultura:
            z+=1
        else:
            tipo=input("Classificação não existente, escolha de novo:")
    #if tipo in tipo_cultura:
    mo=[2.5,2.6-5,5]#%
    materia_organica=int(input(f"Indique a porcentagem de matéria organica\n[0](<=2,5)\n[1](2,6-5)\n[2](>5):"))
    #kg de N/ha em fução do teor de matéria orgânica no solo
    kg_n=0
    if tipo==tipo_cultura[0]:
        gram_n=[80,60,20]
        kg_n=gram_n[materia_organica]
    elif tipo==tipo_cultura[1]:
        leg_n=[60,40,20]
        kg_n=leg_n[materia_organica]
    #ureia ´um adubo nidrogenado com 45% de nitrogenio
    kg_ureia=kg_n/0.45

    #fosforo e potássio
    def rec_P(fosforo):#mg/dm3
        niveis = ["muito baixo", "baixo", "médio", "alto", "muito alto"]
        recomendacao_P = [90, 60, 45, 30, 10]
        if fosforo<3:
            nivel=niveis[0]
            recomendado_p=recomendacao_P[0]
        elif fosforo>=3 and fosforo<5:
            nivel=niveis[1]
            recomendado_p=recomendacao_P[1]
        elif fosforo>= 5 and fosforo<8:
            nivel=niveis[2]
            recomendado_p=recomendacao_P[2]
        elif fosforo>=8 and fosforo<10:
            nivel=niveis[3]
            recomendado_p=recomendacao_P[3]
        elif fosforo>=10 and fosforo<13:
            nivel=niveis[4]
            recomendado_p=recomendacao_P[4]
        elif fosforo>13:
            nivel=niveis[4]
            recomendado_p=recomendacao_P[4]
        return nivel,recomendado_p#kg/ha
    def rec_K(patassio):#mg/dm3
        niveis = ["muito baixo", "baixo", "médio", "alto", "muito alto"]
        recomendacao_K=[80,50,35,20,5]
        if patassio < 3:
            nivel = niveis[0]
            recomendado_k = recomendacao_K[0]
        elif patassio >= 3 and patassio < 5:
            nivel = niveis[1]
            recomendado_k = recomendacao_K[1]
        elif patassio>= 5 and patassio < 8:
            nivel = niveis[2]
            recomendado_k = recomendacao_K[2]
        elif patassio >= 8 and patassio < 10:
            nivel = niveis[3]
            recomendado_k = recomendacao_K[3]
        elif patassio >= 10 and patassio < 13:
            nivel = niveis[4]
            recomendado_k = recomendacao_K[4]
        elif patassio>13:
            nivel = niveis[4]
            recomendado_k = recomendacao_K[4]
        return nivel, recomendado_k#kg/ha
    p=float(input("Qual é a quantidade de fósforo em mg/dm3:"))
    k=float(input("Qual é a quantidade de potássio em mg/dm3:"))
    nivel_p,quantidade_p=rec_P(p)#kg de Mono-Amônio-Fosfato(P2O5) por hectare
    nivel_k,quantidade_k=rec_K(k)#kg de oxido de potassio(K2O) por hectare
    print(f"Resultado da recomendação pré plantio:\nCALAGEM: aplicar {calagem} toneladas de calcario por hectare\nNITROGÊNIO: aplicar {kg_ureia:.2f}kg de ureia por hectare")
    print(f"FOSFORO: o nível de fòsforo esta {nivel_p}, serão necessarios {quantidade_p}kg de Mono-Amônio-Fosfato(P2O5) por hectare")
    print(f"POTASSIO: o nível de potassio esta {nivel_k}, serão necessarios {quantidade_k}de oxido de potassio(K2O) por hectare")
    resposta=input("Caso queira fazer outro calculo digite 's', ou clique enter para finalizar")