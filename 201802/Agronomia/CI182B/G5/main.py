import pygame, random
# bibliotecas pygame e random importadas para o jogo.
from pygame.locals import *
#todas as funções "locals" importadas, tirando a necessidade de serem chamadas no corpo do programa.

def aleatorio(): # função para criar um ponto aleatório
    x = random.randint(10, 580) # número aleatório da coordenada em X com espaço próximo das bordas
    y = random.randint(10, 580) # número aleatório da coordenada em Y com espaço próximo das bordas
    return (x//10 * 10, y//10 * 10)
# número aleatório com divisão inteira por 10, e depois multiplicado por 10, para não gerar uma coordenada "quebrada"


def colisao(c1, c2): # função para registrar duas posições
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
# comando para indicar que duas informações estão no mesmo espaço, e que irá sinalizar um encontro

pygame.init() # inicia o jogo/funções da biblioteca
tela = pygame.display.set_mode((600, 600)) # gera uma matriz com 600x600 pixels
pygame.display.set_caption('Snake') # nomeia o programa no cabeçalho da janela


cobrinha = [(200, 200), (210, 200), (220, 200)] # posição inicial da cobra
cobrinha_cor = pygame.Surface((10, 10)) # bitola em pixel da cobra
cobrinha_cor.fill((255, 255, 255)) # cor da cobra em RGB

maca_pos = aleatorio() # posição que a maçã ira ser gerada
maca = pygame.Surface((10, 10)) # tamanho em pixel da maçã
maca.fill((255, 0, 0)) # cor da maçã em RGB

fps = pygame.time.Clock() # chama uma função de contagem de frames


UP = 0 # ordenação interna dos sentidos
RIGHT = 1
DOWN = 2
LEFT = 3


meu_sentido = LEFT # sentido inicial que a cobra segue


while True: # repetição intermitente dos comandos do jogo
    fps.tick(10) # frequência que o jogo roda
    for event in pygame.event.get(): # captura os comandos inseridos no jogo
        if event.type == QUIT: # comando para fechar o programa
            pygame.quit()

        if event.type == KEYDOWN: # captura o pressionar das teclas
            if event.key == K_UP: # se pressionar a telha para cima
                meu_sentido = UP # o sentido da cobra no jogo é para cima
            if event.key == K_DOWN:
                meu_sentido = DOWN
            if event.key == K_LEFT:
                meu_sentido = LEFT
            if event.key == K_RIGHT:# se pressionar a telha para direita
                meu_sentido = RIGHT # o sentido da cobra no jogo é para direita

    if colisao(cobrinha[0], maca_pos): # se a cobra ocupar a mesma posição que a maçã
        maca_pos = aleatorio() # troca a posição da maçã, usando a função que gera uma posição aleatória
        cobrinha.append((0, 0)) # adiciona um novo pixel na última posisão da cobra

    for i in range(len(cobrinha) - 1, 0, -1): # tamanho da cobra menos uma posição, para receber as novas posições
        cobrinha[i] = (cobrinha[i-1][0], cobrinha[i-1][1]) # cada posição da cobra troca de lugar com a anterior

    if meu_sentido == UP: # se o comando de andar para cima é dado, a cobra se dirige para cima
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10) # se a cobra está se dirigindo para cima, o eixo Y diminui
    if meu_sentido == DOWN:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if meu_sentido == RIGHT: # se o comando de andar para a direita é dado, a cobra se dirige para direita
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1]) # se a cobra está se dirigindo para direita, o eixo X aumenta
    if meu_sentido == LEFT:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    tela.fill((0, 0, 0)) # gera uma tela limpa
    tela.blit(maca, maca_pos) # insere a maçã na tela
    for pos in cobrinha:
        tela.blit(cobrinha_cor, pos) # insere a cobra na tela

    if colisao(cobrinha[0], pos): # cria um encontro da cobra com ela mesma
        break # caso a cobra "bata" nela mesma, a repetição para


    pygame.display.update() # atualiza a tela com as novas informações