produto=int(input("Qual o produto desejado?\nHerbicida? digite-1\nFungicida? digite-2\nFertilizante? digite-3\nInseticida? digite-4\n" ))   #produtos selecionados
v=[]
print("______________________________________________")  #linha decorativa
if produto==1: #herbicida
    v.append("corredor 1")
    cultura=int(input("qual cultura de manejo?\n soja? digite=1\n milho? digite=2\n feijão? digite=3\n café? digite=4\n"))    #culturas escolhidas
    if cultura ==1:
        v.append("estante mais alta")
    elif cultura==2:
        v.append("3ª estante de baixo pra cima")
    elif cultura==3:
        v.append("2ª estante de baixo pra cima")
    elif cultura==4:
        v.append("1ª estante de baixo pra cima")
    else:
        print("não temos esse produto em nosso galpão")
    print("______________________________________________")   
    daninha=int(input("qual a erva daninha está causando problemas?\n tiririca(Cyperus spp.)? digite=1\n picão preto(Bidens pilosa)? digite=2\n dente de leão(Taraxacum officinale)? digite=3\n barba de bode(Cyperus rotundus? digite=4\n"))  #itens escolhidas
    if daninha==1 :
        v.append("gaveta 2")
    elif daninha==2 :
        v.append("gaveta 1")
    elif daninha==3:
        v.append ("gaveta 3")
    elif daninha ==4:
        v.append("gaveta 4")
    else:
        print("não temos em nosso galpão")
elif produto==2:
    v.append("corredor 2")
    cultura =int(input("qual cultura de manejo?\n soja? digite=1\n milho? digite=2\n feijão? digite=3\n café? digite=4\n"))
    if cultura == 1:
        v.append("estante mais alta")
    elif cultura == 2:
        v.append("3ª estante de baixo pra cima")
    elif cultura == 3:
        v.append("2ª estante de baixo pra cima")
    elif cultura ==4:
        v.append("1ª estante de baixo pra cima")
    else:
        print(("não temos esse produto em nosso galpão"))
    print("______________________________________________")
    fungo=int(input("qual o fungo causador de problema?\n Aschersonia aleyrodis? digite=1\n Beauveria bassiana? digite=2\n Metarhizium anisopliae? digite=3\n Hirsutella sp.? digite=4\n"))
    if fungo == 1:
        v.append("gaveta 2")
    elif fungo == 2:
        v.append("gaveta 1")
    elif fungo == 3:
        v.append("gaveta 3")
    elif fungo==4:
        v.append("gaveta 4")
    else:
        print("nao temos esse produto em nosso galpão")
elif produto==3:
    v.append("corredor3")
    cultura =int(input("qual cultura de manejo?\n soja? digite=1\n milho? digite=2\n feijão? digite=3\n café? digite=4\n"))
    if cultura == 1:
        v.append("estante mais alta")
    elif cultura == 2:
        v.append("3ª estante de baixo pra cima")
    elif cultura == 3:
        v.append("2ª estante de baixo pra cima")
    elif cultura ==4:
        v.append("1ª estante de baixo pra cima")
    else:
        print("não temos esse produto em nosso galpão")
    print("______________________________________________")
    fertilizante=int(input("qual o nutriente a planta está necessitando?\n potássio? digite=1\n nitrogênio? digite=2\n fósforo? digite=3\n enxofre? digite=4\n"))
    if fertilizante == 1:
        v.append("gaveta 2")
    elif fertilizante == 2:
        v.append("gaveta 1")
    elif fertilizante == 3:
        v.append("gaveta 3")
    elif fertilizante ==4:
        v.append("gaveta 4")
    else:
        print("não temos esse produto em nosso galpão")
elif produto==4:
    v.append("corredor 4")
    cultura =int(input("qual cultura de manejo?\n soja? digite=1\n milho? digite=2\n feijão? digite=3\n café? digite=4\n"))
    if cultura == 1:
        v.append("estante mais alta")
    elif cultura == 2:
        v.append("3ª estante de baixo pra cima")
    elif cultura == 3:
        v.append("2ª estante de baixo pra cima")
    elif cultura ==4:
        v.append("1ª estante de baixo pra cima")
    else:
        print("não temos esse produto em nosso galpão")
    print("______________________________________________")
    inseto=int(input("qual o inseto está se tornando praga na plantação?\n formiga? digite=1\n mosca bran? digite=2\n broca do milho? digite=3\n lagarta da espiga? digite=4\n"))
    if inseto==1:
        v.append("gaveta 2")
    elif inseto==2:
        v.append("gaveta 1")
    elif inseto == 3:
        v.append("gaveta 3")
    elif inseto==4:
        v.append("gaveta 4")
    else:
        print("não temos esse produto em nosso galpão")
else:
    print("digite um número válido. não possuímos esse produto em nosso galpão!")
print("o seu produto está:{}".format(v))
fim=input("-FIM-")
