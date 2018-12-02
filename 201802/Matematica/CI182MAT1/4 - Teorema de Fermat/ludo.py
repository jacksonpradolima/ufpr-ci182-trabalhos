import turtle


#=========================criando a tartaruga azul=======================#

turtle_blue=turtle.Turtle()
turtle_blue.shape("turtle")
turtle_blue.color("black","blue")
turtle_blue.speed(25)
turtle_blue.up()
turtle_blue.goto(120,-200)
turtle_blue.left(90)



#=========================criando a tartaruga amarela====================#

turtle_yellow=turtle.Turtle()
turtle_yellow.shape("turtle")
turtle_yellow.color("black","yellow")
turtle_yellow.speed(25)
turtle_yellow.up()
turtle_yellow.goto(-240,-200)
turtle_yellow.left(90)


#=========================criando a tartaruga verde=======================#

turtle_green=turtle.Turtle()
turtle_green.shape("turtle")
turtle_green.color("black","green")
turtle_green.speed(25)
turtle_green.up()
turtle_green.goto(-240,160)
turtle_green.right(90)

#=========================criando a tartaruga vervelha====================#

turtle_red=turtle.Turtle()
turtle_red.shape("turtle")
turtle_red.color("black","red")
turtle_red.speed(25)
turtle_red.up()
turtle_red.goto(120,160)
turtle_red.right(90)
#============================criando a tartaruga dado======================#

turtle_dado=turtle.Turtle()
turtle_dado.shape("classic")
turtle_dado.speed(25)
turtle_dado.up()

#================================================criando o tabuleiro==============================================# 

tabuleiro = turtle.Turtle() #criando um "nome" para o modulo turtle 

 

tabuleiro.shape("turtle") #escolhe a caneta 

tabuleiro.speed(11) #velocidade da tartaruga 

tabuleiro.color("blue","blue") #cores do polígono 

tabuleiro.begin_fill() #inicia o preenchimento do polígono 

 

             #1=40 unidades 

 #tabuleiro azul 

 

tabuleiro.forward(200)#200 unidades para frente 

tabuleiro.right(90) #90 graus para a direitA 

tabuleiro.forward(80) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) #90 graus para a esquerda 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

 

 

tabuleiro.right(135) #início do triângulo 

tabuleiro.forward(85) 

tabuleiro.right(90) 

tabuleiro.forward(85) 

tabuleiro.right(135) 

tabuleiro.forward(40) 

 

tabuleiro.end_fill() #Termina o preenchimento do polígono 

#________________________________________________________________ 

 

#tabuleiro amarelo 

 

tabuleiro.up()#levanta a caneta 

tabuleiro.forward(80) 

tabuleiro.right(135) 

 

 

tabuleiro.begin_fill() 

 

tabuleiro.down() #abaixa a caneta 

tabuleiro.color("yellow" , "yellow") #mudando a cor da caneta 

tabuleiro.forward(85) 

tabuleiro.left(90) 

tabuleiro.forward(85) 

tabuleiro.left(135) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(160) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(80) 

tabuleiro.left(90) 

tabuleiro.forward(200) 

 

tabuleiro.end_fill() 

#________________________________________________________________ 

 

#tabuleiro verde 

 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.left(135) 

tabuleiro.forward(85) 

tabuleiro.color("green","green") #mudando a cor da caneta 

 

tabuleiro.begin_fill() 

 

tabuleiro.forward(85) 

tabuleiro.left(135) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(160) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(80) 

tabuleiro.left(90) 

tabuleiro.forward(200) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

 

tabuleiro.end_fill() 

#___________________________________________________________ 

 

#tabuleiro vermelho 

 

tabuleiro.left(135) 

tabuleiro.forward(85) 

tabuleiro.color("red","red") #mudando a cor da caneta 

 

tabuleiro.begin_fill() 

 

tabuleiro.forward(85) 

tabuleiro.left(135) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(160) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(80) 

tabuleiro.left(90) 

tabuleiro.forward(200) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

 

tabuleiro.end_fill() 

#_________________________________________________________ 

 

#delimitando o tabuleiro 

 

tabuleiro.up() #levanta a caneta 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.down() #abaixa a caneta 

 

tabuleiro.color("black") #mudando a cor da caneta 

 

for i in range(0,4): 

    tabuleiro.left(90) 

    tabuleiro.forward(600) 

     

#fazendo as bases 

 

#verde 

     

tabuleiro.begin_fill() 

 

tabuleiro.color("black","green") 

tabuleiro.right(180) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.up() 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.down() 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.up() 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.down() 

 

tabuleiro.end_fill() 

 

#amarela 

 

tabuleiro.up() 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.down() 

 

tabuleiro.begin_fill() 

 

tabuleiro.color("black" , "yellow") 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.up() 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.down() 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.up() 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.down() 

 

tabuleiro.end_fill() 

 

# azul 

 

tabuleiro.up() 

tabuleiro.left(180) 

tabuleiro.forward(360) 

tabuleiro.down() 

 

tabuleiro.begin_fill() 

 

tabuleiro.color("black" , "blue") 

 

tabuleiro.left(90) 

tabuleiro.forward(200) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.up() 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.down() 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

tabuleiro.left(90) 

tabuleiro.forward(160) 

 

tabuleiro.end_fill() 

 

# vermelho 

 

tabuleiro.up() 

tabuleiro.left(180) 

tabuleiro.forward(320) 

tabuleiro.right(90) 

tabuleiro.down() 

 

tabuleiro.begin_fill() 

 

tabuleiro.color("black" , "red") 

tabuleiro.forward(200) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.up() 

tabuleiro.forward(40) 

tabuleiro.down() 

tabuleiro.forward(160) 

tabuleiro.right(90) 

tabuleiro.forward(160) 

tabuleiro.right(90) 

tabuleiro.forward(160) 

tabuleiro.right(90) 

tabuleiro.forward(160) 

 

tabuleiro.end_fill() 

 

#fazendo os quadradinhos 

 

tabuleiro.color("black") 

 

#divisão azul e vermelho 

 

tabuleiro.up() 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.down() 

 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

 

#divisão verde e amarelo 

 

tabuleiro.up() 

tabuleiro.left(180) 

tabuleiro.forward(360) 

tabuleiro.down() 

 

tabuleiro.forward(240) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

 

#divisão verde e vermelho 

 

tabuleiro.up() 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(200) 

tabuleiro.down() 

 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(240) 

tabuleiro.left(180) 

 

# divisão amarelo e azul 

 

tabuleiro.up() 

tabuleiro.forward(360) 

tabuleiro.down() 

 

tabuleiro.forward(240) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(240) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120) 

tabuleiro.left(90) 

tabuleiro.forward(40) 

tabuleiro.left(90) 

tabuleiro.forward(120) 

tabuleiro.right(90) 

tabuleiro.forward(40) 

tabuleiro.right(90) 

tabuleiro.forward(120)

tabuleiro.left(90)

tabuleiro.forward(40)

tabuleiro.right(90)

tabuleiro.forward(240)

tabuleiro.right(90)

tabuleiro.forward(600)



tabuleiro.up()

tabuleiro.right(90)

tabuleiro.forward(75)

tabuleiro.right(90)

tabuleiro.forward(125)

tabuleiro.down()

tabuleiro.begin_fill()

tabuleiro.color("white","white")

tabuleiro.up()




#=====================================turtle dado==================================#

turtle_dado.shape("turtle")
turtle_dado.left(90)
turtle_dado.forward(40)
turtle_dado.right(90)
turtle_dado.forward(280)
turtle_dado.down()
turtle_dado.forward(120)
turtle_dado.right(90)
turtle_dado.forward(240)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(240)
turtle_dado.right(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.right(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.right(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
for x in range(0,4):
    turtle_dado.forward(120)
    turtle_dado.left(90)
turtle_dado.right(90)
turtle_dado.forward(120)
turtle_dado.left(90)
turtle_dado.forward(120)
turtle_dado.right(90)
turtle_dado.forward(120)



#===========montando os valores========#
turtle_dado.up()
turtle_dado.shape("circle")
turtle_dado.color("black","orange")
turtle_dado.back(20)
turtle_dado.right(90)
turtle_dado.forward(20)
turtle_dado.stamp()
for x in range(0,3):
    turtle_dado.forward(80)
    turtle_dado.right(90)
    turtle_dado.stamp()
    
turtle_dado.forward(40)
turtle_dado.right(90)
turtle_dado.forward(40)
turtle_dado.stamp()
turtle_dado.forward(40)
turtle_dado.right(90)
turtle_dado.forward(80)
turtle_dado.stamp()
turtle_dado.forward(40)
turtle_dado.stamp()
turtle_dado.forward(40)
turtle_dado.stamp()
turtle_dado.right(90)
turtle_dado.forward(80)
turtle_dado.right(90)
turtle_dado.stamp()
turtle_dado.forward(40)
turtle_dado.stamp()
turtle_dado.forward(40)
turtle_dado.stamp()
turtle_dado.right(90)
turtle_dado.forward(80)
turtle_dado.right(90)
turtle_dado.forward(120)


turtle_dado.stamp()
turtle_dado.right(45)
turtle_dado.forward(120)
turtle_dado.stamp
turtle_dado.right(45)
turtle_dado.stamp()
turtle_dado.forward(40)

for x in range(0,4):
    turtle_dado.stamp()
    turtle_dado.forward(80)
    turtle_dado.right(90)
turtle_dado.right(90)
turtle_dado.forward(80)

turtle_dado.right(90)
turtle_dado.forward(240)
turtle_dado.right(135)
turtle_dado.stamp()
turtle_dado.forward(60)
turtle_dado.stamp()
turtle_dado.forward(50)
turtle_dado.stamp()

turtle_dado.right(45)
turtle_dado.forward(80)
turtle_dado.left(90)
turtle_dado.forward(80)
turtle_dado.stamp()

#=============================================funçoes dado================================================#

def dado_turtle(dado,vez):
    turtle_dado.speed(2)
    if dado==6:
        if vez=="Blue":

            turtle_dado.color("black","blue")
            
        elif vez=="Yellow":

            turtle_dado.color("black","yellow")

        elif vez=="Green":

            turtle_dado.color("black","green")
            
        if vez=="Red":

            turtle_dado.color("black","red")
            
        turtle_dado.shape("turtle")
        
        turtle_dado.goto(460,-20)

    elif dado==5:

        if vez=="Blue":

            turtle_dado.color("black","blue")
            
        elif vez=="Yellow":

            turtle_dado.color("black","yellow")

        elif vez=="Green":

            turtle_dado.color("black","green")
            
        if vez=="Red":

            turtle_dado.color("black","red")

        turtle_dado.shape("turtle")
        
        turtle_dado.goto(460,-160)
        
    elif dado==4:

        if vez=="Blue":

            turtle_dado.color("black","blue")
            
        elif vez=="Yellow":

            turtle_dado.color("black","yellow")

        elif vez=="Green":

            turtle_dado.color("black","green")
            
        if vez=="Red":

            turtle_dado.color("black","red")

        turtle_dado.shape("turtle")
        turtle_dado.goto(580,100)
        
    elif dado==3:

        if vez=="Blue":

            turtle_dado.color("black","blue")
            
        elif vez=="Yellow":

            turtle_dado.color("black","yellow")

        elif vez=="Green":

            turtle_dado.color("black","green")
            
        if vez=="Red":

            turtle_dado.color("black","red")

        turtle_dado.shape("turtle")

        turtle_dado.goto(340,120)
        
    elif dado==2:

        if vez=="Blue":

            turtle_dado.color("black","blue")
            
        elif vez=="Yellow":

            turtle_dado.color("black","yellow")

        elif vez=="Green":

            turtle_dado.color("black","green")
            
        if vez=="Red":

            turtle_dado.color("black","red")

        turtle_dado.shape("turtle")
        
        turtle_dado.goto(460,120)
        
    else:

        if vez=="Blue":

            turtle_dado.color("black","blue")
            
        elif vez=="Yellow":

            turtle_dado.color("black","yellow")

        elif vez=="Green":

            turtle_dado.color("black","green")
            
        if vez=="Red":

            turtle_dado.color("black","red")
            
        turtle_dado.shape("turtle")
        turtle_dado.goto(460,240)


from random import* #importando random (aleatório)


#===================criando uma lista tabuleiro====================#

lista_tabuleiro=["início"]

for x in range(0,62): #caminho para percorrer ("tabuleiro")
    x="~"
    lista_tabuleiro.append(x)

#=====================criando uma lista das esquinas===================#

lista_esquina=["início"]
for x in range(0,62):
    x="^"
    lista_esquina.append(x)
    
lista_esquina[3]="E"
lista_esquina[9]="E"
lista_esquina[15]="E"
lista_esquina[17]="E"
lista_esquina[23]="E"
lista_esquina[29]="E"
lista_esquina[31]="E"
lista_esquina[37]="E"
lista_esquina[43]="E"
lista_esquina[45]="E"
lista_esquina[51]="E"
lista_esquina[56]="E"
lista_esquina[57]="E"


#===============================funçoes para os bonequinhos andarem======================================#

def bonequinho_azul(b,andar):
    turtle_blue.speed(2)
    turtle_blue.shape("turtle")
    turtle_blue.color("Black","Blue")
    lista_auxiliar=[]
    for x in range(b+1,andar+b+1):
        lista_auxiliar.append(lista_esquina[x])
        
    if b==0:
        turtle_blue.goto(220,-100) #início azul
        turtle_blue.forward(andar*40)
        

    elif lista_auxiliar.count("E")!=0:
       
        if lista_auxiliar.count("E")==1:

            for x in range(b+1,b+andar+1):

                if lista_esquina[x]=="E":

                    if x==9 or x==23 or x==37 or x==51:

                        #turtle_azul.onclick(posicao1)
                    
                        posicao_esquina=lista_esquina.index("E",b+1,b+andar+1)
                        turtle_blue.forward((posicao_esquina-b)*40)
                        turtle_blue.right(90)
                        turtle_blue.forward((andar+b-posicao_esquina)*40)
                        

                    else:
                        
                        #turtle_azul.onclick(posicao2)
                        
                        posicao_esquina=lista_esquina.index("E",b+1,andar+b+1)
                        turtle_blue.forward((posicao_esquina-b)*40)
                        turtle_blue.left(90)
                        turtle_blue.forward((andar+b-posicao_esquina)*40)
                        
                    
    else:
            
        
        turtle_blue.forward(andar*40)
def posicao1(x,y):

    andar=1

    posicao_esquina=lista_esquina.index("E",y+1,y+andar+1)
    turtle_yellow.forward((posicao_esquina-y)*40)
    turtle_yellow.right(90)
    turtle_yellow.forward((andar+y-posicao_esquina)*40)

def posicao2(x,y):

    andar=1
    posicao_esquina=lista_esquina.index("E",b+1,andar+b+1)
    turtle_blue.forward((posicao_esquina-b)*40)
    turtle_blue.left(90)
    turtle_blue.forward((andar+b-posicao_esquina)*40)


def bonequinho_amarelo(y,andar):
    turtle_yellow.shape("turtle")
    turtle_yellow.speed(2)
    turtle_yellow.color("Black","Yellow")
    lista_auxiliar=[]
    for x in range(y+1,andar+y+1):
        lista_auxiliar.append(lista_esquina[x])
        
    if y==0:
        turtle_yellow.goto(-140,-300) #início yellow
        turtle_yellow.right(90)
        turtle_yellow.forward(andar*40)
        

    elif lista_auxiliar.count("E")!=0:
       
        if lista_auxiliar.count("E")==1:

            for x in range(y+1,y+andar+1):

                if lista_esquina[x]=="E":

                    if x==9 or x==23 or x==37 or x==51:
                    
                        posicao_esquina=lista_esquina.index("E",y+1,y+andar+1)
                        turtle_yellow.forward((posicao_esquina-y)*40)
                        turtle_yellow.right(90)
                        turtle_yellow.forward((andar+y-posicao_esquina)*40)
                        

                    else:
                            
                        posicao_esquina=lista_esquina.index("E",y+1,andar+y+1)
                        turtle_yellow.forward((posicao_esquina-y)*40)
                        turtle_yellow.left(90)
                        turtle_yellow.forward((andar+y-posicao_esquina)*40)
                        
                    
    else:
            
        
        turtle_yellow.forward(andar*40)
        


def bonequinho_verde(g,andar):
    turtle_green.speed(2)
    turtle_green.shape("turtle")
    turtle_green.color("Black","Green")
    lista_auxiliar=[]
    for x in range(g+1,andar+g+1):
        lista_auxiliar.append(lista_esquina[x])
        
    if g==0:
        turtle_green.goto(-340,60) #início green
        #turtle_green.right(90)
        turtle_green.forward(andar*40)
        

    elif lista_auxiliar.count("E")!=0:
       
        if lista_auxiliar.count("E")==1:

            for x in range(g+1,g+andar+1):

                if lista_esquina[x]=="E":

                    if x==9 or x==23 or x==37 or x==51:
                    
                        posicao_esquina=lista_esquina.index("E",g+1,g+andar+1)
                        turtle_green.forward((posicao_esquina-g)*40)
                        turtle_green.right(90)
                        turtle_green.forward((andar+g-posicao_esquina)*40)
                        

                    else:
                            
                        posicao_esquina=lista_esquina.index("E",g+1,andar+g+1)
                        turtle_green.forward((posicao_esquina-g)*40)
                        turtle_green.left(90)
                        turtle_green.forward((andar+g-posicao_esquina)*40)
                        
                    
    else:
            
        
        turtle_green.forward(andar*40)
        
def bonequinho_vermelho(r,andar):
    turtle_red.speed(2)
    turtle_red.shape("turtle")
    turtle_red.color("Black","Red")
    lista_auxiliar=[]
    for x in range(r+1,andar+r+1):
        lista_auxiliar.append(lista_esquina[x])
        
    if r==0:
        turtle_red.goto(20,260) #início green
        turtle_red.right(90)
        turtle_red.forward(andar*40)
        

    elif lista_auxiliar.count("E")!=0:
       
        if lista_auxiliar.count("E")==1:

            for x in range(r+1,r+andar+1):

                if lista_esquina[x]=="E":

                    if x==9 or x==23 or x==37 or x==51:
                    
                        posicao_esquina=lista_esquina.index("E",r+1,r+andar+1)
                        turtle_red.forward((posicao_esquina-r)*40)
                        turtle_red.right(90)
                        turtle_red.forward((andar+r-posicao_esquina)*40)
                        

                    else:
                            
                        posicao_esquina=lista_esquina.index("E",r+1,andar+r+1)
                        turtle_red.forward((posicao_esquina-r)*40)
                        turtle_red.left(90)
                        turtle_red.forward((andar+r-posicao_esquina)*40)
                        
                    
    else:
            
        
        turtle_red.forward(andar*40)
        #turtle_red.stamp()


nao_entrarB=0 #para que na primeira rodada os bonequinhos só comecem a avançar quando tirarem seis no dado
nao_entrarR=0 #precisa de um para cada cor 
nao_entrarG=0
nao_entrarY=0

b=0 #contador azul (primeiro bonequinho) caminhada
r=0 #contador vermelho (primeiro bonequinho) caminhada
g=0 #contador verde (primeiro bonequinho) caminhada
y=0 #contador amarelo (primeiro bonequinho) caminhada

#==============================================inicindo o jogo======================================================#

def apertou_azul():
    jogador="Blue"
    jogo(jogador)

def apertou_amarelo():
    jogador="Yellow"
    jogo(jogador)

def apertou_verde():
    jogador="Green"
    jogo(jogador)

def apertou_vermelho():
    jogador="Red"
    jogo(jogador)

        

#=================================================vamos à partida================================================#
def jogo(jogador):
    
    vez="Blue"
    nao_entrarB=0 #para que na primeira rodada os bonequinhos só comecem a avançar quando tirarem seis no dado
    nao_entrarR=0 #precisa de um para cada cor 
    nao_entrarG=0
    nao_entrarY=0

    b=0 #contador azul (primeiro bonequinho) caminhada
    r=0 #contador vermelho (primeiro bonequinho) caminhada
    g=0 #contador verde (primeiro bonequinho) caminhada
    y=0 #contador amarelo (primeiro bonequinho) caminhada
        
    
    while b<62 and y<62 and g<62 and r<62:


        if b<62 and y<62 and g<62 and r<62: #validar se o laço deve continuar ou parar

            #=============================bonequinho azul==========================#
            
            if vez=="Blue":
                
                    dado=randint(1,6)

                    dado_turtle(dado,vez)
                    
                    if dado==6 or nao_entrarB==1: #para que na primeira rodada os bonequinhos só comecem a avançar quando tirarem seis no dado

                        if (dado+b)<=62:
                            
                            while dado==6 and dado+b<=62: #quando dado igual a seis o jogador tem direito a uma nova rodada

                                if dado+b==62:

                                    turtle_blue.forward(40)
                                    turtle_blue.left(90)
                                    turtle_blue.forward(200)
                                    b+=dado
                           
                                
                                else:
                                
                                    contadorB=0
                                    while contadorB!=dado:
                                        andar=1

                                        bonequinho_azul(b,andar)
                                        
                                        contadorB+=1
                                        b+=1

                                    dado=randint(1,6)
                                    dado_turtle(dado,vez)

                            if dado+b<=62:

                                contadorB=0
                                
                                while contadorB!=dado:
                                    andar=1
                                    bonequinho_azul(b,andar)
                                    contadorB+=1
                                    b+=1
                        nao_entrarB=1
                            
                    vez="Yellow"
                        
        #====================================bonequiho amarelo=======================#
                
        if b<62 and y<62 and g<62 and r<62:

            if vez=="Yellow":

                dado=randint(1,6)

                dado_turtle(dado,vez)
                
                
                if dado==6 or nao_entrarY==1:

                    while dado==6 and dado+y<=62:

                        if dado+y==62:

                            turtle_yellow.forward(40)
                            turtle_yellow.left(90)
                            turtle_yellow.forward(200)
                            y+=dado
                         

                        else:
                            contadorY=0
                            while contadorY!=dado:
                                andar=1
                                bonequinho_amarelo(y,andar)
                                contadorY+=1
                                y+=1
     
                            dado=randint(1,6)
                            dado_turtle(dado,vez)

                    if dado+y<=62:

                        contadorY=0
                        while contadorY!=dado:
                            andar=1
                            bonequinho_amarelo(y,andar)
                            contadorY+=1
                            y+=1

                    nao_entrarY=1
                vez="Green"
                
        #======================================bonequinho verde==========================#
                
        if b<62 and y<62 and g<62 and r<62:
            
            if vez=="Green":

                dado=randint(1,6)
                print(vez)
                print(dado)
                dado_turtle(dado,vez)
                

                
                if dado==6 or nao_entrarG==1:

                    while dado==6 and dado+g<=62:

                        if dado+g==62:

                            turtle_green.forward(40)
                            turtle_green.left(90)
                            turtle_green.forward(200)
                            g+=dado
                          
                        else:
                            contadorG=0
                            while contadorG!=dado:
                                andar=1
                                bonequinho_verde(g,andar)
                                contadorG+=1
                                g+=1
  
                            dado=randint(1,6)
                            print(dado)
                            dado_turtle(dado,vez)
                    if dado+g<=62:
                    
                        contadorG=0
                        while contadorG!=dado:
                            andar=1
                            bonequinho_verde(g,andar)
                            contadorG+=1
                            g+=1
                    nao_entrarG=1
                vez="Red"
                

        #========================bonequinho vermelho=====================================#
                
        if b<62 and y<62 and g<62 and r<62:

            if vez=="Red":

                dado=randint(1,6)
                print(vez)
                print(dado)
                dado_turtle(dado,vez)
                
                
                if dado==6 or nao_entrarR==1:

                    while dado==6 and dado+r<=62:
                        if dado+r==62:

                            turtle_red.forward(40)
                            turtle_red.left(90)
                            turtle_red.forward(200)
                            r+=dado
                           
                        
                        else:
                            
                            contadorR=0
                            while contadorR!=dado:
                                andar=1
                                bonequinho_vermelho(r,andar)
                                contadorR+=1
                                r+=1

                            dado=randint(1,6) 
                            dado_turtle(dado,vez)
                    if dado+r<=62:
                        
                        contadorR=0
                        while contadorR!=dado:
                            andar=1
                            bonequinho_vermelho(r,andar)
                            contadorR+=1
                            r+=1
                    nao_entrarR=1
                vez="Blue"
       
#================================================identificar o vencedor===========================================#                

    if vez=="Yellow":
        vencedor=Tk()
        vencedor_texto=Label(vencedor,text="AZUL VENCEU!!!",fg="blue")
        vencedor_texto.place(x=70,y=65)
        if jogador=="Blue":
            vencedor_texto2=Label(vencedor,text="PARABÉNS! VOCÊ VENCEU!")
            vencedor_texto2.place(x=30,y=100)
        else:
            vencedor_texto2=Label(vencedor,text="SINTO MUITO! VOCÊ PERDEU!")
            vencedor_texto2.place(x=50,y=100)



    elif vez=="Blue":
        vencedor=Tk()
        vencedor_texto=Label(vencedor,text="RED VENCEU!!!",fg="red")
        vencedor_texto.place(x=85,y=65)
        if jogador=="Red":
             vencedor_texto2=Label(vencedor,text="PARABÉNS! VOCÊ VENCEU!")
             vencedor_texto2.place(x=50,y=100)
        else:
            vencedor_texto2=Label(vencedor,text="SINTO MUITO! VOCÊ PERDEU!")
            vencedor_texto2.place(x=50,y=100)

        

    elif vez=="Green":
        vencedor=Tk()
        vencedor_texto=Label(vencedor,text="AMARELO VENCEU!!!",fg="yellow")
        vencedor_texto.place(x=70,y=65)

        if jogador=="Yellow":
             vencedor_texto2=Label(vencedor,text="PARABÉNS! VOCÊ VENCEU!")
             vencedor_texto2.place(x=50,y=100)
        else:
            vencedor_texto2=Label(vencedor,text="SINTO MUITO! VOCÊ PERDEU!")
            vencedor_texto2.place(x=50,y=100)


        
        
    elif vez=="Red":
        vencedor=Tk()
        vencedor_texto=Label(vencedor,text="VERDE VENCEU!!!",fg="green")
        vencedor_texto.place(x=70,y=65)
        if jogador=="Green":
             vencedor_texto2=Label(vencedor,text="PARABÉNS! VOCÊ VENCEU!")
             vencedor_texto2.place(x=50,y=100)
        else:
            vencedor_texto2=Label(vencedor,text="SINTO MUITO! VOCÊ PERDEU!")
            vencedor_texto2.place(x=50,y=100)


        

    vencedor.geometry("300x300+200+200")

    vencedor.mainloop()
            



from tkinter import * #importando o módulo de interfaces

def comecar_jogo():

    teste=Tk()

    botao_azul=Button(teste,width=20,text="AZUL",fg="blue",command=apertou_azul)
    botao_azul.place(x=60,y=100)

    botao_amarelo=Button(teste,width=20,text="AMARELO",fg="yellow",command=apertou_amarelo)
    botao_amarelo.place(x=60,y=150)

    botao_verde=Button(teste,width=20,text="VERDE",fg="green",command=apertou_verde)
    botao_verde.place(x=60,y=200)

    botao_vermelho=Button(teste,width=20,text="VERMELHO",fg="red",command=apertou_vermelho)
    botao_vermelho.place(x=60,y=250)

    texto1=Label(teste, text="Bem-Vindo, ao LUDO PYTHON!!!")
    texto1.place(x=50,y=10)

    texto2=Label(teste,text="Para iniciar a diversão, escolha seu jogador:")
    texto2.place(x=20,y=40)
                
    teste.geometry("300x300+200+200")
    teste.mainloop()



comecar_jogo() #chamando a função para iniciar o jogo





        



