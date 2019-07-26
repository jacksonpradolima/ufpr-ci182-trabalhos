import math
import cv2
import numpy as np

#Inicializando as variáveis principais
fator = 0 #constante de conversão pixel -> mm (muda em cada imagem, pois depende da moeda de 0.25: referencial constante)
raio_medio = 0 #Soma dos raios das n laranjas medidos em mm
volume_medio = 0 #Soma dos volumes das n laranjas medidos em mL
n=0 #Total de laranjas analisadas

#Pedindo ao usuário o endereço da primeira imagem
address = input("Por favor, digite o endereco da imagem. Nao se esqueca da extensao nem de que o arquivo deve estar na mesma pasta que este programa: ")

#Verificar imagens até o usuário apertar Enter
while(address!=""):
    print() #Pula linha
    img = cv2.imread(address,0) #Guardando a imagem numa variável
    
    #Verificando se img guardou uma imagem com sucesso
    if isinstance(img,np.ndarray):
        
        #Redimensionar img de modo que a maior dimensão tenha 700 pixel. Assim, evita-se o uso de imagens muito grandes ou muito pequenas em HoughCircles(), o que poderia causar erros.
        height, width = img.shape[:2]
        escala=700/max(height,width)
        img = cv2.resize(img,(round(escala*width), round(escala*height)), interpolation = cv2.INTER_AREA)
        
        #Tratamento de img para uso em funções futuras. A saber, HoughCircles(), circle() e imshow()
        img = cv2.medianBlur(img,5)
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        
        #HoughCircles() procura por círculos em img e os guarda em circles. Parâmetros com Valores Padrão
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,
                                    param1=50,param2=60,minRadius=0,maxRadius=0)
        
        #Verificando se circles não está vazio, ou seja, se algum círculo foi encontrado
        if isinstance(circles,np.ndarray):
            #Verificando se alguma laranja foi encontrada além da moeda
            if len(circles[0])>1:
                
                #Procura-se pelo círculo de menor raio. Considera-se esse círculo como uma moeda de referência de 25 centavos e 25 mm de diâmetro.
                raio_ref = circles[0,0][0]
                for i in circles[0,:]:
                    if i[2]<raio_ref:
                        raio_ref=i[2]
                fator = 12.5/raio_ref #Uma vez que o raio da moeda é conhecido. Ela é usada para definir um fator de conversão pixel -> mm
                
                #Aqui avaliam-se os círculos. Mostra-se para o usuário os raios e volumes estimados de cada laranja individualmente e soma-se esses valores aos totais para uso futuro.
                #Também são desenhados em cimg os contornos e centros das circunferências das laranjas e da moeda.
                for i in circles[0,:]:
                    if i[2]==raio_ref:
                        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),2) #Desenha a circunferência da moeda
                        print("Moeda")
                        print('raio: {0:.2f} mm'.format(i[2]*fator))
                        print()
                    else:
                        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2) #Desenha a circunferência da laranja
                        n += 1
                        raio_medio += i[2]*fator
                        volume_medio += 4*math.pi*((i[2]*fator)**3)/3000
                        print("Laranja {0}".format(n))
                        print('raio: {0:.2f} mm'.format(i[2]*fator))
                        print('volume: {0:.2f} mL'.format(4*math.pi*((i[2]*fator)**3)/3000))
                        print()
                    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3) #Desenha o centro do círculo
                    
                #Informações resumidas de todas as n laranjas analisadas até o momento
                print("Raio Médio: {0:.2f} mm".format(raio_medio/n))
                print("Volume Médio: {0:.2f} mL".format(volume_medio/n))
                #Apenas para preservar a Gramática:
                if n==1:
                    print("Foi analisada 1 laranja")
                else:
                    print("Foram analisadas {0} laranjas".format(n))
                print() #Pula linha
                
                #Se o usuário desejar, cria uma janela exibindo a imagem original tratada com as laranjas e a moeda destacadas
                if input("Gostaria de verificar as laranjas encontradas na imagem?\n Se sim digite S, senão aperte Enter: ")=="S":
                    cv2.imshow('Aperte Enter para Voltar',cimg)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    
            else:print("Desculpe. Não encontrei nenhuma laranja. Tente outra imagem.") #Mensagem de Erro
        else:print("Desculpe. Não encontrei nenhuma laranja. Tente outra imagem.") #Mensagem de Erro
    else:print("Endereco nao encontrado. Tente novamente.") #Mensagem de Erro
    address = input("Por favor, digite o endereco da imagem. Nao se esqueca da extensao nem de que o arquivo deve estar na mesma pasta que este programa. Aperte Enter para Sair: ") #Continua o ciclo com uma nova imagem