from turtle import *
from math import sqrt
import random
import winsound
import os
from tkinter import *


#Organiza a tela
tela = Screen()
tela.bgcolor("black")
tela.title("Space Invaders")
tela.setworldcoordinates(-400, -400, 400, 400) #resolução tela
tela.bgpic("space_invaders_background.gif")
#Registra os formatos da nave e dos invaders.
register_shape("invader.gif")
register_shape("player.gif")
register_shape("laser.gif")

#Borda
borda = Turtle()
borda.speed(0)
borda.color("white")
borda.penup()
borda.setpos(-300,-300)
borda.pendown()
borda.pensize(3)
borda.hideturtle()  #esconde a caneta
for side in range(4):  #Desenha a borda
    borda.fd(600)
    borda.lt(90)
#Score
score = 0
#Desenha o score
score_pen = Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 10, "normal"))
score_pen.hideturtle()

#Desenhando a nave
nave = Turtle()
nave.hideturtle()
nave.shape("player.gif")
nave.color("green")
nave.penup() #Esconde o rastro da caneta.
nave.seth(90)
nave.speed(0)
nave.setposition(0, -280) #Posição inicial da nave
nave.showturtle()
mov_nave = 15  #Velocidade da nave

#Numero de inimigos
n_inimigos = 5
#Lista de inimigos
inimigos = []
#Adiciona os inimigos na lista.
for i in range(n_inimigos):
    #Acrescenta turtles dentro da lista
    inimigos.append(Turtle())


# Inimigo
for inimigo in inimigos:

    inimigo.shape("invader.gif")
    inimigo.color("red")
    inimigo.speed(0)
    inimigo.penup()
    x = random.randint(-200, 200) #Posição aleatoria do inimigo
    y = random.randint(100, 250)  #Posição aleatoria do inimigo
    inimigo.setpos(x, y)


mov_inimigo = 2  # Velocidade do inimigo

#Laser da nave
laser = Turtle()
laser.hideturtle()
laser.shape("laser.gif")
laser.color("yellow")
laser.penup()
laser.seth(90)
laser.speed(0)
laser.shapesize(0.5, 0.5)
mov_laser = 20 #velocidade do laser
 #Estados do laser.
#ready - Preparado para atirar o laser.
#fire - Enquanto o laser é atirado.
est_laser = "ready"

#Movimento da nave - direita, esquerda:
def esquerda():
    x = nave.xcor() #Retorna posição x da nave.
    x -= mov_nave
    if x < -280:  #Limita o movimento para a borda
        x = - 280
    nave.setx(x) #A nave fica na posição x.
def direita():
    x = nave.xcor()
    x += mov_nave
    if x > 280:   #Limita o movimento para a borda
        x = 280
    nave.setx(x)
def solta_laser():
    global est_laser #Define como uma variavel global, caso precise de mudança.
    if est_laser == "ready":
        winsound.PlaySound("laser", winsound.SND_ASYNC)
        est_laser = "fire"
    #Posição do laser em relação a nave:
        x = nave.xcor()
        y = nave.ycor()
        laser.setpos(x, y + 10)
        laser.showturtle()
def eColisao(t1, t2):
    """
    Calcula a distância entre o laser e o inimigo e determina se houve colisão.
    """
    distancia = sqrt(pow(t1.xcor()-t2.xcor(), 2) + pow(t1.ycor()-t2.ycor(), 2))
    if distancia < 15:
        return True
    else:
        return False

listen() #Espera comando do teclado.
onkey(esquerda, "Left") #Movimenta para a esquerda.
onkey(direita, "Right") #Movimenta para a direita.
onkey(solta_laser, "space") #Solta o laser.

#Parte principal do jogo:
while True:
    for inimigo in inimigos:
        #Movimenta o inimigo.
        x = inimigo.xcor()
        x += mov_inimigo
        inimigo.setx(x) #muda para a nova posição
        # Quando atinge a borda desce/sobe e muda o sentido do movimento .
        if inimigo.xcor() > 280:
            #Movimenta todos os inimigos para baixo
            for e in inimigos:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Muda direção
            mov_inimigo *= -1
        if inimigo.xcor() < -280:
            # Movimenta todos os inimigos para baixo
            for e in inimigos:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Muda direção
            mov_inimigo *= -1
        #Verifica a colisão do laser com o inimigo.
        if eColisao(laser, inimigo):
            winsound.PlaySound("explosion", winsound.SND_ASYNC)
            #reseta o laser após a colisão com o alvo
            laser.hideturtle()
            est_laser = "ready" #permite o laser ser atirado novamente após a colisão com o alvo
            laser.setposition(0, -400)
            #reseta o inimigo
            x = random.randint(-200, 200)  # Posição aleatoria do inimigo
            y = random.randint(100, 250)  # Posição aleatoria do inimigo
            inimigo.setpos(x, y)
            #Atualiza o score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()   #Limpa o score
            score_pen.write(scorestring, False, align="left", font=("Arial", 10, "normal"))

        #Colisão entre a nave e o inimigo
        if eColisao(nave, inimigo):
            nave.hideturtle()
            inimigo.hideturtle()
            print("Game Over")
            break

    #Movimento do laser:
    if est_laser == "fire":
        y = laser.ycor()
        y += mov_laser
        laser.sety(y)
    #Verifica se o laser atingiu a borda:
    if laser.ycor() > 275:
        laser.hideturtle()
        est_laser = "ready"






done()