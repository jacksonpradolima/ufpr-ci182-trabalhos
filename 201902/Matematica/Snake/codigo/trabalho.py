import pickle
import numpy as np
from matplotlib import pyplot as plt
import random

training_data, testing_data = pickle.load(open('data.txt','rb'))
'''importa os dados que serão utilizados pelo programa; training_data
consiste de uma lista com 50000 entradas, onde cada entrada consiste de dois
elementos: uma lista com 748 numeros (a imagem) e um vetor representando
o output desejado (por exemplo, se a imagem consiste de um 5 então o output
desejado é (0 0 0 0 0 1 0 0 0 0) ); ja testing_data contém 10000 elementos,
cada elemento consiste de uma imagem(um array com 748 números) e o número ao
qual corresponde a imagem '''

def imprime(matriz):
    for i in range(len(matriz)):
        for l in range(len(matriz[0])):
            print (matriz[i][l], ' ', end='')
        print ('\t')

def imagem(x):
    #vai mostrar a imagem contida nos dados
    x = np.reshape(x,(28,28))
    plt.imshow(x, interpolation='nearest')
    plt.show()

def sigmoide(x):
    '''retorna a função sigmoide; obs: com o uso do numpy x pode ser uma liasta
    ou uma matriz '''
    return 1.0/(1.0+np.exp(-x))

def derivada_sigmoide(x):
    return sigmoide(x)*(1-sigmoide(x))

def random_neural(sizes):
    """cria uma rede neural baseada na lista sizes; por ex
    se sizes = [1,2,3], vai criar uma rede com 3 camadas e um neuronio na
    primeira camada, 2 na segunda e 3 na terceira """
    n = len(sizes)#número de camadas
    vieses = []
    for i in range(1,n):
        temp = np.random.randn(sizes[i],1)
        vieses.append(temp)
    pesos = []
    for i in range(len(sizes)-1):
        b = np.random.randn(sizes[i+1],sizes[i])
        pesos.append(b)
    net = [vieses, pesos]
    return net

def resultado(net, x):
    #x é o input que a rede neural net recebe e a função retorna o resultado
    for i in range(len(net[0])):
        x = sigmoide(np.dot(net[1][i],x)+net[0][i])
        ###np.dot(x,y) realiza a multiplicação de duas matrizes
    return x


def avaliacao (net, test_data):
    #olha quantas imagens a rede acertou
    i = 0
    for k in range(len(test_data)):
        r = resultado(net, test_data[k][0])
        r = np.argmax(r) #argmax traz a posicao com maior valor da lista
        if r == test_data[k][1]:
            i = i+1
    return i
            


def retropropagação(net, x, y):
    ''' Net é a rede sendo usada; x é a imagem usada de input na rede, e
    y é o output desejado'''
    nabla_b = [np.zeros(b.shape) for b in net[0]]
    nabla_w = [np.zeros(p.shape) for p in net[1]]
    activation = x
    activations = [x]
    zs = []
    for b, w in zip(net[0], net[1]):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoide(z)
            activations.append(activation)
    delta = (activations[-1] - y) * derivada_sigmoide(zs[-1])
    nabla_b[-1] = delta
    nabla_w[-1] = np.dot(delta, activations[-2].transpose())
    for l in range(2, len(net[0])+1):
            z = zs[-l]
            sp = derivada_sigmoide(z)
            delta = np.dot(net[1][-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
    return (nabla_b, nabla_w)
    
    

def update(net, mini_batch, eta):
    '''usa o mini_batch para calcular o gradiente aproximado, e então da um
    'passo' eta na direção do negativo do gradiente para otimizar a rede'''
    x = [np.zeros(b.shape) for b in net[0]]
    y = [np.zeros(p.shape) for p in net[1]]
    #cria matrizes no formato das matrizes de pesos e vieses mas com zeros de entradas
    for i in mini_batch:
        delta_x, delta_y = retropropagação(net, i[0], i[1])
        for l in range(len(x)):
            x[l] = x[l] + delta_x[l]
            y[l] = y[l] + delta_y[l]
    for i in range(len(net[0])):
        net[0][i] = net[0][i] - (eta/len(mini_batch))*x[i]
        net[1][i] = net[1][i] - (eta/len(mini_batch))*y[i]



    
def SGD(net, training_data, epocas, tamanho, eta, test_data):
    ''' SGD = stochastic gradient descent ou descida de gradiente estocástica.
    É a função que efetivamente vai treinar a rede. O training_data é os dados
    carregados no começo do programa, consistem de 50000 listas (x,y) onde x é a
    imagem e y é o output desejado; '''
    n = len(training_data)#vai ser 50000 no nosso caso
    for i in range(epocas):
        random.shuffle(training_data)#embaralha aleatoriamente os dados
        mini_batches = [training_data[k:k+tamanho] for k in range(0,n,tamanho)]
        for l in mini_batches:
            update(net, l, eta)
        print ('Epoca {0}: Acertos: {1} de {2}'.format(i, avaliacao(net, test_data), len(test_data)))





