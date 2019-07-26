#vetores que serão usados como banco de dados.Servirão para saber o preço da pizza
sabortradicional = ['3 queijos','4 queijos','alemã','alho E óleo','banana com canela','mussarela','banana','açúcar e canela','bacon','bacon com catupiry','bahiana','brócolis','brócolis com bacon','calabresa',
'calabresa com catupiry','calabresa com cebola','carbonara','cowboy','crocante','escarola','escarola com bacon','fran-palha','frango com catupiry','hamburguesa','lombinho','marguerita','mexicana','milho e bacon',
'milho verde','Mussarela','napolitana','palmito','parmegiana','paulista','presunto','provolone','portuguesa','romana','romeu e julieta','toscana','3 queijos com alho']

saboresborda = ['catupiry','cheddar','calabresa','chocolate preto','chocolate branco','doce de leite','goiabada']

saborpromocionalnobredoce = ['á moda da casa', 'americana','atum','brasileira','brócolis com catupiry','brócolis com tomates secos','caipira','canadense','caprichosa','cinco queijos','du chef','escarola especial','escarola com catupiry',
'espanhola','francesa','frango crocante','frango especial','gorgonzola com champignon','italiana','jabá', 'livorno','lombo com catupiry','lombo com champignon','mineira','primata','quatro estações','romanesca',
'6 queiijos','siciliana','strogonoff vegetariano, strogonoff de carne','tex-mex','texana','vegetariana','carne seca','carne seca ao alho e óleo','champeroni','decamerone','mignon','pepperoni','tomate seco com rúcula'
'chocolate','banana com chocolate','beijinho','beijinho','brigadero','califórnia','charge','cocada','chocolate mesclado','confetti','dois amores','havaiana','lombo califórnia','nutella','prestígio',
'sedução']

#Vetores que serviram como forma de cardápio
cardapio = ['SABORES TRADICIONAIS(R$19,90):','3 queijos','4 queijos','alemã','alho E óleo','banana com canela','mussarela','banana','açúcar e canela','bacon','bacon com catupiry','bahiana','brócolis','brócolis com bacon','calabresa',
'calabresa com catupiry','calabresa com cebola','carbonara','cowboy','crocante','escarola','escarola com bacon','fran-palha','frango com catupiry','hamburguesa','lombinho','marguerita','mexicana','milho e bacon',
'milho verde','Mussarela','napolitana','palmito','parmegiana','paulista','presunto','provolone','portuguesa','romana','romeu e julieta','toscana','3 queijos com alho','SABORES ESPECIAIS (R$24,90):','á moda da casa',
'americana','atum','brasileira','brócolis com catupiry','brócolis com tomates secos','caipira','canadense','caprichosa','cinco queijos','du chef','escarola especial','escarola com catupiry',
'espanhola','francesa','frango crocante','frango especial','gorgonzola com champignon','italiana','jabá', 'livorno','lombo com catupiry','lombo com champignon','mineira','primata','quatro estações','romanesca',
'6 queiijos','siciliana','strogonoff vegetariano, strogonoff de carne','tex-mex','texana','vegetariana','SABORES NOBRES (R$24,90):','carne seca','carne seca ao alho e óleo','champeroni','decamerone','mignon','pepperoni','tomate seco com rúcula',
'SABORES DOCES (R$24,90):','chocolate','banana com chocolate','beijinho','beijinho','brigadero','califórnia','charge','cocada','chocolate mesclado','confetti','dois amores','havaiana','lombo califórnia','nutella','prestígio',
'sedução']
cardapioborda = ['SABORES BORDA:','BIG E GRANDE (R$9,90)','MEDIA E PEQUENA (R$6,90)','catupiry','cheddar','calabresa','chocolate preto','chocolate branco','doce de leite','goiabada']

tamanhos = ['big','grande','media','pequena']

print("----------------Bem vindo ao sistema de pedidos COMA PIZZA-------------------")

ordem = input('Gostaria de pedir uma pizza? ')
valorpizza = valorentrega = quantidadedepizza=0.0 #valores que servirão para o valor final e a quantidade de pizzas
 

if ordem == 'não':
    print('Pedido cancelado')

if ordem != 'não':
    while ordem == 'sim':
        tamanho = input('Qual o tamanho? ')
        while not tamanho in tamanhos:
            print('Não temos esse tamanho, escolha big, grande, media ou pequena!')
            tamanho=input('Qual o tamanho? ')
    
            #Usa a string dada pela variavel tamanho para saber qual o valor a mais na pizza
        if tamanho == 'pequena':
                valorpizza = valorpizza + 0.0
        if tamanho == 'media':
                valorpizza = valorpizza + 5.0
        if tamanho == 'grande':
                valorpizza = valorpizza + 10.0
        if tamanho == 'big':
                valorpizza = valorpizza + 25.0
    


        #Usa o vetor cardápio para mostrar o preço e os seus respectivos sabores
        confirmação = input('Gostaria de ver o cardápio? ')
        if confirmação == 'sim':
            for i in range(0,len(cardapio)):
                print(cardapio[i])
           
        quantidade = int(input("Quantos sabores? "))
        #A variável quantidade dará a quantidade de sabores que irá na pizza
        while quantidade <= 0 or quantidade >= 5:
            print('Não fazemos essa quantidade de sabores!')
            quantidade = int(input("Quantos Sabores? "))          

        if quantidade == 1:
            sabor1 = input("Escolha o primeiro sabor? ")
            
            #Serve para verificar se o nome dado existe no cardápio
            while sabor1 not in sabortradicional and sabor1 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor1 = input("Escolha o primeiro sabor? ")
            
            #Caso exista  á função abaixo verificara o valor a mais que no valor final    
            if sabor1 in saborpromocionalnobredoce:
                valorpizza = valorpizza + 24.90


            if sabor1 in sabortradicional:
                valorpizza = valorpizza + 19.90

            sabor2 = 'nda'
            sabor3 = 'nda'
            sabor4 = 'nda'

        if quantidade == 2:
            
            sabor1 = input("Escolha o primeiro sabor? ")
            
            
            while sabor1 not in sabortradicional and sabor1 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor1 = input("Escolha o primeiro sabor? ")
        
            sabor2 = input("Escolha o segundo sabor? ")
            while sabor2 not in sabortradicional and sabor2 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor2 = input("Escolha o segundo sabor? ")

            if sabor1 in saborpromocionalnobredoce or sabor2 in saborpromocionalnobredoce:
                valorpizza = valorpizza + 24.90


            if sabor1 in sabortradicional and sabor2 in sabortradicional:
               valorpizza = valorpizza + 19.90

            sabor3 = 'nda'
            sabor4 = 'nda'
                         
        if quantidade == 3:

            sabor1 = input("Escolha o primeiro sabor? ")
            while sabor1 not in sabortradicional and sabor1 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor1 = input("Escolha o primeiro sabor? ")

            sabor2 = input("Escolha o segundo sabor? ")
            while sabor2 not in sabortradicional and sabor2 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor2 = input("Escolha o segundo sabor? ")

            sabor3 = input("Escolha o terceiro sabor? ")
            while sabor3 not in sabortradicional and sabor3 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor3 = input("Escolha o terceiro sabor? ")
                
            if sabor1 in saborpromocionalnobredoce or sabor2 in saborpromocionalnobredoce or sabor3 in saborpromocionalnobredoce:
                valorpizza = valorpizza + 24.90


            if sabor1 in sabortradicional and sabor2 in sabortradicional and sabor3 in sabortradicional:
                valorpizza = valorpizza + 19.90

            sabor4 = 'nda'

        if quantidade== 4:

            sabor1 = input("Escolha o primeiro sabor? ")
            while sabor1 not in sabortradicional and sabor1 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor1 = input("Escolha o primeiro sabor? ")

            sabor2 = input("Escolha o segundo sabor? ")
            while sabor2 not in sabortradicional and sabor2 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor2 = input("Escolha o segundo sabor? ")

            sabor3 = input("Escolha o terceiro sabor? ")
            while sabor3 not in sabortradicional and  sabor3 not in saborpromocionalnobredoce:
                print("Não temos esse sabor")
                sabor3 = input("Escolha o terceiro sabor? ")

            sabor4 = input("Escolha o quarto sabor? ")
            while sabor4 not in sabortradicional and sabor4 not in saborpromocionalnobredoce:
                print("Não temos esse sabor!")
                sabor4 = input("Escolha o quarto sabor? ")

            if sabor1 in saborpromocionalnobredoce or sabor2 in saborpromocionalnobredoce or sabor3 in saborpromocionalnobredoce or sabor4 in saborpromocionalnobredoce:
                valorpizza = valorpizza + 24.90

            if sabor1 in sabortradicional and sabor2 in sabortradicional and sabor3 in sabortradicional and sabor4 in sabortradicional:
                valorpizza = valorpizza + 19.90

        borda=input("Recheio na borda? (Se quiser ver o cardápio digite cardapio): ")
        
        #Servirá de maneira parecida com o cardapio anterior
        if borda == "cardapio":
            for i in range(0,len(cardapioborda)):
                print(cardapioborda[i])
            borda=input('Recheio na borda?')

        if borda !='sim':
           borda=='sem borda'
        
        saborborda = 'nda' 

        if borda == "sim":
            saborborda=input("Qual sabor? ")
            while not saborborda in saboresborda:
                print("Não temos esse sabor!")
                saborborda=input("Qual sabor? ")
            if saborborda in saboresborda:
                if tamanho == "pequena" or tamanho == "media":#Verifica o tamanho da pizza pois os valores da borda diferem dependendo do tamanho 
                    valorpizza += 6.90

                if tamanho == "grande" or tamanho == "big": 
                    valorpizza += 9.90

        observação = input('Observação:')

        quantidadedepizza += 1 #Serve para contar a quantidade de pizzas que terá no final do pedido

        #Mostrará ao usurario a pizza que ele pediu
        print('Pizza', tamanho ,':')
        print('Sabor 1:', sabor1)
        print('Sabor 2:', sabor2)
        print('Sabor 3:', sabor3)
        print('Sabor 4:', sabor4)
        print('Borda:', saborborda )
        print(observação)

        ordem=input('Gostaria de mais uma pizza? ')

        




    #Verifica se haverá a necessidade de adicionar a taxa de entrega
    entrega = input('Para balcão, entrega ou retira? ')
    while not entrega == 'balcão' and not entrega == 'retira' and not entrega == 'entrega':
        print('Não temos essa opção!Escolha balcão,entrega ou retira')
        entrega = input('Para entrega? ')

    if entrega == 'balcão' and entrega == 'retira':
        valorentrega = 0 
    if entrega == 'entrega':
        valorentrega += 5.0

    #Mostrara os valores totais do pedido e a quantidade de pizzas 
    valortotal = valorpizza + valorentrega
    print(int(quantidadedepizza) ,'pizza(s)')
    print('Pizza: R$',valorpizza)
    print('Taxa de entrega: R$',valorentrega)
    print('valor total: R$',valortotal)

    #Colocamos essa pergunta por um problema no python onde fechava o progama sem mostrar os dados.
    efetuar = input('Deseja efetuar a compra? ')
    if efetuar == 'sim':
        print('Obrigado pelo pedido!')

    if efetuar == 'não':
        print('Pedido cancelado')
