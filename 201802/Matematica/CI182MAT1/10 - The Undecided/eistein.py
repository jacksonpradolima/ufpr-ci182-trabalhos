resultado = [['X            ','Casa 1','Casa 2','Casa 3','Casa 4','Casa 5'],['Cor          ','Amarela','Azul','Vermelha','Verde','Branca'],['Nacionalidade','Norueguês','Dinamarquês','Inglês','Alemão','Sueco'],['Bebida       ','Água','Chá','Leite','Café','Cerveja'],['Cigarro      ','Dunhill','Blends','Pall Mall','Prince','Bluemaster'],['Animal       ','Gatos','Cavalos','Pássaros','Peixes','Cachorro']]

jogo =[['X            ','Casa 1','Casa 2','Casa 3','Casa 4','Casa 5'],['Cor          ','//','//','//','//','//'],['Nacionalidade','//','//','//','//','//'],['Bebida       ','//','//','//','//','//'],['Cigarro      ','//','//','//','//','//'],['Animal       ','//','//','//','//','//']]
x = y = 0
print('''

Bem vindo ao jogo Teste de Einstein!


O jogo “Teste de Einstein” tem como objetivo exercitar as
capacidades dedutivas e racionais do jogador, tem esse nome devido
ao seu criador, o gênio Albert Einstein, que na época afirmou que
apenas 2% da população possui a capacidade para resolvê-lo. Será que você é capaz?



Regras:
Há 5 casas de diferentes cores.
Em cada casa mora uma pessoa de uma diferente nacionalidade.
Esses 5 proprietários bebem diferentes bebidas, fumam diferentes tipos de cigarros e têm um certo animal de estimação.
Nenhum deles têm o mesmo animal, fumam o mesmo cigarro ou bebem a mesma bebida.

ATENÇÃO: Digite as informações EXATAMENTE como o programa sugere!!!

''')

print(*jogo, sep="\n")




while jogo != resultado:

    print('''
Dicas:
O Norueguês vive na primeira casa.
O Inglês vive na casa Vermelha.
O Sueco tem Cachorros como animais de estimação.
O Dinamarquês bebe Chá.
A casa Verde fica do lado esquerdo da casa Branca.
O homem que vive na casa Verde bebe Café.
O homem que fuma Pall Mall cria Pássaros.
O homem que vive na casa Amarela fuma Dunhill.
O homem que vive na casa do meio bebe Leite.
O homem que fuma Blends vive ao lado do que tem Gatos.
O homem que cria Cavalos vive ao lado do que fuma Dunhill.
O homem que fuma BlueMaster bebe Cerveja.
O Alemão fuma Prince.
O Norueguês vive ao lado da casa Azul.
O homem que fuma Blends é vizinho do que bebe Água.


      ''')
    casa = input("Em qual casa você deseja inserir informações? ")
    while x==0:
        try:
            casa=int(casa)
            if 1 <= casa <= 5:
                x=1
            else:
                print("Valor inválido, tente novamente.")
                casa = input("Em qual casa você deseja inserir informações?")
        except:
            print("Valor inválido, tente novamente")   
            casa = input("Em qual casa você deseja inserir informações? ")    
    fileira = input("""
        1-Cor
        2-Nacionalidade
        3-Bebida
        4-Cigarro
        5-Animal
        Em qual categoria você deseja inserir informações? """)
    while y==0:
        try:
            fileira=int(fileira)
            if 1 <= fileira <= 5:
                y=1
            else:
                print("Valor inválido, tente novamente.")
                fileira = input("""
                    1-Cor
                    2-Nacionalidade
                    3-Bebida
                    4-Cigarro
                    5-Animal""")
        except:
            print("Valor inválido, tente novamente.")
            fileira = input("""
                1-Cor
                2-Nacionalidade
                3-Bebida
                4-Cigarro
                5-Animal""")

    if fileira == 1:
        variavel= input('''
        Cores disponiveis: Amarela,Azul,Vermelha,Verde,Branca. Qual você deseja inserir? ''')
    elif fileira == 2:
        variavel = input('''
        Nacionalidades disponíveis: Norueguês,Dinamarquês,Inglês,Alemão,Sueco. Qual você deseja inserir? ''')
    elif fileira == 3:
        variavel = input('''
        Bebidas disponíveis: Água,Chá,Leite,Café,Cerveja. Qual você deseja inserir? ''')
    elif fileira == 4:
        variavel = input('''
        Cigarros disponíveis: Dunhill,Blends,Pall Mall,Prince,Bluemaster. Qual você deseja inserir? ''')
    elif fileira == 5:
        variavel = input('''
        Animais disponíveis: Gatos,Cavalos,Pássaros,Peixes,Cachorro. Qual você deseja inserir? ''')
    jogo[fileira][casa] = variavel
    print(*jogo, sep="\n")
    x=y=0

print("Parabéns! Você concluiu o jogo!")



