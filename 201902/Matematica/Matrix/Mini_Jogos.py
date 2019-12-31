import pygame
from random import randrange, randint, sample, shuffle

try:                                                # Verifica se o pygame foi iniciado corretamente
    pygame.init()
except:
    print("Pygame nao foi inicializado corretamente")

branco = (255,255,255)                              # Atribui valores rgb para as variáveis das cores a serem usadas 
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
amarelo = (250,250,0)
preto = (0,0,0)
salmao = (250,128,114)     # cor utilizada para o retângulo de perguntas
agua = (127,255,212)       # cor utilizada para os retângulos de alternativas
tomate = (255,99,71)       # cor utilizada para o fundo da tela de Game Over
verde = (50,205,50)        # cor utilizada para o fundo da tela de Vitória
amareloescuro = (100,100,0)
vermelhoescuro = (100,0,0)
verdeescuro = (0,50,0)
azulescuro = (0,0,100)

relogio = pygame.time.Clock()

largura = 1000                                      #define o tamanho da tela do jogo e do placar
altura = 600
tamanho = 50                                        #define tamanho das macas e dos blocos da cobra

fundo = pygame.display.set_mode((largura,altura))   #gera uma tela de largura x altura
pygame.display.set_caption("MINI JOGOS")            #da nome a tela

# De Q1 até Q34 temos as perguntas do QUIZ, assim como de R1 até R34 temos as alternativas de cada pergunta.
# Da prar usar uma matriz pras perguntas e pras respostas

Q1 = "Em “O Senhor dos Anéis”, o mago Gandalf, o Cinzento, enfrenta Balrog e"
Q1_1 = "acaba morrendo. Nessa passagem memorável do livro, Gandalf diz uma frase"
Q1_2 = "que tornou-se famosa. Qual é essa frase?"
R1 = ["a) Fico e defendo meus amigos!", "b) Você não pode passar!", "c) Coragem é a melhor defesa que vocês têm agora!", "d) Não vou pedir que não chorem, pois nem todas as lágrimas são um mal.", "e) Morra, chama de Udûn!"]

Q2 = "A ilustre obra de Miguel de Cervantes, “Dom Quixote”, trata de um homem"
Q2_1 = "apaixonado por livros de cavalaria e que passa a acreditar que faz parte de"
Q2_2 = "um destes. Durante a narrativa, o autointitulado Dom Quixote de La Mancha"
Q2_3 = "fala várias vezes acerca de uma donzela. Qual é o nome desta mulher?"
R2 = ["a) Dorotéia", "b) Drica", "c) Arabella", "d) Beatriz", "e) Dulcinéia"]

Q3 = "Na série britânica Doctor Who o personagem principal possui uma nave espacial"
Q3_1 = "que permite sua viagem no tempo. Há muitos anos, seu sistema de camuflagem"
Q3_2 = "estragou, e sua forma permaneceu como:"
R3 = ["a) Uma cabine telefônica azul", "b) Uma cabine telefônica vermelha", "c) Um orelhão", "d) Uma cabine de polícia azul", "e) Uma cabine de polícia vermelha"]

Q4 = "Um filme ou série de filmes que um dos atores principais mais odiou fazer, mas"
Q4_1 = "que alavancou a sua carreira:"
R4 = ["a) O bebê de Rosemary", "b) Razão e Sensibilidade", "c) Saga Crepúsculo", "d) Jogos Vorazes", "e) Harry Potter"]

Q5 = "Série de comédia cujo enredo apresenta o que acontece na “vida após a morte” de"
Q5_1 = "maneira divertida. Em seu elenco há Kristen Bell, a Anna de Frozen."
R5 = ["a) Friends", "b) Brooklyn 99", "c) The Good Place", "d) The OA", "e) Lucífer"]

Q6 = "Quais são os nomes dos Lobos Gigantes adotados pelos filhos de Ned Stark"
Q6_1 = "em Game of Thrones?"
R6 = ["a) Cão Felpudo, Verão, Nymeria, Lobo Cinzento, Fantasma e Lady", "b) Inverno, Verão, Arya, Lobo Cinzento, Fantasma e Lady", "c) Cão Felpudo, Gladiador, Nymeria, Lobo Branco, Fantasma e Sansa", "d) Gladiador, Inverno, Arya, Lobo Cinzento, Gorila e Sansa", "e) Cão Felpudo, Verão, Nymeria, Lobo Branco, Sombra e Lady"]

Q7 = "No livro Harry Potter e o Cálice de Fogo qual o dragão que Fleur Delacour"
Q7_1 = "enfrenta no torneio Tri Bruxo?"
R7 = ["a) Vermelho Grifo", "b) Verde Gales", "c) Roxo Sangue", "d) Branco Unicórnio", "e) Azul Geleia"]

Q8 = "Qual o nome das criaturas que habitam o Labirinto em Maze Runner?"
R8 = ["a) Grifos", "b) Orcs", "c) Verdugos", "d) Arroxeados", "e) Vermes voadores"]

Q9 = "Qual a cor do sabre de luz de Mace Windu, personagem de Samuel L Jackson na"
Q9_1 = "franquia Star Wars?"
R9 = ["a) Azul", "b) Verde", "c) Rosa", "d) Roxo", "e) Amarelo"]

Q10 = "Na saga Harry Potter, a escola de Magia e Bruxaria de Hogwarts foi fundada por 4"
Q10_1 = "grandes bruxos, quais eram os nomes deles?"
R10 = ["a) Godric Grifinória, Helga Lufa-Lufa, Rowena Corvinal e Salazar Sonserina", "b) Gregório Grifinória, Helga Lufa-Lufa, Ravena Corvinal e Salazar Sonserina", "c) Gregório Grifinória, Helena Lufa-Lufa, Rowena Corvinal e Salazar Sonserina", "d) Godric Grifinória, Helena Lufa-Lufa, Ravena Corvinal e Sandro Sonserina", "e) Godric Grifinória, Helena Lufa-Lufa, Rowena Corvinal e Salazar Sonserina"]

Q11 = "Em Harry Potter, Voldemort mudou de nome para não manter o de seu pai “trouxa”,"
Q11_1 = "do qual tinha vergonha e nojo. Qual era esse nome?"
R11 = ["a) Tom Muriel Riddle", "b) Tom Marvolo Riddle", "c) Thomas Muriel Riddleston", "d) Thomas Marvel Riddle", "e) Tom Marvolo Riddleston"]

Q12 = "Em Percy Jackson, Percy é presenteado com uma caneta que vira espada,"
Q12_1 = "originalmente um presente de Zoe a Hércules. Seu nome, Contra-Corrente, era"
Q12_2 = "a tradução para...?"
R12 = ["a) Lineaklus", "b) Ranelus", "c) Darkless", "d) Anaklusmos", "e) Otaklusmos"]

Q13 = "No desenho Steven Universo existem quatro diamantes, que fazem parte da Grande"
Q13_1 = "Autoridade Diamante. Quais são elas?"
R13 = ["a) Preto, Azul, Verde e Rosa", "b) Branco, Amarelo, Preto e Roxo", "c) Verde, Amarelo, Rosa e Azul", "d) Branco, Amarelo, Rosa e Azul", "e) Roxo, Verde, Amarelo e Branco"]

Q14 = "Quantos livros e filmes fazem parte da franquia Harry Potter?"
R14 = ["a) 8 livros e 7 filmes", "b) 7 livros e 8 filmes", "c) 5 livros e 5 filmes", "d) 7 livros e 7 filmes", "e) 6 livros e 7 filmes"]

Q15 = "Na série The Umbrella Academy, o Sr. Hargreeves tenta adotar o máximo de crianças"
Q15_1 = "nascidas depois de um fenômeno. Quantas ele consegue adotar?"
R15 = ["a) 8 crianças", "b) 5 crianças", "c) 2 crianças", "d) 9 crianças", "e) 7 crianças"]

Q16 = "Um jogo que se passa após o fim da Primeira Guerra Mundial e que se baseia no dilema"
Q16_1 = "“ser o médico ou o monstro”."
R16 = ["a) Vampyr", "b) Vampire: The Masquerade – Bloodlines", "c) Until Dawn", "d) Cyberpunk 2077", "e) Soma"]

Q17 = "Qual o nome do mapa principal do MOBA League of Legends?"
R17 = ["a) Moonhunter", "b) Summoner's Rift", "c) The Dark Place", "d) Green Night", "e) Palace of Darkness"]

Q18 = "Detroit Become Human é um jogo de sucesso da empresa Quantic Dream, qual os nomes dos"
Q18_1 = "3 principais personagens jogáveis?"
R18 = ["a) Connor, Kara e Marcus", "b) Connor, Klara e Marcus", "c) Conner, Kara e Marcus", "d) Conner, Klara e Marcus", "e) Connor, Kara e Marvin"]

Q19 = "Considerada a “cidade do romance”, onde há a Torre Eiffel."
R19 = ["a) Paris", "b) Veneza", "c) Roma", "d) Rio de Janeiro", "e) Londres"] 

Q20 = "Chamada de “cidade maravilhosa”, é a cidade a que as pessoas de fora associam o Brasil."
R20 = ["a) Curitiba", "b) Recife", "c) Salvador", "d) São Paulo", "e) Rio de Janeiro"]

Q21 = "Grande parque localizado em Santa Catarina, internacionalmente conhecido, cujo nome"
Q21_1 = "remete ao de uma pessoa já falecida."
R21 = ["a) Walt Disney", "b) Beto Carreiro World", "c) Parque do Golinha", "d) Jardins de Tivoli", "e) Mirabilândia"]

Q22 = "É considerada uma época de transição entre o período de guerras da primeira metade do"
Q22_1 = "século XX e o período das revoluções comportamentais e tecnológicas da segunda metade."
Q22_2 = "Essa época também foi considerada a “idade de ouro” do cinema."
R22 = ["a) Década de 1940", "b)  Década de 1920", "c) Década de 1950", "d) Década de 1930", "e) Década de 1960"]

Q23 = "Período de surgimento de movimentos artísticos como o dadaísmo e o surrealismo, das"
Q23_1 = "comédias de Chaplin e do primeiro personagem de desenho animado: o Gato Félix. A"
Q23_2 = "muitas vezes chamada “Era do Jazz”, é a época na qual se passa o livro “O Grande"
Q23_3 = "Gatsby” de F. Scott Fitzgerald."
R23 = ["a) Década de 1920", "b) Década de 1950", "c) Década de 1910", "d) Década de 1970", "e) Década de 1930"]

Q24 = "Foi um(a) dos(as) protagonistas da série “Friends”, além de ter feito vários filmes de"
Q24_1 = "comédia romântica, como por exemplo, “Esposa de Mentirinha”."
R24 = ["a) Winona Ryder", "b) Adam Sandler", "c) Jennifer Aniston", "d) Courteney Cox", "e) Brad Pitt"]

Q25 = "Vocalista da banda Panic! At The Disco; intérprete da versão dos créditos de"
Q25_1 = "“Into the Unknown” de Frozen 2."
R25 = ["a) Patrick Stump", "b) Brendon Urie", "c) Billie Joe", "d) Ryan Ross", "e) Pete Wentz"]

Q26 = "Criador da história em quadrinhos “The Umbrella Academy” e vocalista da banda emo"
Q26_1 = "“My Chemical Romance”."
R26 = ["a) Gerard Way", "b) Brendon Urie", "c) Matt Le Branc", "d) Pete Wentz", "e) Ed Sheeran"]

Q27 = "Década do “milagre econômico” brasileiro, o auge da ditadura militar no Brasil."
Q27_1 = "Época de Guerra Fria, com a Alemanha dividida entre Ocidental (capitalista) e"
Q27_2 = "Oriental (socialista). Além disso, esse é o período da crise do petróleo."
R27 = ["a) Década de 1920", "b) Década de 1950", "c) Década de 1960", "d) Década de 1970", "e) Década de 1980"]

Q28 = "São deste momento da história: Charles Darwin, Karl Marx e Sigmund Freud. Foi"
Q28_1 = "um longo período de paz e prosperidade para o povo britânico, conhecido como"
Q28_2 = "Pax Britannica."
R28 = ["a) Belle Époque", "b) Era Vitoriana", "c) Idade Média", "d) Período Elisabetano", "e) Revolução Industrial"]

Q29 = "Período no qual ocorreram as Cruzadas, marcado por grande influência religiosa."
Q29_1 = "Desta época, temos obras de Santo Agostinho e São Tomás de Aquino."
R29 = ["a) Revolução Francesa", "b) Idade Média", "c) Segunda Guerra Mundial", "d) Guerra do Vietnã", "e) Império Romano"]

Q30 = "É um mamífero carnívoro da família dos felídeos, muito popular como animal de estimação."
Q30_1 = "Ocupando o topo da cadeia alimentar, é predador natural de diversos animais, como"
Q30_2 = "roedores, pássaros, lagartixas e alguns insetos."
R30 = ["a) Leão", "b) Cachorro", "c) Gato", "d) Lobo", "e) Coelho"]

Q31 = "É um mamífero mustelídeo característico do Pantanal e da bacia do Rio Amazonas. Este"
Q31_1 = "animal detém uma cauda comprida e achatada, olhos consideravelmente grandes e patas"
Q31_2 = "curtas e espessas. Alimenta-se de peixes."
R31 = ["a) Leão Marinho", "b) Ariranha", "c) Piranha", "d) Capivara", "e) Baleia"]

Q32 = "É um réptil pecilotérmico, sem patas, que rasteja. Pode ser peçonhento ou não."
R32 = ["a) Serpente", "b) Tartaruga", "c) Lagarto", "d) Iguana", "e) Minhoca"]

Q33 = "No primeiro episódio de Pokémon, Ash ganha do Professor Carvalho um..."
R33 = ["a) Bulbasaur", "b) Squirtle", "c) Charmander", "d) Eeve", "e) Pikachu"]

Q34 = "Em Rick & Morty, o personagem Rick repete frequentemente a frase “wubba lubba Dub-Dub”."
Q34_1 = "Qual é o seu significado?"
R34 = ["a) “Me passe a cerveja, Morty”", "b) “Nada importa, na verdade”", "c) “Eu estou em um grande sofrimento, por favor me ajude”", "d) “Gatinhas manhosas robôs safadas”", "e) “Rick é o maioral”"]

correta = ['nada', 'b', 'e', 'd', 'c', 'c', 'a', 'b', 'c', 'd', 'a', 'b', 'd', 'd', 'b', 'e', 'a', 'b', 'a', 'a', 'e', 'b', 'c', 'a', 'c', 'b', 'a', 'd', 'b', 'b', 'c', 'b', 'a', 'e', 'c'] #respostas corretas de cada questão



def texto(mensag, cor, tamtexto, x, y):             #imprime um texto de cor e tamtexto apartir das coordenadas x,y
    font = pygame.font.SysFont(None, tamtexto)
    texto1 = font.render(mensag, True, cor)
    fundo.blit(texto1, [x,y])

    
def cobra(CobraXY):                                 #desenha os blocos da cobra verde em XY[0] x XY[1] de tamanho x tamanho no fundo 
    for XY in CobraXY:
        pygame.draw.rect(fundo, verde, [XY[0], XY[1],tamanho, tamanho])


def maca(macax, macay):                             #desenha as macas vermelhas em ... no fundo 
    pygame.draw.rect(fundo,vermelho, [macax, macay,tamanho, tamanho])

    
def jogo_cobra():     # Nil fazer funcao para zerar parametros
    sair = False
    gameover = False

    coordx = randrange(0, largura - tamanho, 50)    #gera valores numa grade altura x largura de blocos de 50 pixels
    coordy = randrange(0, altura - tamanho, 50)
    macax = randrange(0, largura - tamanho, 50)
    macay = randrange(0, altura - tamanho, 50)
    macaXY = [0,0]
    while (coordx == macax and coordy == macay):
        macax = randrange(0, largura - tamanho, 50)
        macay = randrange(0, altura - tamanho, 50)
    
    velocx = 0          #veloc ded deslocamento nos eixos
    velocy = 0
    CobraXY = []        #posicoes dos blocos da cobra
    CobraComp = 1       #comp inicial da cobra
    pontos = 0          #pontuacao inicial 

    while not(sair):
        relogio.tick(10)
        fundo.fill(preto)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:            #recebe a direcao q a cobra deve ir, sem poder inverter sua direcao
                if event.key == pygame.K_LEFT and velocx != tamanho and mexeu:
                    velocy = 0
                    velocx = -tamanho
                    mexeu = False
                elif event.key == pygame.K_RIGHT and velocx != -tamanho and mexeu:
                    velocy = 0
                    velocx = tamanho
                    mexeu = False
                elif event.key == pygame.K_UP and velocy != tamanho and mexeu:
                    velocy = -tamanho
                    velocx = 0
                    mexeu = False
                elif event.key == pygame.K_DOWN and velocy != -tamanho and mexeu:
                    velocy = tamanho
                    velocx = 0
                    mexeu = False

        coordx += velocx                            #define a posicao da cobra
        coordy += velocy

        if coordx > largura - 1:                    #tranposrta a cobra de um lado ao outro da tela quando aquela ultrapassa a borda desta
            coordx = 0
        if coordx < 0:
            coordx = largura - tamanho
        if coordy > altura  - 1:
            coordy = 0
        if coordy < 0:
            coordy = altura - tamanho 
            
        CobraCabeca = []
        CobraCabeca.append(coordx)
        CobraCabeca.append(coordy)
        CobraXY.append(CobraCabeca)
        
        if len(CobraXY) > CobraComp:
            del CobraXY[0]
            mexeu = True
        if any(CobraCorpo == CobraCabeca for CobraCorpo in CobraXY[:-1]):
                gameover = True

        cobra(CobraXY)

        maca(macax, macay)

        if (coordx == macax) and (coordy == macay):
            macax = randrange(0, largura - tamanho, 50)
            macay = randrange(0, altura - tamanho, 50)
            macaXY[0] = macax
            macaXY[1] = macay
            while any(CobraCorpo == macaXY for CobraCorpo in CobraXY[:-1]):
                macax = randrange(0, largura - tamanho, 50)
                macay = randrange(0, altura - tamanho, 50)
                macaXY[0] = macax
                macaXY[1] = macay
            CobraComp += 1
            pontos += 1

        while gameover:
            fundo.fill(tomate)
            texto("GAME OVER!", preto, 200, largura - 950, altura - 400)
            texto("Pontuação: " +str(pontos), preto, 80, 280, 350)
            pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
            pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
            texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
            texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
            pygame.display.update()
            clique = False
            while not(clique):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                            mousex = pygame.mouse.get_pos()[0]
                            mousey = pygame.mouse.get_pos()[1]
                            if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                clique = True
                                sair = False
                                gameover = False
                                coordx = randrange(0, largura - tamanho, 50)
                                coordy = randrange(0, altura - tamanho, 50)
                                macax = randrange(0, largura - tamanho, 50)
                                macay = randrange(0, altura - tamanho, 50)
                                velocx = 0
                                velocy = 0
                                CobraXY = []
                                CobraComp = 1
                                pontos = 0
                            if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                return 0
                    if event.type == pygame.QUIT:
                        clique = True
                        pygame.quit()
                        exit()
            


            pygame.display.update()

        pygame.display.update()
        















def tela_apagada():
    fundo.fill(preto)                    
    pygame.draw.rect(fundo, amareloescuro, [0, 0, largura/2 - 2, altura/2 - 2])
    pygame.draw.rect(fundo, vermelhoescuro, [largura/2 + 2, 0, largura/2 - 2, altura/2 - 2])
    pygame.draw.rect(fundo, verdeescuro, [0, altura/2 + 2 , largura/2 - 2, altura/2 - 2])
    pygame.draw.rect(fundo, azulescuro, [largura/2 + 2, altura/2 + 2, largura/2 - 2, altura/2 - 2])
    pygame.display.update()

    
                    
def jogo_genius():
    jogar = True
    while jogar:
        rodadas = 10
        sequencia = []
        for i in range(rodadas):
            cor = randint(1,4)
            sequencia.append(cor)

        rod = 1
        erro = 0
        sair = False
        up = False
        fim = False
        
        
        for i in range(1,rodadas+1):
            fundo.fill(agua)
            texto("RODADA " + str(i), preto, 100, largura/3, altura/3)
            pygame.display.update()
            pygame.time.delay(700)
            for j in range(i):
                
                for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       sair = True
                       j = i
                tela_apagada()
                pygame.time.delay(500)
                if sequencia[j] == 1:
                    pygame.draw.rect(fundo, amarelo, [0,0,largura/2 - 2,altura/2 - 2])
                elif sequencia[j] == 2:
                    pygame.draw.rect(fundo, vermelho, [largura/2 + 2,0,largura/2 - 2,altura/2 - 2])
                elif sequencia[j] == 3:
                    pygame.draw.rect(fundo, verde, [0,altura/2 + 2,largura/2 - 2,altura/2 - 2])
                elif sequencia[j] == 4:
                    pygame.draw.rect(fundo, azul, [largura/2 + 2,altura/2 + 2,largura/2 - 2,altura/2 - 2])
                pygame.display.update()
                pygame.time.delay(300)

            jogador = []
            certo = 0
            while not(certo):
                tela_apagada()
                clique = False
                while not(clique):
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and clique == False:
                            mousex = pygame.mouse.get_pos()[0]
                            mousey = pygame.mouse.get_pos()[1]
                            if mousex < (largura/2 - 2) and mousey < (altura/2 - 2):
                                jogador.append(1)
                                pygame.draw.rect(fundo, amarelo, [0,0,largura/2 - 2,altura/2 - 2])
                                pygame.display.update()
                                pygame.time.delay(200)
                                clique = True
                            elif mousex > (largura/2 + 2) and mousex < largura and mousey < (altura/2 - 2):
                                jogador.append(2)
                                pygame.draw.rect(fundo, vermelho, [largura/2 + 2,0,largura/2 - 2,altura/2 - 2])
                                pygame.display.update()
                                pygame.time.delay(200)
                                clique = True
                            elif mousex < (largura/2 - 2) and mousey > (altura/2 + 2) and  mousey < altura:
                                jogador.append(3)
                                pygame.draw.rect(fundo, verde, [0,altura/2 + 2,largura/2 - 2,altura/2 - 2])
                                pygame.display.update()
                                pygame.time.delay(200)
                                clique = True
                            elif mousex > (largura/2 + 2) and mousex < largura and mousey > (altura/2 + 2) and  mousey < altura:
                                jogador.append(4)
                                pygame.draw.rect(fundo, azul, [largura/2 + 2,altura/2 + 2,largura/2 - 2,altura/2 - 2])
                                pygame.display.update()
                                pygame.time.delay(200)
                                clique = True
                        if event.type == pygame.QUIT:
                            clique = True
                            pygame.quit()
                            exit()

                            
                if len(jogador) == len(sequencia[:j+1]):
                    if jogador == sequencia[:j+1]:
                        certo = 1
                    else:
                        fundo.fill(tomate)
                        texto("GAME OVER!", preto, 200, largura - 950, altura - 400)
                        pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
                        pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
                        texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
                        texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
                        pygame.display.update()
                        clique = False
                        while not(clique):
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                                        mousex = pygame.mouse.get_pos()[0]
                                        mousey = pygame.mouse.get_pos()[1]
                                        if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                            return 1
                                        if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                            return 0
                                if event.type == pygame.QUIT:
                                    clique = True
                                    pygame.quit()
                                    exit()
        if jogador == sequencia:
                fundo.fill(agua)
                texto("VITORIA   :)", salmao, 200, largura - 950, altura - 400)
                pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
                pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
                texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
                texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
                pygame.display.update()
                clique = False
                while not(clique):
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                                mousex = pygame.mouse.get_pos()[0]
                                mousey = pygame.mouse.get_pos()[1]
                                if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                    return 1
                                if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                    return 0 
                        if event.type == pygame.QUIT:
                            clique = True
                            pygame.quit()
                            exit()
















def gera_questao(questao_escolhida):                                 # gera a questão aleatoriamente               

##    for i in range(len(Q[questao_escolhida])):
##        texto(Q[questao_escolhida][i]
    

    if questao_escolhida == 1:
      texto(Q1, preto, 30, largura-950,altura-565)
      texto(Q1_1, preto, 30, largura-950,altura-535)
      texto(Q1_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R1[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 2:
      texto(Q2, preto, 30, largura-950,altura-565)
      texto(Q2_1, preto, 30, largura-950,altura-535)
      texto(Q2_2, preto, 30, largura-950,altura-505)
      texto(Q2_3, preto, 30, largura-950,altura-475)
      for i in range(5):
          texto(R2[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 3:
      texto(Q3, preto, 30, largura-950,altura-565)
      texto(Q3_1, preto, 30, largura-950,altura-535)
      texto(Q3_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R3[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 4:
      texto(Q4, preto, 30, largura-950,altura-565)
      texto(Q4_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R4[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 5:
      texto(Q5, preto, 30, largura-950,altura-565)
      texto(Q5_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R5[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 6:
      texto(Q6, preto, 30, largura-950,altura-565)
      texto(Q6_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R6[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 7:
      texto(Q7, preto, 30, largura-950,altura-565)
      texto(Q7_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R7[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão
          
    elif questao_escolhida == 8:
      texto(Q8, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R8[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão
          
    elif questao_escolhida == 9:
      texto(Q9, preto, 30, largura-950,altura-565)
      texto(Q9_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R9[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão
      
    elif questao_escolhida == 10:
      texto(Q10, preto, 30, largura-950,altura-565)
      texto(Q10_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R10[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 11:
      texto(Q11, preto, 30, largura-950,altura-565)
      texto(Q11_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R11[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 12:
      texto(Q12, preto, 30, largura-950,altura-565)
      texto(Q12_1, preto,30, largura-950,altura-535)
      texto(Q12_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R12[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 13:
      texto(Q13, preto, 30, largura-950,altura-565)
      texto(Q13_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R13[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 14:
      texto(Q14, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R14[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 15:
      texto(Q15, preto, 30, largura-950,altura-565)
      texto(Q15_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R15[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 16:
      texto(Q16, preto, 30, largura-950,altura-565)
      texto(Q16_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R16[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 17:
      texto(Q17, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R17[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 18:
      texto(Q18, preto, 30, largura-950,altura-565)
      texto(Q18_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R18[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 19:
      texto(Q19, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R19[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 20:
      texto(Q20, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R20[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 21:
      texto(Q21, preto, 30, largura-950,altura-565)
      texto(Q21_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R21[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 22:
      texto(Q22, preto, 30, largura-950,altura-565)
      texto(Q22_1, preto, 30, largura-950,altura-535)
      texto(Q22_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R22[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 23:
      texto(Q23, preto, 30, largura-950,altura-565)
      texto(Q23_1, preto, 30, largura-950,altura-535)
      texto(Q23_2, preto, 30, largura-950,altura-505)
      texto(Q23_3, preto, 30, largura-950,altura-475)
      for i in range(5):
          texto(R23[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 24:
      texto(Q24, preto, 30, largura-950,altura-565)
      texto(Q24_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R24[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 25:
      texto(Q25, preto, 30, largura-950,altura-565)
      texto(Q25_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R25[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão
      
    elif questao_escolhida == 26:
      texto(Q26, preto, 30, largura-950,altura-565)
      texto(Q26_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R26[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 27:
      texto(Q27, preto, 30, largura-950,altura-565)
      texto(Q27_1, preto, 30, largura-950,altura-535)
      texto(Q27_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R27[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 28:
      texto(Q28, preto, 30, largura-950,altura-565)
      texto(Q28_1, preto, 30, largura-950,altura-535)
      texto(Q28_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R28[i], preto, 30, largura-950, (altura-320)+70*(i-1))                    # mostra as alternativas da questão

    elif questao_escolhida == 29:
      texto(Q29, preto, 30, largura-950,altura-565)
      texto(Q29_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R29[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 30:
      texto(Q30, preto, 30, largura-950,altura-565)
      texto(Q30_1, preto, 30, largura-950,altura-535)
      texto(Q30_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R30[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 31:
      texto(Q31, preto, 30, largura-950,altura-565)
      texto(Q31_1, preto, 30, largura-950,altura-535)
      texto(Q31_2, preto, 30, largura-950,altura-505)
      for i in range(5):
          texto(R31[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 32:
      texto(Q32, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R32[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 33:
      texto(Q33, preto, 30, largura-950,altura-565)
      for i in range(5):
          texto(R33[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    elif questao_escolhida == 34:
      texto(Q34, preto, 30, largura-950,altura-565)
      texto(Q34_1, preto, 30, largura-950,altura-535)
      for i in range(5):
          texto(R34[i], preto, 30, largura-950, (altura-320)+70*(i-1))                   # mostra as alternativas da questão

    pygame.display.update()                                    # atualização da tela
    resposta = 'z'
    
    while resposta == 'z':
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
            mousex = pygame.mouse.get_pos()[0]
            mousey = pygame.mouse.get_pos()[1]
            if mousex > 30 and mousex < 930 and mousey > 200 and mousey < 250:       # reconhece quando o jogador clica na alternativa 'a' 
                resposta = 'a'
            if mousex > 30 and mousex < 930 and mousey > 270 and mousey < 320:       # reconhece quando o jogador clica na alternativa 'b'
                resposta = 'b'
            if mousex > 30 and mousex < 930 and mousey > 340 and mousey < 390:       # reconhece quando o jogador clica na alternativa 'c'
                resposta = 'c'
            if mousex > 30 and mousex < 930 and mousey > 410 and mousey < 460:       # reconhece quando o jogador clica na alternativa 'd'
                resposta = 'd'
            if mousex > 30 and mousex < 930 and mousey > 480 and mousey < 530:       # reconhece quando o jogador clica na alternativa 'e'
                resposta = 'e'

        if event.type == pygame.QUIT:
            rodada = 11
            resposta = 'y'
            pygame.quit()
                    
    return resposta, correta[questao_escolhida]

def jogo_quiz():
    fundo.fill(verde)
    texto("  Quiz  ", preto, 400, largura - 1000, altura - 500)
    texto("Clique para continuar", preto, 100, 120, altura - 80)

    clique = False
    pygame.display.update()
    while not(clique):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clique = True
            if event.type == pygame.QUIT:
                pygame.quit()

    while True:
        rodada = 0
        erro = 0
        lista_questoes = sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], 10)

        while erro == 0 and rodada < 10:
            fundo.fill(branco)
            pygame.draw.rect(fundo, salmao, [largura-970, altura-580, 930, 150])       # cria o retângulo das perguntas 
            pygame.draw.rect(fundo, agua, [largura-970, altura-400, 930, 50])          # cria o retângulo da alternativa 'a'
            pygame.draw.rect(fundo, agua, [largura-970, altura-330, 930, 50])          # cria o retângulo da alternativa 'b'
            pygame.draw.rect(fundo, agua, [largura-970, altura-260, 930, 50])          # cria o retângulo da alternativa 'c'
            pygame.draw.rect(fundo, agua, [largura-970, altura-190, 930, 50])          # cria o retângulo da alternativa 'd'
            pygame.draw.rect(fundo, agua, [largura-970, altura-120, 930, 50])          # cria o retângulo da alternativa 'e'

            resposta_dada, resposta_correta = gera_questao(lista_questoes[rodada])
            if resposta_dada == resposta_correta:                     # caso a resposta esteja correta, uma nova pergunta é gerada para o jogador
                rodada += 1
            else:                                                     # caso a resposta esteja incorreta, o jogo fecha
                erro = 1

        if erro:
            fundo.fill(tomate)
            texto("GAME OVER!", preto, 200, largura - 950, altura - 400)
            pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
            pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
            texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
            texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
            pygame.display.update()
            clique = False
            while not(clique):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                            mousex = pygame.mouse.get_pos()[0]
                            mousey = pygame.mouse.get_pos()[1]
                            if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                clique = True
                            if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                return 0
                    if event.type == pygame.QUIT:
                        clique = True
                        pygame.quit()
                        exit()

        else:
            fundo.fill(agua)
            texto("VITORIA   :)", salmao, 200, largura - 950, altura - 400)
            pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
            pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
            texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
            texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
            pygame.display.update()
            clique = False
            while not(clique):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                            mousex = pygame.mouse.get_pos()[0]
                            mousey = pygame.mouse.get_pos()[1]
                            if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                clique = True
                            if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                return 0
                    if event.type == pygame.QUIT:
                        clique = True
                        pygame.quit()
                        exit()









def jogo_memoria():
    #JOGO DA MEMÓRIA

    #as cartas sao divididas em tres linhas e 6 colunas
    #cada linha é representada pela letra da variavel e cada coluna pelo numero desta
    #o valor das variaveis com letras em maiusculo representam o status da carta naquela posicao
    #virada pra baixo=1
    #virada pra cima=2
    #pares certos=3
    #o valor das varievaies com letras em minusculo representam o numero daquela carta
    while True:     
        A1=1
        A2=1
        A3=1
        A4=1
        A5=1
        A6=1
        B1=1
        B2=1
        B3=1
        B4=1
        B5=1
        B6=1
        C1=1
        C2=1
        C3=1
        C4=1
        C5=1
        C6=1

        #sorteia o numero de cada carta
        Pecas=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
        shuffle(Pecas)
        a1=Pecas[0]
        a2=Pecas[1]
        a3=Pecas[2]
        a4=Pecas[3]
        a5=Pecas[4]
        a6=Pecas[5]
        b1=Pecas[6]
        b2=Pecas[7]
        b3=Pecas[8]
        b4=Pecas[9]
        b5=Pecas[10]
        b6=Pecas[11]
        c1=Pecas[12]
        c2=Pecas[13]
        c3=Pecas[14]
        c4=Pecas[15]
        c5=Pecas[16]
        c6=Pecas[17]

        #largura e altura da tela
        larg=640
        alt=480
        fundo = pygame.display.set_mode((larg,alt))
        fundo.fill(preto)                             #torna o fundo preto

        vidas=10
        cartavirada1=0          #numero da primeira carta virada
        cartavirada2=0          #numero da segunda carta virada
        cartaviradastatus1=0    #indica o status da primeira carta virada, somente virada para cima ou com par feito(2 ou 3 respectivamente)
        cartaviradastatus2=0    #indica o status da segunda carta virada, somente virada para cima ou com par feito(2 ou 3 respectivamente)

        #Desenhos dos retangulos das cartas
        pygame.draw.rect(fundo,branco,[(larg*0.109375)-30,(alt*0.158333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.265625)-30,(alt*0.158333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.421875)-30,(alt*0.158333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.578125)-30,(alt*0.158333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.734375)-30,(alt*0.158333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.890625)-30,(alt*0.158333)-50,60,100])
            
        pygame.draw.rect(fundo,branco,[(larg*0.109375)-30,(alt*0.420833)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.265625)-30,(alt*0.420833)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.421875)-30,(alt*0.420833)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.578125)-30,(alt*0.420833)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.734375)-30,(alt*0.420833)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.890625)-30,(alt*0.420833)-50,60,100])  
            
        pygame.draw.rect(fundo,branco,[(larg*0.109375)-30,(alt*0.683333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.265625)-30,(alt*0.683333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.421875)-30,(alt*0.683333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.578125)-30,(alt*0.683333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.734375)-30,(alt*0.683333)-50,60,100])
        pygame.draw.rect(fundo,branco,[(larg*0.890625)-30,(alt*0.683333)-50,60,100])

        #desenhos dos circulos das vidas
        pygame.draw.circle(fundo,vermelho,[11+35,429],25)
        pygame.draw.circle(fundo,vermelho,[72+35,429],25)
        pygame.draw.circle(fundo,vermelho,[133+35,429],25)
        pygame.draw.circle(fundo,vermelho,[194+35,429],25)
        pygame.draw.circle(fundo,vermelho,[255+35,429],25)
        pygame.draw.circle(fundo,vermelho,[316+35,429],25)
        pygame.draw.circle(fundo,vermelho,[377+35,429],25)
        pygame.draw.circle(fundo,vermelho,[438+35,429],25)
        pygame.draw.circle(fundo,vermelho,[499+35,429],25)
        pygame.draw.circle(fundo,vermelho,[560+35,429],25)

        #atualiza a tela
        pygame.display.update()

        #laco de repeticão que se finaliza quando o usuario perde, ganha ou fecha o jogo
        while vidas!=0 and (A1+A2+A3+A4+A5+A6+B1+B2+B3+B4+B5+B6+C1+C2+C3+C4+C5+C6) != 54:
            #laco que define qual carta foi clicada e a vira para cima
            while cartavirada1==0 and cartaviradastatus1==0:
                #comando que reconhece eventos durante a execução (clique do mouse, comando como alt+f4, etc
                for event in pygame.event.get(): 
                    if event.type==pygame.QUIT:                          #verifica se foi clicado para fechar a aba
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:           #comando que reconhece o clique do mouse
                        mousex=pygame.mouse.get_pos()[0]                 #armazena a coordenada x em que o mouse clicou
                        mousey=pygame.mouse.get_pos()[1]                 #armazena a coordenada y em que o mouse clicou             
                        #condicional que determinara qual a primeira carta que devera ser virada para cima baseado na posicao que o jogador clicou
                        if (mousex >40 and mousex < 100 and mousey > 26 and mousey < 126) and A1==1:
                            texto(str(a1),amarelo,100,40+10,26+20)
                            A1=2
                            cartavirada1=a1
                            cartaviradastatus1=A1
                        elif (mousex >140 and mousex < 200 and mousey > 26 and mousey < 126) and A2==1:
                            texto(str(a2),amarelo,100,140+10,26+20)
                            A2=2
                            cartavirada1=a2
                            cartaviradastatus1=A2
                        elif (mousex >240 and mousex < 300 and mousey > 26 and mousey < 126) and A3==1:
                            texto(str(a3),amarelo,100,240+10,26+20)
                            A3=2
                            cartavirada1=a3
                            cartaviradastatus1=A3
                        elif (mousex >340 and mousex < 400 and mousey > 26 and mousey < 126) and A4==1:
                            texto(str(a4),amarelo,100,340+10,26+20)
                            A4=2
                            cartavirada1=a4
                            cartaviradastatus1=A4
                        elif (mousex >440 and mousex < 500 and mousey > 26 and mousey < 126) and A5==1:
                            texto(str(a5),amarelo,100,440+10,26+20)
                            A5=2
                            cartavirada1=a5
                            cartaviradastatus1=A5
                        elif (mousex >540 and mousex < 600 and mousey > 26 and mousey < 126) and A6==1:
                            texto(str(a6),amarelo,100,540+10,26+20)
                            A6=2
                            cartavirada1=a6
                            cartaviradastatus1=A6
                        elif (mousex >40 and mousex < 100 and mousey >152 and mousey < 252) and B1==1:
                            texto(str(b1),amarelo,100,40+10,152+20)
                            B1=2
                            cartavirada1=b1
                            cartaviradastatus1=B1
                        elif (mousex >140 and mousex < 200 and mousey >152 and mousey < 252) and B2==1:
                            texto(str(b2),amarelo,100,140+10,152+20)
                            B2=2
                            cartavirada1=b2
                            cartaviradastatus1=B2
                        elif (mousex >240 and mousex < 300 and mousey >152 and mousey < 252) and B3==1:
                            texto(str(b3),amarelo,100,240+10,152+20)
                            B3=2
                            cartavirada1=b3
                            cartaviradastatus1=B3
                        elif (mousex >340 and mousex < 400 and mousey > 152 and mousey < 252) and B4==1:
                            texto(str(b4),amarelo,100,340+10,152+20)
                            B4=2
                            cartavirada1=b4
                            cartaviradastatus1=B4
                        elif (mousex >440 and mousex < 500 and mousey > 152 and mousey < 252) and B5==1:
                            texto(str(b5),amarelo,100,440+10,152+20)
                            B5=2
                            cartavirada1=b5
                            cartaviradastatus1=B5
                        elif (mousex >540 and mousex < 600 and mousey > 152 and mousey < 252) and B6==1:
                            texto(str(b6),amarelo,100,540+10,152+20)
                            B6=2
                            cartavirada1=b6
                            cartaviradastatus1=B6
                        elif (mousex >40 and mousex < 100 and mousey > 278 and mousey < 378) and C1==1:
                            texto(str(c1),amarelo,100,40+10,278+20)
                            C1=2
                            cartavirada1=c1
                            cartaviradastatus1=C1
                        elif (mousex >140 and mousex < 200 and mousey > 278 and mousey < 378) and C2==1:
                            texto(str(c2),amarelo,100,140+10,278+20)
                            C2=2
                            cartavirada1=c2
                            cartaviradastatus1=C2
                        elif (mousex >240 and mousex < 300 and mousey > 278 and mousey < 378) and C3==1:
                            texto(str(c3),amarelo,100,240+10,278+20)
                            C3=2
                            cartavirada1=c3
                            cartaviradastatus1=C3
                        elif (mousex >340 and mousex < 400 and mousey > 278 and mousey < 378) and C4==1:        
                            texto(str(c4),amarelo,100,340+10,278+20)
                            C4=2
                            cartavirada1=c4
                            cartaviradastatus1=C4
                        elif (mousex >440 and mousex < 500 and mousey > 278 and mousey < 378) and C5==1:
                            texto(str(c5),amarelo,100,440+10,278+20)
                            C5=2
                            cartavirada1=c5
                            cartaviradastatus1=C5
                        elif (mousex >540 and mousex < 600 and mousey > 278 and mousey < 378) and C6==1:
                            texto(str(c6),amarelo,100,540+10,278+20)
                            C6=2
                            cartavirada1=c6
                            cartaviradastatus1=C6
            pygame.display.update()
            #laco que define qual a segunda carta escolhida
            while cartavirada2==0 and cartaviradastatus2==0:
                #comando que reconhece eventos durante a execução (clique do mouse, comando como alt+f4, etc
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:                  #verifica se foi clicado para fechar a aba
                        pygame.quit()
                    elif (event.type == pygame.MOUSEBUTTONDOWN): #comando que reconhece o clique do mouse
                        mousex=pygame.mouse.get_pos()[0]         #armazena a coordenada x em que o mouse clicou
                        mousey=pygame.mouse.get_pos()[1]         #armazena a coordenada y em que o mouse clicou       
                        #condicional que determinara qual a primeira carta que devera ser virada para cima baseado na posicao do clique do jogador 
                        if (mousex >40 and mousex < 100 and mousey > 26 and mousey < 126) and A1==1:
                            texto(str(a1),amarelo,100,40+10,26+20)
                            A1=2
                            cartavirada2=a1
                            cartaviradastatus2=A1
                        elif (mousex >140 and mousex < 200 and mousey > 26 and mousey < 126) and A2==1:
                            texto(str(a2),amarelo,100,140+10,26+20)
                            A2=2
                            cartavirada2=a2
                            cartaviradastatus2=A2
                        elif (mousex >240 and mousex < 300 and mousey > 26 and mousey < 126) and A3==1:
                            texto(str(a3),amarelo,100,240+10,26+20)
                            A3=2
                            cartavirada2=a3
                            cartaviradastatus2=A3
                        elif (mousex >340 and mousex < 400 and mousey > 26 and mousey < 126) and A4==1:
                            texto(str(a4),amarelo,100,340+10,26+20)
                            A4=2
                            cartavirada2=a4
                            cartaviradastatus2=A4
                        elif (mousex >440 and mousex < 500 and mousey > 26 and mousey < 126) and A5==1:
                            texto(str(a5),amarelo,100,440+10,26+20)
                            A5=2
                            cartavirada2=a5
                            cartaviradastatus2=A5
                        elif (mousex >540 and mousex < 600 and mousey > 26 and mousey < 126) and A6==1:
                            texto(str(a6),amarelo,100,540+10,26+20)
                            A6=2
                            cartavirada2=a6
                            cartaviradastatus2=A6
                        elif (mousex >40 and mousex < 100 and mousey >152 and mousey < 252) and B1==1:
                            texto(str(b1),amarelo,100,40+10,152+20)
                            B1=2
                            cartavirada2=b1
                            cartaviradastatus2=B1
                        elif (mousex >140 and mousex < 200 and mousey >152 and mousey < 252) and B2==1:
                            texto(str(b2),amarelo,100,140+10,152+20)
                            B2=2
                            cartavirada2=b2
                            cartaviradastatus2=B2
                        elif (mousex >240 and mousex < 300 and mousey >152 and mousey < 252) and B3==1:
                            texto(str(b3),amarelo,100,240+10,152+20)
                            B3=2
                            cartavirada2=b3
                            cartaviradastatus2=B3
                        elif (mousex >340 and mousex < 400 and mousey > 152 and mousey < 252) and B4==1:
                            texto(str(b4),amarelo,100,340+10,152+20)
                            B4=2
                            cartavirada2=b4
                            cartaviradastatus2=B4
                        elif (mousex >440 and mousex < 500 and mousey > 152 and mousey < 252) and B5==1:
                            texto(str(b5),amarelo,100,440+10,152+20)
                            B5=2
                            cartavirada2=b5
                            cartaviradastatus2=B5
                        elif (mousex >540 and mousex < 600 and mousey > 152 and mousey < 252) and B6==1:
                            texto(str(b6),amarelo,100,540+10,152+20)
                            B6=2
                            cartavirada2=b6
                            cartaviradastatus2=B6
                        elif (mousex >40 and mousex < 100 and mousey > 278 and mousey < 378) and C1==1:
                            texto(str(c1),amarelo,100,40+10,278+20)
                            C1=2
                            cartavirada2=c1
                            cartaviradastatus2=C1
                        elif (mousex >140 and mousex < 200 and mousey > 278 and mousey < 378) and C2==1:
                            texto(str(c2),amarelo,100,140+10,278+20)
                            C2=2
                            cartavirada2=c2
                            cartaviradastatus2=C2
                        elif (mousex >240 and mousex < 300 and mousey > 278 and mousey < 378) and C3==1:
                            texto(str(c3),amarelo,100,240+10,278+20)
                            C3=2
                            cartavirada2=c3
                            cartaviradastatus2=C3
                        elif (mousex >340 and mousex < 400 and mousey > 278 and mousey < 378) and C4==1:        
                            texto(str(c4),amarelo,100,340+10,278+20)
                            C4=2
                            cartavirada2=c4
                            cartaviradastatus2=C4
                        elif (mousex >440 and mousex < 500 and mousey > 278 and mousey < 378) and C5==1:
                            texto(str(c5),amarelo,100,440+10,278+20)
                            C5=2
                            cartavirada2=c5
                            cartaviradastatus2=C5
                        elif (mousex >540 and mousex < 600 and mousey > 278 and mousey < 378) and C6==1:
                            texto(str(c6),amarelo,100,540+10,278+20)
                            C6=2
                            cartavirada2=c6
                            cartaviradastatus2=C6
            pygame.display.update()            
            pygame.time.delay(1000)          #deixa as cartas escolhidas a mostra antes de vira-las para baixo novamente

            #condicional que compara as duas cartas viradas pelo usuario e determina se fazem par ou nao (caso não faca, o usuario perde uma vida e as cartas sao desviradas)
            if cartavirada1!=cartavirada2:
                if A1==2:
                    A1=1
                    pygame.draw.rect(fundo,branco,[(larg*0.109375)-30,(alt*0.158333)-50,60,100])
                if A2==2:
                    A2=1
                    pygame.draw.rect(fundo,branco,[(larg*0.265625)-30,(alt*0.158333)-50,60,100])
                if A3==2:
                    A3=1
                    pygame.draw.rect(fundo,branco,[(larg*0.421875)-30,(alt*0.158333)-50,60,100])
                if A4==2:
                    A4=1
                    pygame.draw.rect(fundo,branco,[(larg*0.578125)-30,(alt*0.158333)-50,60,100])
                if A5==2:
                    A5=1
                    pygame.draw.rect(fundo,branco,[(larg*0.734375)-30,(alt*0.158333)-50,60,100])
                if A6==2:
                    A6=1
                    pygame.draw.rect(fundo,branco,[(larg*0.890625)-30,(alt*0.158333)-50,60,100])
                  
                if B1==2:
                    B1=1
                    pygame.draw.rect(fundo,branco,[(larg*0.109375)-30,(alt*0.420833)-50,60,100])
                if B2==2:
                    B2=1
                    pygame.draw.rect(fundo,branco,[(larg*0.265625)-30,(alt*0.420833)-50,60,100])
                if B3==2:
                    B3=1
                    pygame.draw.rect(fundo,branco,[(larg*0.421875)-30,(alt*0.420833)-50,60,100])
                if B4==2:
                    B4=1
                    pygame.draw.rect(fundo,branco,[(larg*0.578125)-30,(alt*0.420833)-50,60,100])
                if B5==2:
                    B5=1
                    pygame.draw.rect(fundo,branco,[(larg*0.734375)-30,(alt*0.420833)-50,60,100])
                if B6==2:
                    B6=1
                    pygame.draw.rect(fundo,branco,[(larg*0.890625)-30,(alt*0.420833)-50,60,100])
                if C1==2:
                    C1=1
                    pygame.draw.rect(fundo,branco,[(larg*0.109375)-30,(alt*0.683333)-50,60,100])
                if C2==2:
                    C2=1
                    pygame.draw.rect(fundo,branco,[(larg*0.265625)-30,(alt*0.683333)-50,60,100])
                if C3==2:
                    C3=1
                    pygame.draw.rect(fundo,branco,[(larg*0.421875)-30,(alt*0.683333)-50,60,100])
                if C4==2:
                    C4=1
                    pygame.draw.rect(fundo,branco,[(larg*0.578125)-30,(alt*0.683333)-50,60,100])
                if C5==2:
                    C5=1
                    pygame.draw.rect(fundo,branco,[(larg*0.734375)-30,(alt*0.683333)-50,60,100])
                if C6==2:
                    C6=1
                    pygame.draw.rect(fundo,branco,[(larg*0.890625)-30,(alt*0.683333)-50,60,100])

                vidas = vidas -1

            elif cartavirada1==cartavirada2:
                if cartaviradastatus1==A1:
                    A1=3
                elif cartaviradastatus1==A2:
                    A2=3
                elif cartaviradastatus1==A3:
                    A3=3
                elif cartaviradastatus1==A4:
                    A4=3
                elif cartaviradastatus1==A5:
                    A5=3
                elif cartaviradastatus1==A6:
                    A6=3
                elif cartaviradastatus1==B1:
                    B1=3
                elif cartaviradastatus1==B2:
                    B2=3
                elif cartaviradastatus1==B3:
                    B3=3
                elif cartaviradastatus1==B4:
                    B4=3
                elif cartaviradastatus1==B5:
                    B5=3
                elif cartaviradastatus1==B6:
                    B6=3
                elif cartaviradastatus1==C1:
                    C1=3
                elif cartaviradastatus1==C2:
                    C2=3
                elif cartaviradastatus1==C3:
                    C3=3
                elif cartaviradastatus1==C4:
                    C4=3
                elif cartaviradastatus1==C5:
                    C5=3
                elif cartaviradastatus1==C6:
                    C6=3
                if cartaviradastatus2==A1:
                    A1=3
                elif cartaviradastatus2==A2:
                    A2=3
                elif cartaviradastatus2==A3:
                    A3=3
                elif cartaviradastatus2==A4:
                    A4=3
                elif cartaviradastatus2==A5:
                    A5=3
                elif cartaviradastatus2==A6:
                    A6=3
                elif cartaviradastatus2==B1:
                    B1=3
                elif cartaviradastatus2==B2:
                    B2=3
                elif cartaviradastatus2==B3:
                    B3=3
                elif cartaviradastatus2==B4:
                    B4=3
                elif cartaviradastatus2==B5:
                    B5=3
                elif cartaviradastatus2==B6:
                    B6=3
                elif cartaviradastatus2==C1:
                    C1=3
                elif cartaviradastatus2==C2:
                    C2=3
                elif cartaviradastatus2==C3:
                    C3=3
                elif cartaviradastatus2==C4:
                    C4=3
                elif cartaviradastatus2==C5:
                    C5=3
                elif cartaviradastatus2==C6:
                    C6=3
            #condicional que retira as vidas da tela
            if vidas==9:
                pygame.draw.circle(fundo,preto,[560+35,429],25)
            if vidas==8:
                pygame.draw.circle(fundo,preto,[499+35,429],25)
            if vidas==7:
                pygame.draw.circle(fundo,preto,[438+35,429],25)
            if vidas==6:
                pygame.draw.circle(fundo,preto,[377+35,429],25)
            if vidas==5:
                pygame.draw.circle(fundo,preto,[316+35,429],25)
            if vidas==4:
                pygame.draw.circle(fundo,preto,[255+35,429],25)
            if vidas==3:
                pygame.draw.circle(fundo,preto,[194+35,429],25)
            if vidas==2:
                pygame.draw.circle(fundo,preto,[133+35,429],25)
            if vidas==1:
                pygame.draw.circle(fundo,preto,[72+35,429],25)
            if vidas==0:
                pygame.draw.circle(fundo,preto,[11+35,429],25)
                pygame.display.update()
                pygame.time.delay(500)
            #reseta as variaveis para que o programa consiga ler novamente 2 novas cartas
            cartaviradastatus1=0
            cartaviradastatus2=0
            cartavirada1=0
            cartavirada2=0
            pygame.display.update()          



            
        #após o primeiro laco de repeticão acabar, o jogo é levado a uma das duas telas possiveis (vitoria ou derrota)  
        if vidas == 0:
            fundo = pygame.display.set_mode((largura,altura))
            fundo.fill(tomate)
            texto("GAME OVER!", preto, 200, largura - 950, altura - 400)
            pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
            pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
            texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
            texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
            pygame.display.update()
            clique = False
            while not(clique):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                            mousex = pygame.mouse.get_pos()[0]
                            mousey = pygame.mouse.get_pos()[1]
                            if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                clique = True
                            if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                return 0
                    if event.type == pygame.QUIT:
                        clique = True
                        pygame.quit()
                        exit()
        else:
            fundo = pygame.display.set_mode((largura,altura))
            fundo.fill(agua)
            texto("VITORIA   :)", salmao, 200, largura - 950, altura - 400)
            pygame.draw.rect(fundo, preto, [0, 7*(altura/8), largura, altura/8])
            pygame.draw.rect(fundo, branco, [largura/2 -1, 7*(altura/8), 2, altura/8])
            texto("Reiniciar", branco, 100, 90, 7*altura/8 + 8)
            texto("Sair", branco, 100, largura/2 + 180, 7*altura/8 + 8)
            pygame.display.update()
            clique = False
            while not(clique):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                            mousex = pygame.mouse.get_pos()[0]
                            mousey = pygame.mouse.get_pos()[1]
                            if  mousex < largura/2 - 1 and mousey > 7*altura/8:
                                clique = True
                            if mousex > largura/2 + 1 and mousey > 7*altura/8:
                                return 0
                    if event.type == pygame.QUIT:
                        clique = True
                        pygame.quit()
                        exit()
            
                          














sair = False
while not(sair):
    clique = False
    fundo.fill(preto)
    pygame.draw.rect(fundo, branco, [0, 30, largura, 140])
    pygame.draw.rect(fundo, branco, [0, 200, largura, 70])
    pygame.draw.rect(fundo, branco, [0, 300, largura, 70])
    pygame.draw.rect(fundo, branco, [0, 400, largura, 70])
    pygame.draw.rect(fundo, branco, [0, 500, largura, 70])
    texto("MINI JOGOS", preto, 150, 200, 50)
    texto("Genius", verde, 100, 370, 205)
    texto("Quiz", agua, 100, 410, 300)
    texto("Memória", vermelho, 100, 350, 405)
    texto("Snake", verde, 100, 390, 505)
    pygame.display.update()
    while not(clique):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                      # reconhece onde o jogador está clicando com o mouse
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]
                if mousey > 200 and mousey < 280:
                    reiniciar = jogo_genius()
                    while reiniciar:
                        reiniciar = jogo_genius()
                    clique = True
                if mousey > 300 and mousey < 380:
                    jogo_quiz()
                    clique = True
                if mousey > 400 and mousey < 480:
                    jogo_memoria()
                    clique = True
                if mousey > 500 and mousey < 580:
                    jogo_cobra()
                    clique = True
            if event.type == pygame.QUIT:
                sair = True
                clique = True

pygame.quit()
exit()
