from os import listdir, path
from os.path import isfile, join
from random import randint
import difflib
from PIL import Image
import ast
import shutil
from kivy.app import App
from kivy.uix.screenmanager import Screen


# le as informacoes dos elementos da interface do arquivo .kv
class janelaPrincipal(Screen):

    pass


def self(args):  # usado em outras funcoes

    pass


class janela(App):  # classe aonde sao executadas todas as funcoes da interface

    # le quantos arquivos possui a pasta "data/" e junta "data/"ao nome deles, para elespoderem ser acessados corretamente por outras funcoes
    configs = [f for f in listdir("data/") if isfile(join("data/", f))]

    # seleciona aleatoriamente um arquivo de configuracao
    peca = configs[randint(0, len(configs)-1)]

    def build(self):  # constroi os elementos da janela segundo as configuracoes do arquivo .kv

        return janelaPrincipal()

    def randselec(self):  # escolhe aleatoriamente uma imagem e os pontos dela

        # escolhe um arquivo aleatoriamente
        x = self.configs[randint(0, (len(self.configs)-1))]

        abrir = open("data/"+x)  # abre o arquivo escolhido

        # transforma o arquivo em uma lista em que cada linha e um item
        linha = abrir.readlines()

        # seleciona a terceira linha, aonde esta o endereco da imagem
        imagempeca = linha[2]

        imagempeca = imagempeca[7:]  # remove o identificador da linha

        imagempeca = imagempeca[:-1]  # remove o indicador de nova linha

        pontos = linha[5:]  # seleciona os pontos

        pontos = pontos[randint(0, (len(pontos)-1))]  # pega um ponto aleatorio

        # converte cada item dentro do pontos para os seus valores de integrais e strings
        pontos = ast.literal_eval(pontos)

        img = Image.open(imagempeca)  # abre a imagem selecionada

        seta = Image.open("data/images/arrow.png")  # abre a imagem da seta

        # cola a seta nas coordenadas indicadas pelo ponto
        img.paste(seta, pontos[:2], seta)

        img.save("data/cache/output.png")  # salva a imagem

        nome = pontos[2]  # pega o nome do ponto

        # abre o arquivo temporario do nome
        nomecache = open("data/cache/nomecache.txt", "wb")

        # salva o nome do ponto para um arquivo temporario
        nomecache.write(nome.encode('utf-8', 'ignore'))

        nomecache.close()  # fecha o arquivo

    def asd(self):
        print(self.ptn)

    def resp(self, text):  # compara o imput do usuario com o gabarito e altera a sua pontuacao

        # abre o arquivo de pontuacao
        score = open("data/cache/score.txt", "r")

        pontuacao = score.readlines()  # separa as linhas do arquivo

        pontuacao = float(pontuacao[0])  # seleciona a primeira linha

        score.close()  # fecha o arquivo de pontuacao

        # abre o arquivo com o nome do ponto
        nome = open('data/cache/nomecache.txt')

        nomecache = nome.readline()  # le o arquivo do nome

        nome.close()  # fecha o arquivo do nome

        # faz a comparacao entre o input do usuario e o nome do ponto
        comparacao = difflib.SequenceMatcher(None, text, nomecache).ratio()

        if comparacao == 1:  # se eles forem identicos

            pontuacao = pontuacao+1.0  # aumenta a pontuacao

            pontuacao = str(pontuacao)  # converte a pontuacao em string

            # abre o arquivo de pontuacao
            f = open("data/cache/score.txt", "wb")

            # escreve a nova pontuacao
            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()  # fecha o arquivo

        elif comparacao >= 0.75 and comparacao < 1:  # se o input do usuario nao for exato

            pontuacao = pontuacao + 0.8  # atribui um valor parcial

            pontuacao = str(pontuacao)

            f = open("data/cache/score.txt", "wb")

            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()

        elif comparacao >= 0.6 and comparacao < 0.75:

            pontuacao = pontuacao + 0.6

            pontuacao = str(pontuacao)

            f = open("data/cache/score.txt", "wb")

            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()

        else:  # se o input for muito diferente

            pontuacao = pontuacao + 0.0  # nao aumenta a pontuacao

            pontuacao = str(pontuacao)

            f = open("data/cache/score.txt", "wb")

            f.write(pontuacao.encode('utf-8', 'ignore'))

            f.close()

        log = "\nResposta: " + text + " / gabarito: " + nomecache + " / pontuacao: " + \
            str(pontuacao)  # cria uma string comparando o imput com o gabarito e a pontuacao atual

        # abre o arquivo de log temporario da sessao
        hist = open("data/cache/historico.txt", "ab+")

        # escreve a string de log no arquivo
        hist.write(log.encode('utf-8', 'ignore'))

        hist.close()  # fecha o arquivo

    def pontuacao(self):  # funcao para mostrar a pontuacao na tela

        ptn = open("data/cache/score.txt", "r")  # abre o arquivo de pontuacao

        self.pontuacao = ptn.readlines()  # le a pontuacao escrita nele

        self.pontuacao = self.pontuacao[0]  # seleciona a linha

        return self.pontuacao  # devolve o valor da linha

    # disponibiliza o valor da pontuacao para dentro da classe
    ptn = pontuacao(self)

    def resetar(self):  # cria um log da ultima secao e descarta os arquivos temporarios

        # le o endereco absoluto do arquivo
        his = path.realpath("data/cache/historico.txt")

        log = his+".log"  # coloca a extensao .log ao arquivo

        shutil.copy(his, log)  # cria um arquivo de log definitivo

        # limpa o arquivo historico
        open("data/cache/historico.txt", "w").close()

        reset = open("data/cache/score.txt", "w")  # abre o arquivo score

        reset.write('0.0')  # reseta o arquivo de score

        reset.close()  # fecha o arquivo


if __name__ == '__main__':

    janela().run()  # loop principal da interface grafica
