import pygame
from random import randrange

pygame.mixer.init()  # inicia a música
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

rosa = (255, 62, 150)  # encontra as cores no site http://cloford.com/
azul = (151, 255, 255)
vermelho = (255, 48, 48)
verde = (24,252,0)
amarelo = (255,215,0)
preto = (41,36,33)

try:
    pygame.init()  # inicia o jogo no pygame
except:
    print("O jogo Evil Cobrinha não pode ser inicializado!")

largura = 600  # define a variavel largura da tela em pixels
altura = 500  # define a variavel altura da tela em pixels
tamanho = 10  # define a variavel tamanho da cobrinha em pixels
placar = 60

relogio = pygame.time.Clock()  # define a velocidade em que ocorrerá o update de tela
fundo = pygame.display.set_mode((largura, altura))  # tamanho da tela, 600 x 600 pixels
pygame.display.set_caption('Evil Cobrinha')  # nome que aparece na aba


def texto(msg, cor, size, x, y):
    font = pygame.font.SysFont(None, size)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])  # insere o texto e define a posição em que se encontra o texto (centro da tela)


def cobrinha(CobraXY):
    for XY in CobraXY:  # cria uma lista CobraXY
        pygame.draw.rect(fundo, rosa, [XY[0], XY[1], tamanho, tamanho])  # define o fundo, a cor e as dimensões da cobrinha


def ringo(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])  # define o fundo, a cor e as dimensões da maçã


def evil_cobrinha():  # função do jogo
    sair = True
    fimdejogo = False
    pos_x = randrange(0, largura - tamanho, 10)  # faz com que a posição inicial x da cobrinha seja aleatória e múltipla de 10
    pos_y = randrange(0, altura - tamanho-placar, 10)  # faz com que a posição inicial y da cobrinha seja aleatória e múltipla de 10
    ringo_x = randrange(0, largura - tamanho, 10)  # faz com que a posição inicial x da maçã seja aleatória e múltipla de 10
    ringo_y = randrange(0, altura - tamanho-placar, 10)  # faz com que a posição inicial y da maçã seja aleatória e múltipla de 10
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []  # Cria uma lista da cobra XY
    CobraComp = 1  # Indica o comprimento inicial da cobra
    pontos = 0

    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho, 10)  # faz com que a posição inicial x da cobrinha seja aleatória e múltipla de 10
                        pos_y = randrange(0, altura - tamanho-placar, 10)  # faz com que a posição inicial y da cobrinha seja aleatória e múltipla de 10
                        ringo_x = randrange(0, largura - tamanho, 10)  # faz com que a posição inicial x da maçã seja aleatória e múltipla de 10
                        ringo_y = randrange(0, altura - tamanho-placar, 10)  # faz com que a posição inicial y da maçã seja aleatória e múltipla de 10
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []  # Cria uma lista da cobra XY
                        CobraComp = 1  # Indica o comprimento inicial da cobra
                        pontos = 0
                    elif event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                fundo.fill(vermelho)
                texto('Oh, Jeez, Rick - Game Over!', azul, 50, 65, 30)
                texto('Sua pontuação: '+str(pontos), preto, 40, 70, 80)
                pygame.draw.rect(fundo, preto, [45, 120, 210, 50])
                texto('Continuar(C)', amarelo, 35, 50, 125)
                pygame.draw.rect(fundo, preto, [300, 120, 150, 50])
                texto('Sair(S)', amarelo, 35, 310, 125)
                pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho: #não é possível se mover na diração oposta logo em seguida
                    velocidade_y = 0
                    velocidade_x = -tamanho
                elif event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                elif event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                elif event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

        fundo.fill(azul)
        pos_x += velocidade_x
        pos_y += velocidade_y

        CobraInicio = [pos_x, pos_y]  # Cria uma outra lista da cabeça da cobra
        CobraXY.append(CobraInicio)  # adiciona a lista CobraInicio à lista CobraXY

        if len(CobraXY) > CobraComp:
            del CobraXY[0]  # deleta o primeiro elemento da lista, que é o rabo da cobra, o novo elemento da lista

        pygame.draw.rect(fundo, verde, [0, altura-placar, largura, placar])
        texto('Pontuação: ' +str(pontos), preto, 25, 10, altura-50)
        cobrinha(CobraXY)  # envia os valores de pos_x e pos_y em forma de lista

        if pos_x == ringo_x and pos_y == ringo_y:  # se a houver a colisão da cobrinha com a maçã
            ringo_x = randrange(0, largura - tamanho, 10)  # faz com que a nova posição x da maçã seja aleatória e múltipla de 10
            ringo_y = randrange(0, altura - tamanho - placar, 10)  # faz com que a nova posição y da maçã seja aleatória e múltipla de 10
            CobraComp += 1  # faz com que o comprimento da cobra sempre cresça em 1 unidade
            pontos += 1

        ringo(ringo_x, ringo_y)
        pygame.display.update()
        relogio.tick(15)
        if pos_x > largura:
            fimdejogo = True
        if pos_x < 0:
            fimdejogo = True
        if pos_y > altura-placar:
            fimdejogo = True
        if pos_y < 0:
            fimdejogo = True


evil_cobrinha()
pygame.quit()
