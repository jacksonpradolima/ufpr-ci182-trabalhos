from os import listdir,path
from os.path import isfile, join
from random import randint
import difflib
from PIL import Image
import ast
import shutil
from kivy.app import App
from kivy.uix.screenmanager import Screen




class janelaPrincipal(Screen): #lê as informações dos elementos da interface do arquivo .kv

    pass


def self(args): #usado em outras funções

    pass


class janela(App): #classe aonde são executadas todas as funções da interface


    configs = [f for f in listdir("data/") if isfile(join("data/", f))] #lê quantos arquivos possui a pasta "data/" e junta "data/"ao nome deles, para elespoderem ser acessados corretamente por outras funções

    peca=configs[randint(0,len(configs)-1)] #seleciona aleatóriamente um arquivo de configuração


    def build(self): #constroi os elementos da janela segundo as configurações do arquivo .kv

        return janelaPrincipal()


    def randselec(self): # escolhe aleatoriamente uma imagem e os pontos dela

        x=self.configs[randint(0,(len(self.configs)-1))] # escolhe um arquivo aleatoriamente

        abrir =open("data/"+x) #abre o arquivo escolhido

        linha=abrir.readlines() #transforma o arquivo em uma lista em que cada linha é um item

        imagempeca=linha[2] # seleciona a terceira linha, aonde esta o endereco da imagem

        imagempeca=imagempeca[7:] # remove o identificador da linha

        imagempeca=imagempeca[:-1] #remove o indicador de nova linha

        pontos=linha[5:] #seleciona os pontos

        pontos=pontos[randint(0,(len(pontos)-1))] # pega um ponto aleatório

        pontos=ast.literal_eval(pontos)  # converte cada item dentro do pontos para os seus valores de integrais e strings

        img=Image.open(imagempeca) #abre a imagem selecionada

        seta=Image.open("data/images/arrow.png") #abre a imagem da seta

        img.paste(seta,pontos[:2],seta) #cola a seta nas coordenadas indicadas pelo ponto

        img.save("data/cache/output.png") #salva a imagem

        nome=pontos[2] # pega o nome do ponto

        nomecache=open("data/cache/nomecache.txt","wb") #abre o arquivo temporario do nome

        nomecache.write(nome.encode('utf-8','ignore')) #salva o nome do ponto para um arquivo temporario

        nomecache.close() #fecha o arquivo

    def asd(self):
        print(self.ptn)

    def resp(self, text): #compara o imput do usuario com o gabarito e altera a sua pontuação

        score = open("data/cache/score.txt", "r") #abre o arquivo de pontuação

        pontuacao = score.readlines() #separa as linhas do arquivo

        pontuacao = float(pontuacao[0]) #seleciona a primeira linha

        score.close() #fecha o arquivo de pontuação

        nome=open('data/cache/nomecache.txt') #abre o arquivo com o nome do ponto

        nomecache=nome.readline() #le o arquivo do nome

        nome.close()  #fecha o arquivo do nome


        comparacao=difflib.SequenceMatcher(None,text,nomecache).ratio() #faz a comparação entre o input do usuario e o nome do ponto


        if comparacao==1: #se eles forem identicos

            pontuacao=pontuacao+1.0 #aumenta a pontuação

            pontuacao=str(pontuacao) #converte a pontuação em string

            f=open("data/cache/score.txt","wb") #abre o arquivo de pontuação

            f.write(pontuacao.encode('utf-8','ignore')) #escreve a nova pontuação

            f.close() #fecha o arquivo

        elif comparacao >=0.75 and comparacao < 1: #se o input do usuario não for exato

            pontuacao = pontuacao + 0.8 #atribui um valor parcial

            pontuacao = str(pontuacao)

            f = open("data/cache/score.txt", "wb")

            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()

        elif comparacao >=0.6 and comparacao < 0.75:

            pontuacao = pontuacao + 0.6

            pontuacao = str(pontuacao)

            f = open("data/cache/score.txt", "wb")

            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()

        else: # se o input for muito diferente

            pontuacao = pontuacao + 0.7 #não aumenta a pontuação

            pontuacao = str(pontuacao)

            f = open("data/cache/score.txt", "wb")

            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()

        log = "\nResposta: " + text + " / gabarito: " + nomecache + " / pontuação: " + str(pontuacao) #cria uma string comparando o imput com o gabarito e a pontuação atual


        hist = open("data/cache/historico.txt", "ab+") #abre o arquivo de log temporario da sessão

        hist.write(log.encode('utf-8', 'ignore')) #escreve a string de log no arquivo

        hist.close() #fecha o arquivo

    def pontuacao(self): # função para mostrar a pontuação na tela


        ptn = open("data/cache/score.txt", "r") #abre o arquivo de pontuação

        self.pontuacao = ptn.readlines() #le a pontuação escrita nele

        self.pontuacao = self.pontuacao[0] #seleciona a linha

        return self.pontuacao #devolve o valor da linha

    ptn=pontuacao(self) #disponibiliza o valor da pontuação para dentro da classe


    def resetar(self): #cria um log da ultima seçao e descarta os arquivos temporarios


        his=path.realpath("data/cache/historico.txt") #lê o endereço absoluto do arquivo

        log=his+".log" #coloca a extensão .log ao arquivo

        shutil.copy(his,log) #cria um arquivo de log definitivo

        open("data/cache/historico.txt","w").close() #limpa o arquivo historico

        reset=open("data/cache/score.txt","w") #abre o arquivo score

        reset.write('0.0') #reseta o arquivo de score

        reset.close() #fecha o arquivo



janela().run() #loop principal da interface grafica