from random import choice
listapalavras=['banana','carro','cachorro','agronomia','maquete','banoffe','curitiba']
palavra=choice(listapalavras)
charada=[]
letrasErradas =[]
for letra in palavra:
    charada.append(letra)
vazio=['_']*(len(charada))
k=0
m=0
palpite=str(input("Chute uma letra:"))
while k<6 and m<(len(charada)):
    j=0
    i=0
    while i<(len(charada)):
        if palpite == charada[i]:
            m=m+1
            vazio.pop(i)
            vazio.insert(i,palpite)
            print(vazio)
            i=i+1
            j=j+1
        else:
            i=i+1
    if j==0:
        letrasErradas.append(palpite)
        k=k+1
        print("Você tem mais {0} chances".format(7-k))
    elif m==len(charada):
        print("Parabéns! Você acertou! :)")
        print("A palavra certa era: {0}".format(charada))
        break
    print("Letras Erradas: {0}".format(letrasErradas))
    palpite=str(input("Chute uma letra:"))
else:
    print("Acabaram suas chances! :(")
    print("A palavra certa era: {0}".format(charada))