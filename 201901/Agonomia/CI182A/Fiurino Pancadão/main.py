cult = input("Cultura escolhida:")
ant = input ("Cultura anterior:")
produ = float(input("Produtividade esperada:"))
intP = input ("Para a interpretação do Fosfóro:")
intK = input ("Para a interpretação do Potássio:")
phc = float(input("pH CaCl2:"))
pha = float (input("pH H2O:"))
al = float(input("Aluminio:"))
h = float(input("H+:"))
ca = float(input("Calcio:"))
mg = float(input("Magnésio:"))
na = float(input("Sodio:"))
p = float(input("Fósforo:"))
k = float(input ("Potássio:"))
argila = float(input("Argila:"))
co = float(input("Matéria orgânica:"))
mo = float(input("Matéria orgânica:"))





sb = ca + k + mg + na
ctc = sb + h + al
m = 100*(al/ctc)
v = ( sb * 100)/ctc
t = sb + al



if phc>=6:
    print("pH CaCl2: Condição a evitar")
elif phc>5.5:
    print ("pH CaCl2: Muito alto")
elif phc>=5 and phc<=5.5:
    print ("pH CaCl2: Alto")
elif phc>=4.5 and phc<5:
    print ("pH CaCl2: Médio")
elif phc>=4 and phc<4.5:
    print ("pH CaCl2: Baixo")
else:
    print("pH CaCl2: Muito baixo")

if pha>6.7:
    print("ph H2O: Condição a evitar")
elif pha>6.2:
    print ("ph H2O: Muito alto")
elif pha>=5.7 and pha<=6.2:
    print ("ph H2O: Alto")
elif pha>=5.2 and pha<5.7:
    print ("ph H2O: Médio")
elif pha>=4.7 and pha<5.2:
    print ("ph H2O: Baixo")
else:
    print("ph H2O: Muito baixo")

if al>2.5:
    print ("Al3: Muito alto")
elif al>=1.6 and al<=2.5:
    print ("Al3: Alto")
elif al>=0.8 and al<1.6:
    print ("Al3: Médio")
elif al>=0.3 and al<0.8:
    print ("Al3: Baixo")
else:
    print("Al3: Muito baixo")

if ca>6:
    print ("Ca2: Muito alto")
elif ca>=2.1 and ca<=6:
    print ("Ca2: Alto")
elif ca>=1.1 and ca<2.1:
    print ("Ca2: Médio")
elif ca>=0.5 and ca<1.1:
    print ("Ca2: Baixo")
else:
    print("Ca2: Muito baixo")

if mg>2:
    print ("Mg2: Muito alto")
elif mg>=1.1 and mg<=2:
    print ("Mg2: Alto")
elif mg>=0.5 and mg<1.1:
    print ("Mg2: Médio")
elif mg>=0.2 and mg<0.5:
    print ("Mg2: Baixo")
else:
    print("Mg2: Muito baixo")

if m>50:
    print ("m (%): Muito alto")
elif m>=21 and m<=50:
    print ("m (%): Alto")
elif m>=11 and m<21:
    print ("m (%): Médio")
elif m>=5 and m<11:
    print ("m (%): Baixo")
else:
    print("m (%): Muito baixo")

if v>90:
    print("V (%): Condição a evitar")
elif v>70:
    print ("V (%): Muito alto")
elif v>=51 and v<=70:
    print ("V (%): Alto")
elif v>=36 and v<51:
    print ("V (%): Médio")
elif v>=21 and v<36:
    print ("V (%): Baixo")
else:
    print("V (%): Muito baixo")

if ctc>24:
    print ("T ou CTC a pH 7,0: Muito alto")
elif ctc>=15 and ctc<=24:
    print ("T ou CTC a pH 7,0: Alto")
elif ctc>=8 and ctc<15:
    print ("T ou CTC a pH 7,0: Médio")
elif ctc>=5 and ctc<8:
    print ("T ou CTC a pH 7,0: Baixo")
else:
    print("T ou CTC a pH 7,0: Muito baixo")

if t>8:
    print ("t ou CTC efetiva: Muito alto")
elif t>=4.1 and t<=8:
    print ("t ou CTC efetiva: Alto")
elif t>=2.1 and t<4.1:
    print ("t ou CTC efetiva: Médio")
elif t>=1.1 and t<2.1:
    print ("t ou CTC efetiva: Baixo")
else:
    print("t ou CTC efetiva: Muito baixo")

if co>20:
    print ("CO: Muito alto")
elif co>=15 and co<=20:
    print ("CO: Alto")
elif co>=9 and co<15:
    print ("CO: Médio")
elif co>=4 and co<9:
    print ("CO: Baixo")
else:
    print("CO: Muito baixo")

if mo>3.4:
    print ("MO: Muito alto")
elif mo>=2.5 and mo<=3.4:
    print ("MO: Alto")
elif mo>=1.5 and mo<2.5:
    print ("MO: Médio")
elif mo>=0.7 and mo<1.5:
    print ("MO: Baixo")
else:
    print("MO: Muito baixo")

if intP=="Argila":
    if  argila<250 :
        if p>120 :
            print("P: Condição a evitar")
            auxp="Condição a evitar"
        elif p>24 and p<=120:
            print ("P: Muito alto")
            auxp="Muito alto"
        elif p>=19 and p<=24:
            print ("P: Alto")
            auxp="Alto"
        elif p>=13 and p<19:
            print ("P: Médio")
            auxp="Médio"
        elif p>=6 and p<13:
            print ("P: Baixo")
            auxp="Baixo"
        else:
            print("P: Muito baixo")
            auxp="Muito baixo"

    if  argila>=250 and argila <=400 :
        if p>90 :
            print("P: Condição a evitar")
            auxp="Condição a evitar"
        elif p>18 and p<=90:
            print ("P: Muito alto")
            auxp="Muito alto"
        elif p>=13 and p<=18:
            print ("P: Alto")
            auxp="Alto"
        elif p>=9 and p<13:
            print ("P: Médio")
            auxp="Médio"
        elif p>=4 and p<9:
            print ("P: Baixo")
            auxp="Baixo"
        else:
            print("P: Muito baixo")
            auxp="Muito baixo"

    if  argila>400 :
        if p>60 :
            print("P: Condição a evitar")
            auxp="Condição a evitar"
        elif p>12 and p<=60:
            print ("P: Muito alto")
            auxp="Muito alto"
        elif p>=10 and p<=12:
            print ("P: Alto")
            auxp="Alto"
        elif p>=7 and p<10:
            print ("P: Médio")
            auxp="Médio"
        elif p>=3 and p<7:
            print ("P: Baixo")
            auxp="Baixo"
        else:
            print("P: Muito baixo")
            auxp="Muito baixo"

elif intP=="Olerícolas":
    if p>300:
        print("P: Condição a evitar")
        auxp="Condição a evitar"
    elif p>100 and p<=300:
        print ("P: Muito alto")
        auxp="Muito alto"
    elif p>=51 and p<=100:
        print ("P: Alto")
        auxp="Alto"
    elif p>=21 and p<51:
        print ("P: Médio")
        auxp="Médio"
    elif p>=8 and p<21:
        print ("P: Baixo")
        auxp="Baixo"
    else:
        print("P: Muito baixo")
        auxp="Muito baixo"

elif intP=="Florestais":
    if p>28:
        print("P: Condição a evitar")
        auxp="Condição a evitar"
    elif p>7 and p<=28:
        print ("P: Muito alto")
        auxp="Muito alto"
    elif p>=6 and p<=7:
        print ("P: Alto")
        auxp="Alto"
    elif p>=4 and p<6:
        print ("P: Médio")
        auxp="Médio"
    elif p>=2 and p<4:
        print ("P: Baixo")
        auxp="Baixo"
    else:
        print("P: Muito baixo")
        auxp="Muito baixo"
        
elif intP=="Pastagem":
    if p>40:
        print("P: Condição a evitar")
        auxp="Condição a evitar"
    elif p>10 and p<=40:
        print ("P: Muito alto")
        auxp="Muito alto"
    elif p>=7 and p<=10:
        print ("P: Alto")
        auxp="Alto"
    elif p>=4 and p<7:
        print ("P: Médio")
        auxp="Médio"
    elif p>=2 and p<4:
        print ("P: Baixo")
        auxp="Baixo"
    else:
        print("P: Muito baixo")
        auxp="Muito baixo"
else:
    print("Fora dos parâmetros")

if intK == "K trocável":
    if k>0.45:
        print ("K: Muito alto")
        auxk=("Muito alto")
    elif k>=0.22 and k<=0.45:
        print ("K: Alto")
        auxk="Alto"
    elif k>=0.13 and k<0.22:
        print ("K: Médio")
        auxk="Médio"
    elif k>=0.06 and k<0.13:
        print ("K: Baixo")
        auxk="Baixo"
    elif k<0.06:
        print ("K: Muito baixo")
        auxk="Muito baixo"

elif intK == "Olerícolas, alfafa e café":
    if k>1.2:
        print ("K: Muito alto")
        auxk=("Muito alto")
    elif k>=0.46 and k<=1.2:
        print ("K: Alto")
        auxk="Alto"
    elif k>=0.31 and k<0.46:
        print ("K: Médio")
        auxk="Médio"
    elif k>=0.15 and k<0.31:
        print ("K: Baixo")
        auxk="Baixo"
    elif k<0.15:
        print ("K: Muito baixo")
        auxk="Muito baixo"
else:
    print("Fora dos parâmetros")

if cult == "milho":
    if ant == "Gramínea" and produ < 8:
        print("Adubação nitrogenada : 80 à 120 Kg/ha")
    elif ant == "Gramínea" and produ >= 8 and produ <= 12:
        print("Adubação nitrogenada : 121 à 180 Kg/ha")
    elif ant == "Gramínea" and produ >= 13 and produ <= 16:
        print("Adubação nitrogenada : 181 à 260 Kg/ha")
    elif ant == "Gramínea" and produ > 16:
        print("Adubação nitrogenada : 261 à 340 Kg/ha")
    elif ant == "Leguminosa" and produ < 8:
        print("Adubação nitrogenada : 20 à 60 Kg/ha") 
    elif ant == "Leguminosa" and produ >= 8 and produ <= 12:
        print("Adubação nitrogenada : 61 à 120 Kg/ha")
    if produ <8:
        if auxp == "Muito baixo":
            print ("Adubação fosfatada : 110 à 130 Kg/ha")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : 90 à 110 Kg/ha")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 70 à 90 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 50 à 70 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 30 à 50 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >= 8 and produ <= 12:
        if auxp=="Muito baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : 111 à 130 Kg/ha")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 91 à 110 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 71 à 90 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 51 à 70 Kg/ha")
        else:
            print ("Condição  evitar")
    
    if produ >= 13 and produ <= 16:
        if auxp == "Muito baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : 131 à 150 Kg/ha")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 111 à 130 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 91 à 110 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 71 à 90 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >16:
        if auxp == "Muito baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 131 à 150 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 111 à 130 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 91 à 110 Kg/ha")
        else :
            print ("Condição  evitar")
    if produ <8:
        if auxk == "Muito baixo":
            print ("Adubação potássica : 110 à 130 Kg/ha")
        elif auxk == "Baixo":
            print ("Adubação potássica : 70 à 100 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 40 à 70 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 20 à 40 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 20 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >= 8 and produ <= 12:
        if auxk == "Muito baixo":
            print ("Adubação potássica : Inviavél")
        elif auxk == "Baixo":
            print ("Adubação potássica : 101 à 130 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 71 à 100 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 41 à 70 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 20 à 41 Kg/ha")
        else :
            print ("Condição  evitar")
    
    if produ >= 13 and produ <= 16:
        if auxk == "Muito baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxk == "Baixo":
            print ("Adubação potássica : 131 à 160 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 101 à 130 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 71 à 100 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 41 à 70 Kg/ha")
        else :
            print ("Condição  evitar")
    if produ > 16:
        if auxk=="Muito baixo":
            print ("Adubação potássica : Inviavél")
        elif auxk == "Baixo":
            print ("Adubação potássica : 161 à 190 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 131 à 160 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 101 à 130 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 71 à 100 Kg/ha")
        else :
            print ("Condição  evitar " )
elif cult=="Soja":
    print ("Não a necessidade de adubção nitrogenada na soja.")
    if produ < 3:
        if auxp == "Muito baixo":
            print ("Adubação fosfatada : 81 à 100 Kg/ha")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : 61 à 80 Kg/ha")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 41 à 60 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 20 à 40 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 0 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >= 3 and produ <= 4:
        if auxp=="Muito baixo":
            print ("Adubação fosfatada : 101 à 120 Kg/ha")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : 81 à 100 Kg/ha")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 61 à 80 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 41 à 60 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 20 à 40 Kg/ha")
        else :
            print ("Condição  evitar " )
    
    if produ > 4 and produ <= 5:
        if auxp=="Muito baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : 101 à 120 Kg/ha")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 81 à 100 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 61 à 80 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 41 à 60 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >5:
        if auxp == "Muito baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Baixo":
            print ("Adubação fosfatada : Inviavél")
        elif auxp == "Médio":
            print ("Adubação fosfatada : 101 à 120 Kg/ha")
        elif auxp == "Alto":
            print ("Adubação fosfatada : 81 à 100 Kg/ha")
        elif auxp == "Muito alto":
            print ("Adubação fosfatada : 61 à 80 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ <3:
        if auxk == "Muito baixo":
            print ("Adubação potássica : 81 à 100 Kg/ha")
        elif auxk == "Baixo":
            print ("Adubação potássica : 61 à 80 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 41 à 60 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 20 à 40 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 0 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >= 3 and produ <= 4:
        if auxk=="Muito baixo":
            print ("Adubação fosfatada : 101 à 120 Kg/ha")
        elif auxk == "Baixo":
            print ("Adubação potássica : 81 à 100 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 61 à 80 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 41 à 60 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 20 à 40 Kg/ha")
        else :
            print ("Condição  evitar " )
    
    if produ >4 and produ <= 5:
        if auxk == "Muito baixo":
            print ("Adubação potássica : Inviavél")
        elif auxk == "Baixo":
            print ("Adubação potássica : 101 à 120 Kg/ha")
        elif auxk == "Médio":
            print ("Adubação potássica : 81 à 100 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 61 à 80 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 41 à 60 Kg/ha")
        else :
            print ("Condição  evitar " )
    if produ >5:
        if auxk == "Muito baixo":
            print ("Adubação potássica : Inviavél")
        elif auxk == "Baixo":
            print ("Adubação potássica : Inviavél")
        elif auxk == "Médio":
            print ("Adubação potássica : 101 à 120 Kg/ha")
        elif auxk == "Alto":
            print ("Adubação potássica : 81 à 100 Kg/ha")
        elif auxk == "Muito alto":
            print ("Adubação potássica : 61 à 80 Kg/ha")
        else :
            print ("Condição  evitar " )
            

vescolhido = int(input("Saturação por base em % :"))
prnt = int(input("Poder de reação do calcario:"))
calagem = ((vescolhido-v)*ctc)/prnt
print("Necessidade de calagem:", calagem, "t/ha")















        















