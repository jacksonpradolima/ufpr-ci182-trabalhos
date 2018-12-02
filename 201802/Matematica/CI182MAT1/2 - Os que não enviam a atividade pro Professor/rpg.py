'''
    Jogo de RPG em python
'''

from random import randint
import os
#comandos que o jogador pode utilizar
Chaves_de_comandos = """
-Status: Ver saude e nivel
-Descansar: Recuperar saude
-Explorar: Procura o caminho de casa podendo encontrar monstros maléficos
-Habilidades : Mostra as habilidades da classe escolhida
-Todos os comandos podem ser escritos em letra minúscula
-Sair: Sai do jogo
"""

class Dado:
	#Cria a classe Dado, define a função rolar com os parâmetros x, lados e retorna um valor entre x e o número lados.
    def rolar(x,lados):
        return randint(x,lados)
        

class Personagem:
    def __init__(self,nome,saude,exp):
        self.nome = nome
        self.saude = saude
        self.exp = exp
    ''' 
    Cria a classe Personagem, que será utilizada em mobs e no personagem principal. A classe personagem contém nome, 
    saude e pontos de experiência do mob ou jogador. def _init_ inicia toda vez que um objeto da classe é criado e os parâmetros (self,nome,hp,exp).
    '''

class Guerreiro(Personagem):
	#Aqui é definida a classe Guerreiro, que é umas das possíveis escolhas para o jogador.
    def __init__(self): 
        super().__init__(nome =input("Você se tornou um guerreiro que não teme a morte, que nome você dirá à fada? "), saude=18, exp=4) # super(). é pra chamar a classe Personagem
    prof = "guerreiro" #classe do personagem
    max_saude = 18 #vida maxima inicial
    nivel = 1 #nivel inicial
    dano_max = Dado.rolar(2,15) #dano de ataque
    ganho_vida = 3 #aumento na vida maxima
    nivel2 = 20 #experiência necessária para passar de nível
    ''' 
    Aqui definimos a saude (pontos de vida) inicial Guerreiro como 15 por padrão. O dano inicial dele foi definido como uma rolagem de dado que 
    varia de 2 a 15. O personagem começa no nível 1 e conforme seu nível nível aumenta também há um ganho de vida.
    '''
    

    def lutar(self):
        lutar()

    def bankai(self):

        heroi.saude -= 4 #perde isso de vida quando usa a habilidade
        if heroi.saude > 0:
            rollD = Dado.rolar(15,25)
            print("\nVocê usou bankai causando", rollD, "de dano")
            mob.saude -= rollD #vida que o monstro perde
            print("O", mob.nome, "esta com", mob.saude,"de vida")
        else:
            print("Você morreu!")
    

    Comandos = { # dicionário com os comandos
            'l': ('lutar', lutar),
            'b': ('bankai', bankai)
            }

class Mago(Personagem):
	#Aqui é definida a classe Mago, a segunda escolha possível para o jogador.
    def __init__(self):
        super().__init__(nome =input("Você se tornou um mago que busca o conhecimento incessantemente, que nome você dirá à fada? "), saude=15, exp=4)
    prof = "mago" #classe do personagem
    mana = 1 #mana inicial
    max_mana = 1 #mana maxima inicial
    max_saude = 15 #vida maxima inicial
    nivel = 1 #nivel incial 
    dano_max = Dado.rolar(1,10) #dano de ataque
    ganho_vida = 2  #aumento na vida maxima
    nivel2 = 12 #experiencia necessaria para passar de nivel
    
    '''
    Assim como no Guerreiro, aqui na Classe do Mago foram definidos os pontos de vida iniciais, o dano inicial e o nível que o jogador começa. 
    Mas o ganho de vida por nível foi reduzido e a experiência para aumentar seu nível também. Outra diferença é que colocamos um parâmetro mana para o 
    Mago poder utilizar magias (Será visto logo em seguida)
    '''

    def lutar(self):
        lutar()
    
    def missil_magico(self):
        if heroi.mana > 0:
            rollD = Dado.rolar(5,12) # dano da habilidade
            Mago.mana -= 1 #perde 1 de mana quando usa a habilidade
            print("\nVocê usou Mísssil mágico causando", rollD, "de dano")
            mob.saude -= rollD #vida que o monstro perde
            print("O", mob.nome, "esta com", mob.saude,"de vida")
        else:
            print("Mana insuficiente")

    def bola_de_fogo(self):
        if heroi.nivel >= 5: #condiçao para o uso da habilidade
            if heroi.mana > 2:
                rollD = Dado.rolar(15,30) # dano da habilidade
                heroi.mana -= 3 #consome 3 de mana
                print("\nVocê usou Bola de fogo causando", rollD, "de dano")
                mob.saude -= rollD #vida que o monstro perde
                print("O", mob.nome, "esta com", mob.saude,"de vida")
            else:
                print("Mana insuficiente")
        else:
            print("Nível mínimo 5")

        ''' 
        Assim como o Guerreiro, o Mago tem a opção "lutar" que utiliza o Dado para dar um ataque simples no inimigo. Definimos o "míssil_magico" e a
        "bola_de_fogo" como habilidades especiais (com parâmetros de dano maiores) assim como no guerreiro, mas o mago utiliza a mana para poder usar
        suas habilidades, caso não tenha mana não será possível utiliza-las em combate. A Bola de fogo por ter parâmetros de dano bastante elevados
        só poderá ser utilizada a partir do nível 5.
        '''

    
    def gerar_mana(self):
        if Mago.mana < Mago.max_mana:   
            Mago.mana += 1 #ganha 1 de mana quando usa o comando durante a batalha
            print("Mana atual: {0}/{1}".format(Mago.mana,Mago.max_mana))
        else:
            print("Mana máxima!")
    ''' 
    Gera mana para o jogador poder utilizar as habilidades do Mago novamente
    '''    
    Comandos = { # dicionário igual ao do anterior
            'l': ('lutar', lutar) ,
            'm': ('missil_magico', missil_magico),
            'f': ('bola_de_fogo', bola_de_fogo),
            'g': ('gerar_mana', gerar_mana),
            }
'''
 As classes a seguir são os mobs(monstros) que nós preparamos para as batalhas, cada um com seus parâmetros de Dano, 
Vida e habilidades próprias
'''
    
class Boss(Personagem):
    ''' 
        Classe Boss, herdando os parâmetros da classe Personagem, com super(). Definimos o dano base como uma rolagem de dados entre 4 e 15 
    e a habilidade choque_do_trovao como uma rolagem entre 5 e 18, que serão as habilidades que o Boss poderá utilizar em batalha.
    '''
    def __init__(self):
            super().__init__(nome = "Pikachu", saude = 40, exp = 40) 
    dano_max = Dado.rolar(4,15) #dano de ataque
    choque_do_trovao = Dado.rolar(5,18) #dano da habilidade

class Globin(Personagem):
    '''
    Classe Globin, herdando os parâmetros da classe Personagem, com super(). Definimos seu dano base como uma rolagem entre 1 e 6.
    '''
    def __init__(self):
            super().__init__(nome = "Globin", saude = 8, exp = 6) 
    dano_max = Dado.rolar(1,6) #dano que o monstro causa
    

class Orc(Personagem):
    ''' 
    Classe Orc, herdando os parâmetros da classe Personagem, com super(). Definimos seu dano base como uma rolagem entre 3 e 8.
    '''
    def __init__(self):
            super().__init__(nome = "Orc", saude = 10, exp = 8)
    dano_max = Dado.rolar(3,8) #dano que o monstro causa
    


class Sombra(Personagem):
    ''' 
    Classe Sombra, herdando os parâmetros da classe Personagem, com super(). Definimos seu dano base como uma rolagem entre 2 e 10, e também 
    uma magia com o dano sendo uma rolagem entre 5 e 12.
    '''
    def __init__(self):
            super().__init__(nome = "Sombra", saude = 20, exp = 15)
    dano_max = Dado.rolar(2,10) #dano que o monstro causa no ataque
    magia = Dado.rolar(5,12) #dano que o monstro causa na habilidade

class Esqueleto(Personagem):
    ''' 
    Classe Esqueleto, herdando os parâmetros da classe Personagem, com super(). Definimos seu dano base como uma rolagem entre 3 e 15
    '''
    def __init__(self):
            super().__init__(nome = "Esqueleto", saude = 20, exp = 15)
    dano_max = Dado.rolar(3,15) #dano que o monstro causa

class Piratas(Personagem):
    ''' 
    Classe Piratas, herdando os parâmetros da classe Personagem, com super(). Definimos seu dano base como uma rolagem entre 4 e 11
    '''
    def __init__(self):
            super().__init__(nome = 'Piratas', saude = 25, exp = 25)
    dano_max = Dado.rolar(4,11) #dano que o oponente causa

def random_mob():
    ''' 
    Aqui é definido o mob da vez. Sempre que essa função é chamada, um dado é rolado e tem uma chance de cair em um mob
    diferente, a função leva em conta tanto nível do jogador quanto a rolagem(Quanto maior o nível do jogador, mais fortes 
    serão os mobs que podemaparecer). O mob que saírá dessa função pelo return é mesmo que o jogador irá enfrentar na próxima
    vez que a função batalha() for chamada.  
    '''
    chance = Dado.rolar(1,9)
    if heroi.nivel < 2:
        mob = Globin()
    elif heroi.nivel >= 2 and heroi.nivel < 5:
        if chance >= 5:
            mob = Globin()
        else:
            mob = Orc()
    elif heroi.nivel >= 5 and heroi.nivel < 9:
        if chance >= 8:
            mob = Sombra()
        elif chance < 8 and chance > 5:
            mob = Esqueleto()
        elif chance <= 5 and chance > 3:
            mob = Orc()       
        else:
            mob = Globin()
    elif heroi.nivel >= 9 and heroi.nivel <13 and heroi.nivel != 10:
        if chance >=5:
            mob = Esqueleto()
        else:
            mob = Sombra()
    elif heroi.nivel == 10:
            mob = Piratas()
    else:
        mob = Boss()
    return mob

def profissao():
    '''
    qui é definida a Classe que o jogador irá utilizar no jogo: Mago ou Guerreiro. Caso o jogador escolha o tomo, ele irá 
    utilizar as funções e parâmetros do Mago para jogar. Caso escolha a espada as funções e parâmetros serão as do Guerreiro, 
    já definidas anteriormente.
    '''
    print("Você escolhe a espada ou o tomo?\n")
    print("Espada: Guerreiro\nTomo: Mago")
    classe = input(">")
    while classe != 'espada' and classe != 'tomo':
        print("Comando inválido") 
        classe = input("Digite novamente: ")
    if classe == "espada":
        return Guerreiro()  #escolhe a classe guerreiro com base na seleçao do item
    else:
        return Mago() #escolhe a classe mago com base na seleçao do item

class Ataque():
    ''' 
    Já definimos os parâmetros de dano e habilidades tanto do jogador quanto dos mobs. Agora falta dizer quando um mob vai 
    utilizar um ataque normal ou uma habilidade diferente e é isso que essa classe faz! Definimos a partir de rolagem de dados
    se o mob irá utilizar um ataque mais básico ou a sua habilidade especial. Também foram utilizados dados para dizer se o ataque
    acertou ou não, inclusive os ataques do jogador, e caso o ataque acerte ele será descontado da vida do alvo.
        A função também conta com prints atualizando o jogador sobre acertos e erros de ataques, vida atual do alvo após ser 
    atingido e também informando quando o mob utiliza uma habilidade especial.
    '''

    def jogador(): 
        roll = Dado.rolar(1,10)
        if roll >= 5: #condiçao para acerto/erro do ataque do jogador
            rollD = heroi.dano_max  #dano do ataque
            print("\nVocê acertou com", rollD, "de dano")
            mob.saude -= rollD #perda de vida do monstro
            print("O", mob.nome, "esta com", mob.saude,"de vida") 
        else:
            print("\nVoce errou!") 

    def mob(): # Dano dos monstros
        roll = Dado.rolar(1,20)
        if mob.nome == "Sombra":
            if roll >= 10:
                rollD = mob.dano_max # dano aleatório
                print(mob.nome,"acertou com",rollD,"de dano")
                heroi.saude -= rollD # vida que o herói perde
                print(heroi.nome,"tem",heroi.saude,"de vida\n")
            else:
                rollD = mob.magia  
                print(mob.nome,"usou a habilidade sugar vida causando",rollD,"de dano")
                heroi.saude -= rollD  # vida que o herói perde no ataque
                print(heroi.nome,"tem",heroi.saude,"de vida\n")
        if mob.nome == 'Boss': # dano do boss
            if roll >= 12:
                rollD = mob.dano_max  
                print(mob.nome,"acertou com",rollD,"de dano")
                heroi.saude -= rollD 
                print(heroi.nome,"tem",heroi.saude,"de vida\n")
            else:
                rollD = Boss.choque_do_trovao 
                print(mob.nome,"usou choque_do_trovao",rollD,"de dano")
                heroi.saude -= rollD 
                print(heroi.nome,"tem",heroi.saude,"de vida\n")
        if roll >= 10 and mob.nome != 'Sombra' and mob.nome != 'Boss':
            rollD = mob.dano_max 
            print("O",mob.nome,"acertou com",rollD,"de dano")
            heroi.saude -= rollD  
            print(heroi.nome,"tem",heroi.saude,"de vida\n")
        else:
            print("O",mob.nome,"errou!\n")

def Subir_nivel():
    ''' 
    Definimos que na classe Guerreiro e Mago como padrão que o jogador deverá começar no nível 1. Agora é a parte em que 
    definimos as vantagens de subir de nível. Quando a experiência do jogador for maior ou igual a experiência necessária para
    personagem. Caso esteja jogando com o Mago também haverá ganho de mana.
    '''

    if heroi.exp >= heroi.nivel2:
        heroi.nivel += 1 #aumento do nivel
        heroi.nivel2 = heroi.nivel2
        while heroi.saude <= (heroi.max_saude/2): 
            heroi.saude += 1 #ganho de vida
        heroi.max_saude += heroi.ganho_vida #aumento da vida maxima
        if heroi.prof == "mago":
            heroi.max_mana += 1 #aumento da mana maxima
            while heroi.mana <= (heroi.max_mana/2):
                heroi.mana += 1 #ganha mana 
            print("\nVoce subiu de nivel:\nNivel: {0} --> {1}\nVida atual: {2}| Vida máxima:{3} --> {4}\nMana atual: {5} | Mana máxima: {6} --> {7}".format(heroi.nivel-1,heroi.nivel,heroi.saude,heroi.max_saude-2,heroi.max_saude,heroi.mana,heroi.max_mana-1,heroi.max_mana))
        else:
            print("\nVoce subiu de nivel:\nNivel: {0} --> {1}\nVida atual: {2} | Vida máxima: {3} --> {4}".format(heroi.nivel-1,heroi.nivel,heroi.saude,heroi.max_saude-3,heroi.max_saude ))

class Options(Personagem):
    '''
    Aqui é definida como o corpo do jogo por assim dizer. Por ser uma classe muito extensa os comentários serão divididos por
     função para facilitar o entendimento.
     '''
    def ajuda():
        '''
        Essa função é um guia que imprime as ações que o jogador pode tomar.
        '''
        print(Chaves_de_comandos)
    
    def descansar():
        ''' 
        Essa função serve para recuperar a vida do jogador, mas também há uma chance (definida per rolagem de dado) de um mob
        encontrar o jogador e o atacar, neste caso o jogador somente entra em batalha e não chega a recuperar a vida.
        '''
        chance = Dado.rolar(1,5)
        if chance <= 3: 
            if heroi.saude < heroi.max_saude:
                print("Você tirou uma soneca")
                heroi.saude += 1
                print("Você tem {0}/{1} de vida".format(heroi.saude, heroi.max_saude))
            else:
                print("Você está com a vida máxima")
        else:
            print("Você foi atacado por ", mob.nome)
            batalha()

    def habilidades():
        ''' 
        Imprime as habilidades de batalha do jogador conforme a classe escolhida para jogar.
        '''
        if heroi.prof == "mago":
            print('''
-Lutar: Desfere golpes corpo-a-corpo
-Missil mágico: Apesar do nome poderoso, o dano nao é lá grandes coisas
-Bola de fogo: Causa grande dano, porém o gasto de mana aumenta consideravelmente(nivel5)
-Gerar mana: Você recupera sua mana
                ''')
        else:
            print('''
-Lutar: Desfere golpes corpo-a-corpo
-Bankai: Usa a energia vital(saude) para desferir um poderoso golpe
                ''')
    
    def super_mode():
        ''' 
        Essa função foi definida para facilitar testes e apresentações do RPG. Ela aumenta substancialmente a vida e o dano 
        do jogador.
        '''
        heroi.saude = 99
        heroi.dano_max = Dado.rolar(99,99)


   
    def status():
        ''' 
        Imprime os status do jogador: Vida atual e máxima, mana (caso a classe escolhida seja Mago) e nível atual.
        '''
        if heroi.prof == 'mago':
            print("Vida: {0}/{1}".format(heroi.saude, heroi.max_saude))
            print("Mana: {0}/{1}".format(heroi.mana, heroi.max_mana))
            print("Nível: ", heroi.nivel)
        else:
            print("Vida: {0}/{1}".format(heroi.saude, heroi.max_saude)) 
            print("Nível: ", heroi.nivel)

    def sair():
        '''
        Sair do jogo
        '''
        quit()
    
    def explorar(): 
        ''' 
        Essa é a função mais extensa do programa. Aqui nós definimos todos os caminhos e eventos que o jogo oferece. 
        Quando o jogador decide explorar, há uma rolagem de dados que define o evento que irá ocorrer. O dado rola e conforme
        o valor que cai (entre 1 e 15) temos desde eventos mais simples até eventos mais complexos que vão demandar de decisões 
        mais complicadas do usuário.
            Alguns desses eventos têm como parâmetro para a ocontecer o nível do personagem. 
        '''
        lugar = Dado.rolar(1,15)
        if heroi.nivel < 13:
            if heroi.nivel == 5:
                print('''\nPassando por uma trilha na floresta, você se depara com uma cidade, quando se lembra que Valinor, 
a cidade dos elfos, fica nessa trilha.\nLogo que você pisa na cidade um soldado elfo lhe recebe e diz que o rei estava a espera.
Após uma breve caminhada você chega à sala do trono e então o rei elfo lhe recebe e ofereceu um chá para lhe dar as novas. 
Rei elfo: Chegou a informação de que o Pikachu devastou a sua cidade, lamento... Mas tenho boas novas, 
descobri a sua localização e obtive informações cruciais para derrotarmos o monstro. O Pikachu está escondido no fim do vale
das trevas, atualmente com o seu nível seria impossível mata-lo mesmo com o item encantado da fada. Mas 
se você aumentar a sua experiência em batalhas e alcançar o nível 13 você deverá ser capaz de salvar a humanidade! Como prova
de minha boa vontade lhe entrego este pergaminho de sabedoria, ele melhorará as suas habilidades em batalha.
\n -O acessor do Rei aparece na sala e o convoca para um reunião urgente, assim você segue jornada.''')
                heroi.nivel += 1
            elif heroi.nivel == 10:
                print('''
Você chegou à cidade de Fiore, uma cidade bastante perigosa e habitada, principalmente, por humanos. Aqui piratas contrabandeiam 
seus produtos roubados e os cidadãos vivem com medo e à mercê de bandidos. Quando você passa os piratas logo veem o item mágico 
que a fada lhe deu. Você acelera o passo e segue o seu rumo.
\n...\n
Algum tempo depois, já próximo a saída da cidade, os piratas te emboscam e pedem o seu item mágico. Você se rende e entrega ou luta? 
~~Digite: "lutar" ou "entregar"
 ''')
                comando = input(">")
                while comando != "lutar" and comando != "entregar":
                    print("Comando inválido!")
                    comando = input(">")
                if comando == 'entregar':
                    heroi.saude = 0
                    print("Os piratas fugiram rapidamente com o item e você não terá como recuperá-lo. Sem ele você não poderá derrotar pikachu! GAME OVER!!!")
                else:
                    batalha()
                

            else:    
                if lugar == 1:
                    print("\nVocê vê o caminho se dividindo. Deseja seguir para a esquerda ou direita?")
                    caminho = input(">")
                    while caminho != 'esquerda' and caminho != 'direita':
                        print("Comando inválido")
                        caminho = input(">")
                    chance = Dado.rolar(1,5)
                    if chance < 3:
                        if caminho == 'esquerda':
                            print("\nVocê entrou numa caverna aparentemente vazia!")
                        else:
                            print("\nVocê se depara com um deserto tortuoso, em seu estado atual esse caminho é morte certa. Explore outros caminhos.")
                    else:
                        print("\nAndando pela trilha você encontrou um(a)", mob.nome,"\n")
                        batalha()
                elif lugar == 2:
                    print("\nVocê encontrou uma nascente onde jaz um antigo sacerdote. Examinar ou continuar?")
                    comando = input(">")
                    while comando != 'examinar' and comando != 'continuar':
                        print("Comando inválido, digite novamente!")
                        comando = input(">")
                    if comando == "examinar":
                        print("\nVocê encontrou uma escrita que conta a história do sacerdote, deseja ler? Sim ou não")
                        comando2 = input(">")
                        while comando2 != 'sim' and comando2 != 'não':
                            print("Comando inválido, digite novamente!")
                            comando2 = input(">")
                        if comando2 == "sim":
                            print('''\nO Sacerdote Mohandas Karamchand Ghandi foi um líder espiritual e pacifista indiano.
Nasceu na cidade indiana de Bombaim, no ano de 700. Ghandi morreu ao selar Pikachu no ano de 777.''')
                        else:
                            print("\nVocê ignora e escrita e segue caminho...")
                elif lugar == 3:
                    print("Você encontrou uma caverna onde aparentemente monstros habitavam, tome cuidado!",mob.nome, "lhe avistou\n")
                    batalha()
                elif lugar == 4:
                    print("\nVocê tropeça em algo. Ver ou Continuar")
                    comando = input(">")
                    while comando != 'ver' and comando != 'continuar':
                        print("Comando inválido")
                        comando = input(">")
                    if comando == 'ver':
                        print("Você encontrou uma túnel escondido e, ao explora-lo, encontrou um baú escondido num canto escuro.\nO que deseja fazer? Ignorar ou abrir?")
                        comando = input(">")
                        while comando != 'ignorar' and comando != 'abrir':
                            print("Comando inválido")
                            comando = input(">")
                        if comando == 'abrir':
                            print("Ao tentar abrí-lo você desencadeia uma armadilha e um",mob.nome,"te ataca!\n")
                            batalha()
                        else:
                            print("Você vê uma luz no fim do túnel")
                    if comando == 'continuar':
                        chance = Dado.rolar(1,5)
                        if chance > 3:
                            print("Você encontrou", mob.nome,"\n")
                            batalha()
                        else:
                            print("Você sente um calafrio e continua o seu caminho.")
                elif lugar > 5 and lugar <= 7:
                    print("\nVocê encontra uma lápide. Examinar ou Continuar?")
                    comando = input(">")
                    while comando != 'examinar' and comando != 'continuar':
                        print("Comando inválido")
                        comando = input("Digite novamente: ")
                    if comando == 'examinar':
                        print("\nVôcê acha uma joia entre as mãos do esqueleto. Pegar ou Continuar?")
                        comando = input(">")
                        while comando != 'pegar' and comando != 'continuar':
                            print("\nComando inválido, digite novamente!")
                            comando = input("Digite novamente: ")
                        if comando == 'pegar':
                            heroi.saude = 0
                            print("\nSua ganância invocou a ira divina!", heroi.nome," morreu!")
                        else:
                            print("\nPor não ter se deixado levar pela ganância, os espiritos o abençoam!")
                            heroi.saude = heroi.max_saude
                elif lugar == 8:
                    print("Você encontrou uma mensagem no chão. Examinar ou Continuar?")
                    comando = input(">")
                    while comando != 'examinar' and comando != 'continuar':
                        print("Comando inválido")
                        comando = input("Digite novamente: ")
                    if comando == 'examinar':
                        print("\nO que é o que é, o cubo disse pro quadrado?")
                        comando = input(">")
                        print("\nResposta: NA VERDADE EU NÃO SEI HAHAHAH!")
                        print("Sua frustração atraiu um", mob.nome,"\n")
                        batalha()
                elif lugar == 9:
                    print("Você explorou um pequeno deserto.")
                elif lugar == 10:
                    print("Você encontra uma caverna com portões esculpidos em pedra. Deseja entrar? Sim ou não.")
                    comando = input(">")
                    while comando != 'sim' and comando != 'não':
                        print("Comando inválido, digite novamente!")
                        comando = input(">")
                    if comando == 'sim':
                        print('''\nVocê entra na caverna e logo vê escrituras na parede. Ela diz o seguinte: 
-Esta foi uma das mais bonitas cavernas feita pelos elfos. Quando o poderoso Pikachu apareceu pela primeira vez ele atacou não só os humanos, como também os 
elfos. Sendo tirados de seu lar o elfos se espalharam pelo planeta e geraram facções. Uma delas foi os Noldorin, aqueles que fizeram esta caverna tão grandioza 
e explêndida. Após a queda do pikachu alguns de seus lacaios continuaram vagando por aí. Estes encontraram a o portão para a caverna e destruíram esta facção
em poucos dias com uma força imensa.


...


Você ouve um barulho na caverna.
VOCÊ FOI ATACADO POR UM(A) {0}'''.format(mob.nome))
                        batalha()
                    else:
                        print("\nVocê sente um calafrio e uma sensação de desconforto ao seguir caminho. Aparentemente aquela caverna transmitia energias ruins.")
                elif lugar ==11:
                    print('''Você avista ao longe a cidade de Angmarun, antiga cidade das sombras. Lá o Rei das mortos-vivos, servo de Pikachu, comandava o exército dos esqueletos
na batalha contra os humanos. Deseja prosseguir? ~~Sim ou não''')
                    comando = input(">")
                    while comando != 'sim' and comando != 'não' and comando != 'morreu':
                        print("Comando inválido, digite novamente!")
                        comando = input(">")
                    if comando == 'sim':
                        print('''\n\nVocê chega aos portais de Angmarun e logo sente a escuridão que permeia o lugar. À direita há uma grande montanha, aparentemente
quando a cidade era habitada havia uma masmorra lá. À esquerda construções com escritas nefastas, talvez feitiços malígnos, talvez algum
culto ou simplesmente textos de algum livro. Você não consegue ler mas se sente mais pesado apenas ao lançar a visão em direção às escritas.
Em frente se ergue, alto e imponente, o palácio do Rei. Magnífico e ao mesmo tempo aterrorizante.
Onde você deseja explorar? 
    (m) Masmorras.
    
    (c) Construções
    ''')
                        if heroi.saude<=0:
                            comando = 's'
                        else:
                            comando = input(">")
                        while comando != 'm' and comando != 'p' and comando != 'c' and comando != 's':
                                print("Comando inválido, digite novamente!")
                                comando = input(">")
                        while comando != 's':

                            if comando == 'm':
                                print('''\nChegando às masmorras você avista um monte de cinzas que, aparentemente, são de pessoas há muito já mortas. Entrando um pouco mais a fundo
você encontra instrumentos de tortura. Quando de repente \n\n...\n\n"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" você pula aterrorizado. As vozes das pessoas
que sofreram neste lugar estão ecoando na sua cabeça. De repente o céu começa a escurecer e você percebe um temporal se aproximando. Seu coração começa a ficar aflito e você começa
a sentir uma presença malígna se aproximando. Mais do que rápido você sai da cidade das sombras.''')
                                break
                                
                            
                                        
                            elif comando == 'c':
                            	print(" Essas construções foram abandonadas há muito tempo, não há nada aqui. De repente o céu começa a trovejar e ficar roxo. Você sente um poder malígno chegando no lugar e é obrigado a correr da cidade.")
                            	break

                            	
                            
                                	

                                

                                    
                                            
                                    


                
                else:
                    print("Você encontrou", mob.nome,"\n")
                    batalha()
        else:
            print("Um Pikachu selvagem apareceu!\n")
            batalha()

print('''\nSubitamente você acorda em uma caverna e logo a frente avista uma fada. Esta que lhe retribui o olhar e diz:
-Finalmente você acordou! Sua vila foi atacada por um Pikachu e você foi o único sobrevivente. O Pikachu é uma criatura das 
trevas que retorna a cada 1000 anos para atormentar a humanidade. A última vez que ele retornou os humanos foram quase extintos!\n
-Sinto em você um tremendo potencial, será que você lutaria contra o Pikachu para salvar a humanidade? Caso aceite eu terei o 
prazer de lhe oferecer um de meus itens mágicos, err... Qual o seu nome mesmo??\n
\n==>Os itens que a fada disponibilizou são uma espada e um tomo, digite:
     ''')

heroi = profissao() 
mob = random_mob() # Utilizamos para facilitar de chamar essas classes posteriormente.

def batalha(): 
    ''' 
    Aqui é definido é definido como a batalha irá ocorrer. Essa função lê o comando que o usuário deu na batalha e o executa, 
    após executar o comando do usuário é o turno do do mob. Caso o mob morra a sua experiência é adicionada à experiência do herói
    e então é chamada a função Subir_nivel(). Caso a vida do herói seja menor ou igual a zero a função imprime uma mensagem.
    '''
    while heroi.saude > 0 and mob.saude > 0:
        for comando_2, action in heroi.Comandos.items(): 
            ''' 
            lê o dicionário Comandos e atribui as variaveis comandos_2 e action seus valores respectivos.
            '''
            print('Pressione {} para {}'.format(comando_2, action[0])) 
        comando_2 = input(">")
        while comando_2 not in heroi.Comandos and comando_2 != 'status':
            print("Comando não válido, digite novamente!")
            comando_2 = input(">")
            
        if heroi.saude > 0: 
            if comando_2 == 'l':
                Ataque.jogador() #aplica ataque do jogador
                if mob.saude > 0:
                    Ataque.mob() #aplica ataque do monstro
            elif comando_2  == 'm':
                heroi.missil_magico() #aplica magia do jogador
                if mob.saude > 0:
                    Ataque.mob() #aplica ataque do monstro
            elif comando_2 == 'b':
                heroi.bankai() #aplica habilidade do jogador
                if mob.saude > 0:
                    Ataque.mob() #aplica ataque do monstro
            elif comando_2 =='f':
                heroi.bola_de_fogo() #aplica magia do jogador
                if mob.saude > 0:
                    Ataque.mob() #aplica ataque do monstro
            elif comando_2 =='status':
                Options.status() #mostra os status do jogador
            else:
                heroi.gerar_mana() #aumento de mana
                Ataque.mob() #aplica ataque do monstro
            
            
    if heroi.saude <= 0:
        print(heroi.nome,'morreu!')
    else: 
        if heroi.prof == "mago": # atualiza o nivel, e se upar mostra Vida, Mana e Xp
            print('O',mob.nome,'morreu!')        
            heroi.exp += mob.exp #ganho de xp para subir de nivel
            print("\nVida {0}/{1}\nMana {2}/{3}\nXP {4}".format(heroi.saude,heroi.max_saude,heroi.mana,heroi.max_mana,heroi.exp))
            Subir_nivel()
        else:
            print('O',mob.nome,'morreu!') # Atualiza o nivel e se upar mostra Vida e Xp       
            heroi.exp += mob.exp #ganho de xp para subir de nivel
            print("\nVida {0}/{1}\nXP {2}".format(heroi.saude,heroi.max_saude,heroi.exp))
            Subir_nivel()

if heroi.prof == "mago": 
    print("\nNome: {0}, Vida: {1}, Mana: {2}, XP: {3}\n".format(heroi.nome, heroi.saude,heroi.mana,heroi.exp))
else:
    print("\nNome: {0}, Vida: {1}, XP: {2}\n".format(heroi.nome, heroi.saude,heroi.exp))
print("Digite ajuda para ver os comandos: ")

count = 0 
while heroi.saude > 0 and heroi.nivel < 14:
    ''' 
    Aqui é onde o programa chama as funções/classes. Até agora nós definimos como o jogo deve ocorrer, aqui é onde o usuário 
    decide qual função da opções vai ser chamada para o jogo poder seguir.
    '''
    acao = input("\nDigite a sua ação: ")
    mob = random_mob()
    resultado = count%3  # limpa a tela de comando conforme certas ações sao executadas
    count += 0.5
    if resultado == 1:
        os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela
    if acao == 'explorar':
        Options.explorar()
        count += 1
    elif acao == 'descansar':
        Options.descansar()
        count += 0.5
    elif acao == 'ajuda':
        Options.ajuda()
    elif acao == 'status':
        Options.status()
    elif acao == 'super_mode':
        Options.super_mode()
    elif acao == 'ganhar_xp':
        Options.ganhar_xp()
    elif acao == 'habilidades':
        Options.habilidades()
    elif acao == 'sair':
        Options.sair()
    else:
        print("Ação inválida")

if heroi.saude <= 0:
    print("Rest in peace\n") #jogador morreu
    escolha = input("Deseja continuar?\nSim ou Não: ") # Pede se o jogador quer continuar ou não, se sim volta para o jogo.
    while escolha != "sim" and escolha != "não":
        print("Comando inválido") # Repete ate validar o comando
        escolha = input("Digite um comando válido: ")
    while escolha == "sim":
        os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela
        heroi = profissao()
        mob = random_mob()

        if heroi.prof == "mago":
            heroi.mana = heroi.max_mana
            print("\nNome:{0}, HP:{1}, Mana:{2} XP:{3}\n".format(heroi.nome, heroi.saude,heroi.mana,heroi.exp))
        else:
            print("\nNome:{0}, HP:{1},XP:{2}\n".format(heroi.nome, heroi.saude,heroi.exp))
        print("Digite ajuda para ver os comandos")

        while heroi.saude > 0 and heroi.nivel < 14: # Mesmo código que o de cima
            acao = input("Digite a sua ação: ")
            mob = random_mob()
            resultado = count%3
            count += 0.5
            if resultado == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
            if acao == 'explorar':
                Options.explorar()
                count += 1
            elif acao == 'descansar':
                Options.descansar()
                count += 0.5
            elif acao == 'ajuda':
                Options.ajuda()
            elif acao == 'status':
                Options.status()
            elif acao == 'super_mode':
                Options.super_mode()
            elif acao == 'ganhar_xp':
                Options.ganhar_xp()
            elif acao == 'habilidades':
                Options.habilidades()
            else:
                print("Ação inválida")
    if heroi.nivel == 14:
                print('''
        Parabéns! Você salvou a humanidade por mais 1000 anos, agora todos reconhecem {0} como um grande herói e seu nome será lembrado para sempre como
        um dos grandes campeões a derrotar o poderoso Pikachu. Essa história teve um final feliz, esperamos que nas próximas reencarnações de Pikachu
        ajam heróis tão destemidos quanto você para proteger a humanidade, pois estando preparados ou não,  Pikachu continuará com seu insaciável desejo por
        sangue...
        '''.format(heroi.nome))
    else:
        escolha = input("Deseja continuar?\n Sim ou Não")
            


else:
    print('''
        Parabéns! Você salvou a humanidade por mais 1000 anos, agora todos reconhecem {0} como um grande herói e seu nome será lembrado para sempre como
        um dos grandes campeões a derrotar o poderoso Pikachu. Essa história teve um final feliz, esperamos que nas próximas reencarnações de Pikachu
        ajam heróis tão destemidos quanto você para proteger a humanidade, pois estando preparados ou não,  Pikachu continuará com seu insaciável desejo por
        sangue...
        '''.format(heroi.nome))