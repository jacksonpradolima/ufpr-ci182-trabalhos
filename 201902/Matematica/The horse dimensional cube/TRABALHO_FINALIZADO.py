def mostra(v):
    #A função mostra foi criada com o intúito de melhorar a vizualisação de matrizes, quando se dá um print.
    #Ela escreve cada elemento da matriz em uma linha, e quebra a linha entre 2 linhas
    seq = ""
    for i in range(len(v)):
        for j in range(len(v[i])):
            seq += "{0}  ".format(v[i][j])
        if i < len(v) - 1:
                seq += " \n \n"
    print(seq)
def mostra_cubo(cubo):
    #Aqui a função mostra_cubo usa da função mostra para 'printar' o cubo em si.
    for i in cubo:
        mostra(cubo[i])
        print("\n \n")

#Aqui o vetor cubo é criado, tomando um dicionário para, invez de cada posição do vetor ser representada por um número, as posições serem nomeadas.
#Essa mudança de notação ajuda no entendimento geral do código.

cubo = {'Y': [],
        'B': [],
        'O': [],
        'G': [],
        'R': [],
        'W': []}
#Aqui o vetor cubo é preenchido com entradas que representam a posição resolvida do cubo.
for k,v in cubo.items():
    for i in range(3):
        v.append([])
        for j in range(3):
            v[i].append(k)

from tradução import traducao_IpG
from tradução import traducao_GpI


def turn(X, cubo):
    #Essa função rotaciona o cubo
    
    """As rotações serão nomeadas da seguinte maneira (em relação a notação usual):
    NOTAÇÃO P/ PROGRAMA    ###       NOTAÇÃO USUAL
    -    Y                 ###             U
    -    U                 ###             U'
    -    B                 ###             F
    -    N                 ###             F'
    -    O                 ###             L
    -    P                 ###             L'
    -    G                 ###             B
    -    H                 ###             B'
    -    R                 ###             R
    -    T                 ###             R'
    -    W                 ###             D
    -    E                 ###             D'               
    """
    #Rotações no sentido horário
    if X == "Y":
        #Rotaciona a face em si, nesse caso ele rotaciona a matriz Y em -90°
        cubo['Y'][0][2], cubo['Y'][1][2], cubo['Y'][2][2], cubo['Y'][0][1], cubo['Y'][2][1], cubo['Y'][0][0], cubo['Y'][1][0], cubo['Y'][2][0] = cubo['Y'][0][0], cubo['Y'][0][1], cubo['Y'][0][2], cubo['Y'][1][0], cubo['Y'][1][2], cubo['Y'][2][0], cubo['Y'][2][1], cubo['Y'][2][2] 
        #Troca linhas e colunas das faces adjacentes a face principal, completando o movimento usualmente chamado de "U"
        for i in range(3):
            cubo['O'][0][-i-1], cubo['G'][0][-i-1], cubo['R'][0][-i-1], cubo['B'][0][-i-1] = cubo['B'][0][-i-1], cubo['O'][0][-i-1], cubo['G'][0][-i-1], cubo['R'][0][-i-1]
    elif X == "B":
        cubo['B'][0][2], cubo['B'][1][2], cubo['B'][2][2], cubo['B'][0][1], cubo['B'][2][1], cubo['B'][0][0], cubo['B'][1][0], cubo['B'][2][0] = cubo['B'][0][0], cubo['B'][0][1], cubo['B'][0][2], cubo['B'][1][0], cubo['B'][1][2], cubo['B'][2][0], cubo['B'][2][1], cubo['B'][2][2]
        for i in range(3):
            cubo['O'][-i-1][2], cubo['Y'][2][i], cubo['R'][i][0], cubo['W'][0][-i-1] = cubo['W'][0][-i-1], cubo['O'][-i-1][2], cubo['Y'][2][i], cubo['R'][i][0]
    elif X == "O":
        cubo['O'][0][2], cubo['O'][1][2], cubo['O'][2][2], cubo['O'][0][1], cubo['O'][2][1], cubo['O'][0][0], cubo['O'][1][0], cubo['O'][2][0] = cubo['O'][0][0], cubo['O'][0][1], cubo['O'][0][2], cubo['O'][1][0], cubo['O'][1][2], cubo['O'][2][0], cubo['O'][2][1], cubo['O'][2][2]
        for i in range(3):
            cubo['B'][i][0], cubo['W'][i][0], cubo['G'][-i-1][2], cubo['Y'][i][0] = cubo['Y'][i][0], cubo['B'][i][0], cubo['W'][i][0], cubo['G'][-i-1][2]
    elif X == "G":
        cubo['G'][0][2], cubo['G'][1][2], cubo['G'][2][2], cubo['G'][0][1], cubo['G'][2][1], cubo['G'][0][0], cubo['G'][1][0], cubo['G'][2][0] = cubo['G'][0][0], cubo['G'][0][1], cubo['G'][0][2], cubo['G'][1][0], cubo['G'][1][2], cubo['G'][2][0], cubo['G'][2][1], cubo['G'][2][2]
        for i in range(3):
            cubo['O'][i][0], cubo['W'][2][i], cubo['R'][-i-1][2], cubo['Y'][0][-1-i] = cubo['Y'][0][-i-1], cubo['O'][i][0], cubo['W'][2][i], cubo['R'][-i-1][2]
    elif X == "R":
        cubo['R'][0][2], cubo['R'][1][2], cubo['R'][2][2], cubo['R'][0][1], cubo['R'][2][1], cubo['R'][0][0], cubo['R'][1][0], cubo['R'][2][0] = cubo['R'][0][0], cubo['R'][0][1], cubo['R'][0][2], cubo['R'][1][0], cubo['R'][1][2], cubo['R'][2][0], cubo['R'][2][1], cubo['R'][2][2]
        for i in range(3):
            cubo['Y'][-i-1][2], cubo['G'][i][0], cubo['W'][-i-1][2], cubo['B'][-i-1][2] = cubo['B'][-i-1][2], cubo['Y'][-i-1][2], cubo['G'][i][0], cubo['W'][-i-1][2]
    elif X == "W":
        cubo['W'][0][2], cubo['W'][1][2], cubo['W'][2][2], cubo['W'][0][1], cubo['W'][2][1], cubo['W'][0][0], cubo['W'][1][0], cubo['W'][2][0] = cubo['W'][0][0], cubo['W'][0][1], cubo['W'][0][2], cubo['W'][1][0], cubo['W'][1][2], cubo['W'][2][0], cubo['W'][2][1], cubo['W'][2][2]
        for i in range(3):
            cubo['B'][2][i], cubo['R'][2][i], cubo['G'][2][i], cubo['O'][2][i] = cubo['O'][2][i], cubo['B'][2][i], cubo['R'][2][i], cubo['G'][2][i]
    #Rotações no sentido anti-horário
    
    elif X == "U":
        cubo['Y'][2][0], cubo['Y'][1][0], cubo['Y'][0][0], cubo['Y'][2][1], cubo['Y'][0][1], cubo['Y'][2][2], cubo['Y'][1][2], cubo['Y'][0][2] = cubo['Y'][0][0], cubo['Y'][0][1], cubo['Y'][0][2], cubo['Y'][1][0], cubo['Y'][1][2], cubo['Y'][2][0], cubo['Y'][2][1], cubo['Y'][2][2] 
        for i in range(3):
            cubo['R'][0][i], cubo['G'][0][i], cubo['O'][0][i], cubo['B'][0][i] = cubo['B'][0][i], cubo['R'][0][i], cubo['G'][0][i], cubo['O'][0][i]
    elif X == "N":
        cubo['B'][2][0], cubo['B'][1][0], cubo['B'][0][0], cubo['B'][2][1], cubo['B'][0][1], cubo['B'][2][2], cubo['B'][1][2], cubo['B'][0][2] = cubo['B'][0][0], cubo['B'][0][1], cubo['B'][0][2], cubo['B'][1][0], cubo['B'][1][2], cubo['B'][2][0], cubo['B'][2][1], cubo['B'][2][2]
        for i in range(3):
            cubo['R'][-i-1][0], cubo['Y'][2][-i-1], cubo['O'][i][2], cubo['W'][0][i] = cubo['W'][0][i], cubo['R'][-i-1][0], cubo['Y'][2][-i-1], cubo['O'][i][2]
    elif X == "P":
        cubo['O'][2][0], cubo['O'][1][0], cubo['O'][0][0], cubo['O'][2][1], cubo['O'][0][1], cubo['O'][2][2], cubo['O'][1][2], cubo['O'][0][2] = cubo['O'][0][0], cubo['O'][0][1], cubo['O'][0][2], cubo['O'][1][0], cubo['O'][1][2], cubo['O'][2][0], cubo['O'][2][1], cubo['O'][2][2]
        for i in range(3):
            cubo['G'][i][2], cubo['W'][-i-1][0], cubo['B'][-i-1][0], cubo['Y'][-i-1][0] = cubo['Y'][-i-1][0], cubo['G'][i][2], cubo['W'][-i-1][0], cubo['B'][-i-1][0]
    elif X == "H":
        cubo['G'][2][0], cubo['G'][1][0], cubo['G'][0][0], cubo['G'][2][1], cubo['G'][0][1], cubo['G'][2][2], cubo['G'][1][2], cubo['G'][0][2] = cubo['G'][0][0], cubo['G'][0][1], cubo['G'][0][2], cubo['G'][1][0], cubo['G'][1][2], cubo['G'][2][0], cubo['G'][2][1], cubo['G'][2][2]
        for i in range(3):
            cubo['R'][i][2], cubo['W'][2][-i-1], cubo['O'][-i-1][0], cubo['Y'][0][i] = cubo['Y'][0][i], cubo['R'][i][2], cubo['W'][2][-i-1], cubo['O'][-i-1][0]
    elif X == "T":
        cubo['R'][2][0], cubo['R'][1][0], cubo['R'][0][0], cubo['R'][2][1], cubo['R'][0][1], cubo['R'][2][2], cubo['R'][1][2], cubo['R'][0][2] = cubo['R'][0][0], cubo['R'][0][1], cubo['R'][0][2], cubo['R'][1][0], cubo['R'][1][2], cubo['R'][2][0], cubo['R'][2][1], cubo['R'][2][2]
        for i in range(3):
            cubo['W'][i][2], cubo['G'][-i-1][0], cubo['Y'][i][2], cubo['B'][i][2] = cubo['B'][i][2], cubo['W'][i][2], cubo['G'][-i-1][0], cubo['Y'][i][2]
    elif X == "E":
        cubo['W'][2][0], cubo['W'][1][0], cubo['W'][0][0], cubo['W'][2][1], cubo['W'][0][1], cubo['W'][2][2], cubo['W'][1][2], cubo['W'][0][2] = cubo['W'][0][0], cubo['W'][0][1], cubo['W'][0][2], cubo['W'][1][0], cubo['W'][1][2], cubo['W'][2][0], cubo['W'][2][1], cubo['W'][2][2]
        for i in range(3):
            cubo['G'][2][-1-i], cubo['R'][2][-1-i], cubo['B'][2][-1-i], cubo['O'][2][-1-i] = cubo['O'][2][-1-i], cubo['G'][2][-1-i], cubo['R'][2][-1-i], cubo['B'][2][-1-i]

def alg(v, cubo):
    #Essa função pega uma string contendo movimentos, transforma ela num vetor e aplica as sucessivas rotações descritas nessa string
    v.split()
    for i in range(len(v)):
        turn(v[i], cubo)
    return cubo


class canto:
    #Classe das peças de canto, que carrega as informações das cores da peça em relação aos eixos.
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    #Define igualdade na classe como se os valores x, y e z são iguais, independente da ordem.
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z) or (self.x == other.x and self.y == other.z and self.z == other.y) or (self.x == other.y and self.y == other.x and self.z == other.z) or (self.x == other.y and self.y == other.z and self.z == other.x) or (self.x == other.z and self.y == other.y and self.z == other.x) or (self.x == other.z and self.y == other.x and self.z == other.y)
class meio:
    #Classe das peças de meio, que carrega as informações das cores numa orientação pré-definida (cor 1 sempre é a virada para a face branca ou amarela, e se a peça não tiver nessas faces, a cor 1 sempre é a virada pra face azul ou verde).
    def __init__(self, cor1, cor2):
        self.cor1 = cor1
        self.cor2 = cor2
    #Cria um método de comparar 2 elementos da classe meio, aqui se eles têm as mesmas cores, independentes da ordem, é definido que eles são iguais.
    def __eq__(self, other):
        return (self.cor1 == other.cor1 and self.cor2 == other.cor2) or (self.cor1 == other.cor2 and self.cor2 == other.cor1)

#Essa função traduz as 6 matrizes das faces para as classes de meio e canto.
#Ela é criada para facilitar o encontro de uma peça específica e o caminho ela deve tomar.

def trans_2p3(cubo):
    
    #Criação dos 8 cantos.
    
    C1 = canto(cubo["G"][0][2], cubo["O"][0][0], cubo["Y"][0][0])
    C2 = canto(cubo["G"][0][0], cubo["R"][0][2], cubo["Y"][0][2])
    C3 = canto(cubo["B"][0][0], cubo["O"][0][2], cubo["Y"][2][0])
    C4 = canto(cubo["B"][0][2], cubo["R"][0][0], cubo["Y"][2][2])
    C5 = canto(cubo["B"][2][0], cubo["O"][2][2], cubo["W"][0][0])
    C6 = canto(cubo["B"][2][2], cubo["R"][2][0], cubo["W"][0][2])
    C7 = canto(cubo["G"][2][2], cubo["O"][2][0], cubo["W"][2][0])
    C8 = canto(cubo["G"][2][0], cubo["R"][2][2], cubo["W"][2][2])
    
    #Criação dos 12 meios.
    
    M1 = meio(cubo["Y"][0][1], cubo["G"][0][1])
    M2 = meio(cubo["Y"][1][0], cubo["O"][0][1])
    M3 = meio(cubo["Y"][1][2], cubo["R"][0][1])
    M4 = meio(cubo["Y"][2][1], cubo["B"][0][1])
    M5 = meio(cubo["B"][1][0], cubo["O"][1][2])
    M6 = meio(cubo["B"][1][2], cubo["R"][1][0])
    M7 = meio(cubo["G"][1][0], cubo["R"][1][2])
    M8 = meio(cubo["G"][1][2], cubo["O"][1][0])
    M9 = meio(cubo["W"][0][1], cubo["B"][2][1])
    M10 = meio(cubo["W"][1][0], cubo["O"][2][1])
    M11 = meio(cubo["W"][1][2], cubo["R"][2][1])
    M12 = meio(cubo["W"][2][1], cubo["G"][2][1])

    return C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12

#Salva as posições de cada peça no cubo resolvido para futuras comparações
Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8, Mr1, Mr2, Mr3, Mr4, Mr5, Mr6, Mr7, Mr8, Mr9, Mr10, Mr11, Mr12 = trans_2p3(cubo)

def find(X, op, cubo):
    #op é a variavel que diz se a função procura nos meios ou nos cantos
    
    #Procura X nos cantos
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    if op == "C":
        if X == C1:
            return C1
        elif X == C2:
            return C2
        elif X == C3:
            return C3
        elif X == C4:
            return C4
        elif X == C5:
            return C5
        elif X == C6:
            return C6
        elif X == C7:
            return C7
        elif X == C8:
            return C8
    
    #Procura X nos 
    elif op == "M":
        if X == M1:
            return M1
        elif X == M2:
            return M2
        elif X == M3:
            return M3
        elif X == M4:
            return M4
        elif X == M5:
            return M5
        elif X == M6:
            return M6
        elif X == M7:
            return M7
        elif X == M8:
            return M8
        elif X == M9:
            return M9
        elif X == M10:
            return M10
        elif X == M11:
            return M11
        elif X == M12:
            return M12
        

def cruz(cubo):
    solve = ""
    #Resolve a cruz da face branca.
    
    #Arruma o meio M9.
    
    #Carrega no formato de cantos e meios o cubo embaralhado.
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    #Encontra nesses meios qual é igual ao meio 9 do cubo resolvido.
    OP = find(Mr9, "M", cubo)
    if OP == M1:
        #Aqui ele verifica a orientação da peça e, a partir disso, diz o caminho que ela deve percorrer.
        if OP.cor1 == "W":
            move = "YYBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "UONP"
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "W":
            move = "UBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "ONP"
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "W":
            move = "YBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "TBR"
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "W":
            move = "BB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "BWTE"
            solve += move
            alg(move, cubo)
    elif OP == M5:
        if OP.cor1 == "W":
            move = "EOW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "N"
            solve += move
            alg(move, cubo)
    elif OP == M6:
        if OP.cor1 == "W":
            move = "WTE"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "B"
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor1 == "W":
            move = "WRE"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "WWHEE"
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "W":
            move = "EPW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "WWGEE"
            solve += move
            alg(move, cubo)
    elif OP == M9:
        if OP.cor1 == "B":
            move = "BEOW"
            solve = solve + move
            alg(move, cubo)
    elif OP == M10:
        if OP.cor1 == "W":
            move = "OOUBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "PN"
            solve += move
            alg(move, cubo)
    elif OP == M11:
        if OP.cor1 == "W":
            move = "RRYBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "RB"
            solve += move
            alg(move, cubo)
    elif OP == M12:
        if OP.cor1 == "W":
            move = "GGYYBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "B":
            move = "HOUPBB"
            solve += move
            alg(move, cubo)
    
    #Arruma o meio M10
    
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Mr10,"M", cubo)
    if OP == M1:
        if OP.cor1 == "W":
            move = "UOO"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "GPH"
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "W":
            move = "OO"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "OWNE"
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "W":
            move = "UUOO"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "YNOB"
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "W":
            move = "YOO"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "NOB"
            solve += move
            alg(move, cubo)
    elif OP == M5:
        if OP.cor1 == "W":
            move = "O"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "WNE"
            solve += move
            alg(move, cubo)
    elif OP == M6:
        if OP.cor1 == "W":
            move = "WWTWW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "WBE"
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor1 == "W":
            move = "WWRWW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "EHW"
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "W":
            move = "P"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "EGW"
            solve += move
            alg(move, cubo)
    elif OP == M10:
        if OP.cor2 == "W":
            move = "PWNE"
            solve += move
            alg(move, cubo)
    elif OP == M11:
        if OP.cor1 == "W":
            move = "RRYYOO"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "RWBE"
            solve += move
            alg(move, cubo)
    elif OP == M12:
        if OP.cor1 == "W":
            move = "HEGW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "O":
            move = "HP"
            solve += move
            alg(move, cubo)
    
    #Arruma o meio M11
    
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Mr11, "M", cubo)
    if OP == M1:
        if OP.cor1 == "W":
            move = "YRR"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "HRG"
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "W":
            move = "YYRR"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "UBTN"
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "W":
            move = "RR"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "TEBW"
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "W":
            move = "URR"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "BTN"
            solve += move
            alg(move, cubo)
    elif OP == M5:
        if OP.cor1 == "W":
            move = "BBTBB"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "ENW"
            solve += move
            alg(move, cubo)
    elif OP == M6:
        if OP.cor1 == "W":
            move = "T"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "EBW"
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor1 == "W":
            move = "R"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "WHE"
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "W":
            move = "GGRGG"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "WGE"
            solve += move
            alg(move, cubo)
    elif OP == M11:
        if OP.cor1 == "R":
            move = "REBW"
            solve += move
            alg(move, cubo)
    elif OP == M12:
        if OP.cor1 == "W":
            move = "HEGW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "R":
            move = "GR"
            solve += move
            alg(move, cubo) 
            
    #Arruma o meio M12
    
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Mr12, "M", cubo)
    if OP == M1:
        if OP.cor1 == "W":
            move = "GG"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "HERW"
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "W":
            move = "YGG"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "PGO"
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "W":
            move = "UGG"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "RHT"
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "W":
            move = "UUGG"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "URHT"
            solve += move
            alg(move, cubo)
    elif OP == M5:
        if OP.cor1 == "W":
            move = "WOE"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "OOGOO"
            solve += move
            alg(move, cubo)
    elif OP == M6:
        if OP.cor1 == "W":
            move = "ETW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "RRHRR"
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor1 == "W":
            move = "ERW"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "H"
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "W":
            move = "WPE"
            solve += move
            alg(move, cubo)
        elif OP.cor1 == "G":
            move = "G"
            solve += move
            alg(move, cubo)
    elif OP == M12:
        if OP.cor1 == "G":
            move = "GERW"
            solve += move
            alg(move, cubo)
    #Aqui, é esperado que a cruz branca esteja resolvida.
    return solve

def cantos1(solve, cubo):
    #termina de resolver a face branca
    D = "RYT"
    E = "NUB"
    M = "RYYTU" + D 
 
    
    
    #Essa função auxilia a resolução. Ela troca 2 peças sob certas condições.
    #Ela coloca um canto que esteja na posição C4 e tenha uma cor branca na posição C6 com a cor branca virada para a face branca.
    
    def poe(X, solve, cubo):
        if X.x == "W":
            solve += E
            alg(E, cubo) 
            return E
        elif X.y == "W":
            solve += D
            alg(D, cubo)
            return D
        elif X.z == "W":
            solve += M
            alg(M, cubo)
            return M 
     
    #arruma o canto C5   
        
    #Recebe as informações do cubo
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    #Encontra onde está o canto igual ao canto 5 do cubo resolvido
    OP = find(Cr5, "C", cubo)
    if OP == C1:
        #O canto é levado para a posição C4 e o destino final dele é levado para a posição C6, e então é aplicada a função poe 
        move = "WYY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    elif OP == C2:
        move = "WY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    elif OP == C3:
        move = "WU"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    elif OP == C4:
        move = "W"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    elif OP == C5:
        if C5.x == "W":
            move = "WRYTU" + D + "E"
            solve += move
            alg(move, cubo)
        elif C5.y == "W":
            move = "WNUBY" + E + "E"
            solve += move
            alg(move, cubo)
    elif OP == C6:
        move = D + "UW"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    elif OP == C7:
        move = "WW" + D + "UE"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    elif OP == C8:
        move = "E" + D + "U" + "WW"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "E"
        solve += move
        alg(move, cubo)
    
    #Arruma o canto C6
    

    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Cr6, "C", cubo)
    if OP == C1:
        move = "YY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
    elif OP == C2:
        move = "Y"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
    elif OP == C3:
        move = "U"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
    elif OP == C4:
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += op1
    elif OP == C6:
        if OP.x == "W":
            move = "NUBY" + E
            solve += move
            alg(move, cubo)
        elif OP.y == "W":
            move = "RYTU" + D
            solve += move
            alg(move, cubo)
    elif OP == C7:
        move = "WW" + D + "U" + "WW"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
    elif OP == C8:
        move = "E" + D + "UW"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
    
    #arruma o canto C7
    
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Cr7, "C", cubo)
    if OP == C1:
        move = "WWYY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "EE"
        solve += move
        alg(move, cubo)
    elif OP == C2:
        move = "WWY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "EE"
        solve += move
        alg(move, cubo)
    elif OP == C3:
        move = "WWU"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "EE"
        solve += move
        alg(move, cubo)
    elif OP == C4:
        move = "WW"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        mobe = "EE"
        solve += move
        alg(move, cubo)
    elif OP == C7:
        if OP.x == "W":
            move = "EENUBY" + E + "EE"
            solve += move
            alg(move, cubo)
        elif OP.y == "W":
            move = "EERYTU" + D + "EE"
            solve += move
            alg(move, cubo)
    elif OP == C8:
        move = "E" + D + "U" + "E"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "WW"
        solve += move
        alg(move, cubo)
        
    #arruma o canto C8
    
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Cr8, "C", cubo)
    if OP == C1:
        move = "EYY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "W"
        solve += move
        alg(move, cubo)
    elif OP == C2:
        move = "EY"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "W"
        solve += move
        alg(move, cubo)
    elif OP == C3:
        move = "UE"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "W"
        solve += move
        alg(move, cubo)
    elif OP == C4:
        move = "E"
        alg(move, cubo)
        C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
        op1 = poe(C4, solve, cubo)
        solve += move + op1
        move = "W"
        solve += move
        alg(move, cubo)
    elif OP == C8:
        if OP.x == "W":
            move = "ERYTU" + D + "W"
            solve += move
            alg(move, cubo)
        elif OP.y == "W":
            move = "ENUBY" + E + "W"
            solve += move
            alg(move, cubo)
    
    return solve

def seg_cam(solve, cubo):
    #Termina de arrumar a segunda camada do cubo
    
    #Colocar o meio M5 no lugar
    
    #Carrega as informações do cubo
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    #Encontra ode o meio igual ao M5 do cubo resolvido está.
    OP = find(Mr5, "M", cubo)
    '''Para facilitar o entendimento dessa função, cada movimento é definido como:
    Um setup move que coloca a peça no lugar indicado e um ou + algoritmos q levam uma peça na face X 
    para o encontro de duas face yz.
    Por exemplo se eu escrevo G-ob, a peça vai da face verde para entre as faces laranja e azul'''
    if OP == M1:
        #Levando em conta a orientação, a peça é colocada no lugar
        if OP.cor1 == "B":
            move = "BUNONPB"
            #G-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "Y" + "PYONOBP"
            #R-ob
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "B":
            move = "Y" + "BUNONPB"
            #G-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "YY" + "PYONOBP"
            #R-ob
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "B":
            move = "U" + "BUNONPB"
            #G-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "PYONOBP"
            #R-ob
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "B":
            move = "UU" + "BUNONPB"
            #G-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "U" + "PYONOBP"
            #R-ob
            solve += move
            alg(move, cubo)
    elif OP == M5:
        if OP.cor2 == "B":
            move = "BUNYPYYOYPYYO"
            #ob-ob
            solve += move
            alg(move, cubo)
    elif OP == M6:
        if OP.cor1 == "B":
            move = "RUTBTNR" + "BUNONPB"
            #O-br / G-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "RUTBTNR" + "Y" + "PYONOBP"
            #O-br / R-ob
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor1 == "B":
            move = "GUHRHTG" + "YY" + "PYONOBP"
            #B-rg / R-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "GUHRHTG" + "Y" + "BUNONPB"
            #B-rg / G-ob
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "B":
            move = "OUPGPHO" + "YY" + "BUNONPB"
            #R-go / G-ob
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "OUPGPHO" + "U" + "PYONOBP"
            #R-go / R-ob
            solve += move
            alg(move, cubo)
            
            
    #Colocar o meio M6 no lugar
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Mr6, "M", cubo)
    if OP == M1:
        if OP.cor1 == "B":
            move = "NYBTBRN"
            #G-br
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "U" + "RUTBTNR"
            #O-br
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "B":
            move = "Y" + "NYBTBRN"
            #G-br
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "RUTBTNR"
            #O-br
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "B":
            move = "U" + "NYBTBRN"
            #G-br
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "YY" + "RUTBTNR"
            #O-br
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "B":
            move = "UU" + "NYBTBRN"
            #G-br
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "Y" + "RUTBTNR"
            #O_br
            solve += move
            alg(move, cubo)
    elif OP == M6:
        if OP.cor2 == "B":
            move = "RUTYNYYBYNYYB"
            #br-br
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor1 == "B":
            move = "GUHRHTG" + "RUTBTNR"
            #B-rg / O-br
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "GUHRHTG" + "Y" + "NYBTBRN"
            #B-rg / G-br
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "B":
            move = "OUPGPHO" + "YY" + "NYBTBRN"
            #R-go / G-br
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "B":
            move = "OUPGPHO" + "Y" + "RUTBTNR"
            #R-go / O-br
            solve += move
            alg(move, cubo)
    
    
    #Colocar o meio M7 no lugar
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Mr7, "M", cubo)
    if OP == M1:
        if OP.cor1 == "G":
            move = "UU" + "GUHRHTG"
            #B-rg
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "U" + "TYRHRGT"
            #O-rg
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "G":
            move = "U" + "GUHRHTG"
            #B-rg
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "TYRHRGT"
            #O-rg
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "G":
            move = "Y" + "GUHRHTG"
            #B-rg
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "YY" + "TYRHRGT"
            #O-rg
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "G":
            move = "GUHRHTG"
            #B-rg
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "Y" + "TYRHRGT"
            #O_rg
            solve += move
            alg(move, cubo)
    elif OP == M7:
        if OP.cor2 == "G":
            move = "GUHYTYYRYTYYR"
            #rg-rg
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor1 == "G":
            move = "OUPGPHO" + "GUHRHTG"
            #R-go / B-rg
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "OUPGPHO" + "Y" + "TYRHRGT"
            #R-go / O-rg
            solve += move
            alg(move, cubo)
    
        #Colocar o meio M8 no lugar
    C1, C2, C3, C4, C5, C6, C7, C8, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12 = trans_2p3(cubo)
    OP = find(Mr8, "M", cubo)
    if OP == M1:
        if OP.cor1 == "G":
            move = "YY" + "HYGPGOH"
            #B-go
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "Y" + "OUPGPHO"
            #R-go
            solve += move
            alg(move, cubo)
    elif OP == M2:
        if OP.cor1 == "G":
            move = "U" + "HYGPGOH"
            #B-go
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "YY" + "OUPGPHO"
            #R-go
            solve += move
            alg(move, cubo)
    elif OP == M3:
        if OP.cor1 == "G":
            move = "Y" + "HYGPGOH"
            #B-go
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "OUPGPHO"
            #R-go
            solve += move
            alg(move, cubo)
    elif OP == M4:
        if OP.cor1 == "G":
            move = "HYGPGOH"
            #B-go
            solve += move
            alg(move, cubo)
        elif OP.cor2 == "G":
            move = "U" + "OUPGPHO"
            #R-go
            solve += move
            alg(move, cubo)
    elif OP == M8:
        if OP.cor2 == "G":
            move = "OUPYHYYGYHYYG"
            #go-go
            solve += move
            alg(move, cubo)
            
            
    return solve

def cruz_amarela(solve, cubo):
    #Essa função orienta todos os meios da última camada
    #A partir daqui, as funções não usam mais as classes, mas as posições em sí.
    if cubo["Y"][0][1] == "Y":
        if cubo["Y"][1][0] == "Y" and cubo["Y"][2][1] != "Y":
            move = "BYRUTN"
            solve += move
            alg(move,cubo)
        elif cubo["Y"][1][2] == "Y" and cubo["Y"][1][0] != "Y":
            move = "OYBUNP"
            solve += move
            alg(move,cubo)
        elif cubo["Y"][2][1] == "Y" and cubo["Y"][1][0] != "Y":
            move = "OBYNUP"
            solve += move
            alg(move,cubo)
    elif cubo["Y"][1][0] == "Y":
        if cubo["Y"][1][2] == "Y" and cubo["Y"][2][1] != "Y":
            move = "BRYTUN"
            solve += move
            alg(move, cubo)
        elif cubo["Y"][2][1] == "Y" and cubo["Y"][1][2] != "Y":
            move = "RYGUHT"
            solve += move
            alg(move, cubo)
    elif cubo["Y"][1][2] == "Y":
        move = "GYOUPH"
        solve += move
        alg(move, cubo)
    elif cubo["Y"][2][1] != "Y":
        move = "BYRUTNYBRYTUN"
        solve += move
        alg(move, cubo)
    return solve
    
def oll_de_cruz(solve, cubo):
    #Deixa a face amarela toda amarela, orientada.
    
    """ Essa função funciona assim, no primeiro if, a função alg é aplicada, então toda a comparação
    se baseia no cubo após a função alg. Desse modo, se a posição estiver certa, é só aplicar o algoritmo.
    Pórem, esse movimento Y não foi computado na solve, então ele deve ser adicionado na solve, mas não aplicado novamente em alg."""
    #caso sune
    if (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["G"][0][2] == "Y") and (cubo["R"][0][2] == "Y") and (cubo["B"][0][2] == "Y"):
        move = "RYTYRYYT"
        solve += "Y" + move
        alg(move, cubo)
    """Os elif dessa função e da próxima são, dentro de cada caso, exatamente iguais, mas verificam coisas diferentes,
    pois ao começo de cada um é aplicada a função alg, mudando o cubo. Logo ela procura uma posição específica
    independente da orientação da última camada, i.e., cada elif de um mesmo caso A procura esse caso A em cada rotação
    da camada "Y", isto é, se a posição atual do cubo está a, no máximo, 2 movimentos na face amarela do caso A procurado """
    if (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["G"][0][2] == "Y") and (cubo["R"][0][2] == "Y") and (cubo["B"][0][2] == "Y"):
        move = "RYTYRYYT"
        solve += "UU" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["G"][0][2] == "Y") and (cubo["R"][0][2] == "Y") and (cubo["B"][0][2] == "Y"):
        move = "RYTYRYYT"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["G"][0][2] == "Y") and (cubo["R"][0][2] == "Y") and (cubo["B"][0][2] == "Y"):
        move = "RYTYRYYT"
        solve += move
        alg(move, cubo)
        
    #caso anti-sune
    elif (alg("Y",cubo)["Y"][0][2] == "Y") and (cubo["R"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RYYTURUT"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][0][2] == "Y") and (cubo["R"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RYYTURUT"
        solve += "UU" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][0][2] == "Y") and (cubo["R"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RYYTURUT"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][0][2] == "Y") and (cubo["R"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RYYTURUT"
        solve += move
        alg(move, cubo)
        
    #caso pi
    elif (alg("Y",cubo)["B"][0][2] == "Y") and (cubo["O"][0][2] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RUUTTURRUTTUUR"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["G"][0][0] == "Y") and (cubo["O"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RUUTTURRUTTUUR"
        solve += "UU" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["G"][0][0] == "Y") and (cubo["O"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RUUTTURRUTTUUR"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["G"][0][0] == "Y") and (cubo["O"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["O"][0][0] == "Y"):
        move = "RUUTTURRUTTUUR"
        solve += move
        alg(move, cubo)
    
    #caso H
    elif (alg("Y",cubo)["G"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["B"][0][0] == "Y"):
        move = "RUUTURYTURUT"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["G"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["B"][0][0] == "Y"):
        move = "RUUTURYTURUT"
        solve += "UU" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["G"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["B"][0][0] == "Y"):
        move = "RUUTURYTURUT"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["G"][0][2] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["B"][0][0] == "Y"):
        move = "RUUTURYTURUT"
        solve += move
        alg(move, cubo)
    
    #caso L
    elif (alg("Y",cubo)["O"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["Y"][2][2] == "Y"):
        move = "RUUTURYTURYTURUT"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["O"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["Y"][2][2] == "Y"):
        move = "RUUTURYTURYTURUT"
        solve += "UU" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["O"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["Y"][2][2] == "Y"):
        move = "RUUTURYTURYTURUT"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["O"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["G"][0][0] == "Y") and (cubo["Y"][2][2] == "Y"):
        move = "RUUTURYTURYTURUT"
        solve += move
        alg(move, cubo)
    
    #caso chato
    elif (alg("Y",cubo)["B"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["Y"][0][2] == "Y"):
        move = "RRWTYYRETYYT"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["B"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["Y"][0][2] == "Y"):
        move = "RRWTYYRETYYT"
        solve += "UU" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["B"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["Y"][0][2] == "Y"):
        move = "RRWTYYRETYYT"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["B"][0][2] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][0] == "Y") and (cubo["Y"][0][2] == "Y"):
        move = "RRWTYYRETYYT"
        solve += move
        alg(move, cubo)
    
    #caso T
    elif (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y"):
        move = "TNOBRNPB"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y"):
        move = "TNOBRNPB"
        solve += "YY" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y"):
        move = "TNOBRNPB"
        solve += "U" + move
        alg(move, cubo)
    elif (alg("Y",cubo)["Y"][2][0] == "Y") and (cubo["Y"][0][0] == "Y") and (cubo["B"][0][2] == "Y") and (cubo["G"][0][0] == "Y"):
        move = "TNOBRNPB"
        solve += move
        alg(move, cubo)
    
    return solve

def pll(solve, cubo):
    #Permuta a última camada, quase resolvendo o cubo

    """Essa função usa a mesma lógica da última função, porém com uma abordagem diferente para a comparação.
    Na função acima comparava-se posições específicas com a cor amarela.
    Aqui, compara 12 cores 3 a 3, para ver qual caso de permutar a última camada deve ser aplicado."""
    #caso Ua
    if ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 

        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["B"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RURYRYRUTURR"
        solve += "Y" + move
        alg(move, cubo)
    
    
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["B"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RURYRYRUTURR"
        solve += "YY" + move
        alg(move, cubo)
    
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["B"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RURYRYRUTURR"
        solve += "U" + move
        alg(move, cubo)
    
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["B"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RURYRYRUTURR"
        solve += move
        alg(move, cubo)
    
    #caso Ub
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["B"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RRYRYTUTUTYT"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["B"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RRYRYTUTUTYT"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y",cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["B"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RRYRYTUTUTYT"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["B"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RRYRYTUTUTYT"
        solve += move
        alg(move, cubo)
    
    #caso Z
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["B"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["O"][0][1] == cubo["G"][0][2])):
        move = "RYTYTUTYRUTURRYR"
        solve += "Y" + move
        alg(move, cubo)
    elif (alg("Y", cubo)["B"][0][0] == cubo["B"][0][2] and 
        cubo["R"][0][1] == cubo["B"][0][2] and 
        #arruma a parte laranja
        cubo["O"][0][0] == cubo["O"][0][2] and
        cubo["G"][0][1] == cubo["O"][0][2] and
        #arruma a parte vermelha
        cubo["R"][0][0] == cubo["R"][0][2] and
        cubo["B"][0][1] == cubo["R"][0][2] and
        #arruma a parte verde
        cubo["G"][0][0] == cubo["G"][0][2] and
        cubo["O"][0][1] == cubo["G"][0][2]):
        move = "RYTYTUTYRUTURRYR"
        solve += move
        alg(move, cubo)
    #para corrigir o 'erro'
    alg("YY", cubo)
    
    #caso H
    if ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["G"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["B"][0][1] == cubo["G"][0][2])):
        move = "ORYYPTNHUUBG"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["G"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        (cubo["B"][0][1] == cubo["G"][0][2])):
        move = "ORYYPTNHUUBG"
        solve += move
        alg(move, cubo)
    #para corrigir o 'erro'
    alg("YY", cubo)
    
    #caso Aa
    if ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][1]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["B"][0][2] == cubo["O"][0][0])):
        move = "TBTGGRNTGGRR"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][1]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["B"][0][2] == cubo["O"][0][0])):
        move = "TBTGGRNTGGRR"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][1]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["B"][0][2] == cubo["O"][0][0])):
        move = "TBTGGRNTGGRR"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][1]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["G"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["B"][0][2] == cubo["O"][0][0])):
        move = "TBTGGRNTGGRR"
        solve += move
        alg(move, cubo)
    
    #caso Ab
    elif ((alg("Y", cubo)["B"][0][1] == cubo["O"][0][2]) and 
        (cubo["G"][0][0] == cubo["O"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["R"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["B"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RHRBBTGRBBRR"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][1] == cubo["O"][0][2]) and 
        (cubo["G"][0][0] == cubo["O"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["R"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["B"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RHRBBTGRBBRR"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][1] == cubo["O"][0][2]) and 
        (cubo["G"][0][0] == cubo["O"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["R"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["B"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RHRBBTGRBBRR"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][1] == cubo["O"][0][2]) and 
        (cubo["G"][0][0] == cubo["O"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["R"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["B"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RHRBBTGRBBRR"
        solve += move
        alg(move, cubo)
    
    #caso E
    elif ((alg("Y", cubo)["B"][0][1] == cubo["R"][0][2]) and 
        (cubo["O"][0][0] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["B"][0][0]) and
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2])):
        move = "RHTBRGTNRGTBRHTN"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][1] == cubo["R"][0][2]) and 
        (cubo["O"][0][0] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["B"][0][0]) and
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2])):
        move = "RHTBRGTNRGTBRHTN"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][1] == cubo["R"][0][2]) and 
        (cubo["O"][0][0] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["B"][0][0]) and
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2])):
        move = "RHTBRGTNRGTBRHTN"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][1] == cubo["R"][0][2]) and 
        (cubo["O"][0][0] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["B"][0][0]) and
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["R"][0][0] == cubo["O"][0][2])):
        move = "RHTBRGTNRGTBRHTN"
        solve += move
        alg(move, cubo)
    
    #caso F
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TUNRYTUTBRRUTURYTYR"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TUNRYTUTBRRUTURYTYR"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TUNRYTUTBRRUTURYTYR"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TUNRYTUTBRRUTURYTYR"
        solve += move
        alg(move, cubo)
    
    #caso Ga
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["R"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RRYTYTURURRUWTYRE"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["R"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RRYTYTURURRUWTYRE"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["R"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RRYTYTURURRUWTYRE"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["R"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RRYTYTURURRUWTYRE"
        solve += move
        alg(move, cubo)
    
    #caso Gb
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TURYERRYTYRURURRW"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TURYERRYTYRURURRW"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TURYERRYTYRURURRW"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][1] == cubo["O"][0][0]) and
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "TURYERRYTYRURURRW"
        solve += move
        alg(move, cubo)
    
    #caso Gc
    elif ((alg("Y", cubo)["B"][0][2] == cubo["O"][0][0]) and 
        (cubo["G"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["G"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PPUOUOYPYPPUEOUPW"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][2] == cubo["O"][0][0]) and 
        (cubo["G"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["G"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PPUOUOYPYPPUEOUPW"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][2] == cubo["O"][0][0]) and 
        (cubo["G"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["G"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PPUOUOYPYPPUEOUPW"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][2] == cubo["O"][0][0]) and 
        (cubo["G"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        (cubo["G"][0][2] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PPUOUOYPYPPUEOUPW"
        solve += move
        alg(move, cubo)
    
    #caso Gd
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["B"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTUWRRURUTYTYRRE"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["B"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTUWRRURUTYTYRRE"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["B"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTUWRRURUTYTYRRE"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["G"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["B"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTUWRRURUTYTYRRE"
        solve += move
        alg(move, cubo)
    
    #caso Ja
    elif ((alg("Y", cubo)["O"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        (cubo["B"][0][1] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PUOBPUOYONPPYO"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["O"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        (cubo["B"][0][1] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PUOBPUOYONPPYO"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["O"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        (cubo["B"][0][1] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PUOBPUOYONPPYO"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["O"][0][0] == cubo["B"][0][2]) and 
        (cubo["O"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["G"][0][2] == cubo["B"][0][0]) and
        (cubo["B"][0][1] == cubo["B"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["R"][0][2]) and
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        (cubo["G"][0][0] == cubo["O"][0][2])):
        move = "PUOBPUOYONPPYO"
        solve += move
        alg(move, cubo)
    
    #caso Jb
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTNRYTUTBRRUT"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTNRYTUTBRRUT"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTNRYTUTBRRUT"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["R"][0][1] == cubo["R"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["O"][0][0]) and
        (cubo["O"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["B"][0][1] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2])):
        move = "RYTNRYTUTBRRUT"
        solve += move
        alg(move, cubo)
    
    #caso Na
    elif ((alg("Y", cubo)["G"][0][0] == cubo["B"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][2]) and 
        #arruma a parte laranja
        (cubo["R"][0][2] == cubo["O"][0][0]) and
        (cubo["R"][0][1] == cubo["O"][0][0]) and
        #arruma a parte vermelha
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["G"][0][2]) and
        (cubo["B"][0][0] == cubo["G"][0][2])):
        move = "RYTY" + "RYTNRYTUTBRRUT" + "UURUT"
        solve += move
        alg(move, cubo)
    #corrigidor de erros
    alg("U", cubo)
    
    #caso Nb
    if ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["G"][0][2]) and 
        #arruma a parte laranja
        (cubo["O"][0][2] == cubo["R"][0][0]) and
        (cubo["R"][0][1] == cubo["R"][0][0]) and
        #arruma a parte vermelha
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        (cubo["O"][0][1] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2])):
        move = "PUOU" + "PUOBPUOYONPPYO" + "YYPYO"
        solve += move
        alg(move, cubo)
    #corridor de erros
    alg("U", cubo)
    
    #caso Ra
    if ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["O"][0][1] == cubo["G"][0][2])):
        move = "RYTNRYYTUUTBRYRUUT"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["O"][0][1] == cubo["G"][0][2])):
        move = "RYTNRYYTUUTBRYRUUT"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["O"][0][1] == cubo["G"][0][2])):
        move = "RYTNRYYTUUTBRYRUUT"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][1]) and 
        (cubo["R"][0][2] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["O"][0][1] == cubo["G"][0][2])):
        move = "RYTNRYYTUUTBRYRUUT"
        solve += move
        alg(move, cubo)
    
    #caso Rb
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["G"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        (cubo["G"][0][1] == cubo["R"][0][2])):
        move = "TYYRUUTBRYTUTNRR"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["G"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        (cubo["G"][0][1] == cubo["R"][0][2])):
        move = "TYYRUUTBRYTUTNRR"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["G"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        (cubo["G"][0][1] == cubo["R"][0][2])):
        move = "TYYRUUTBRYTUTNRR"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["B"][0][2]) and 
        (cubo["R"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["G"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["B"][0][1] == cubo["G"][0][2]) and
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        #arruma a parte verde
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        (cubo["G"][0][1] == cubo["R"][0][2])):
        move = "TYYRUUTBRYTUTNRR"
        solve += move
        alg(move, cubo)
    
    #caso T
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RYTUTBRRUTURYTN"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RYTUTBRRUTURYTN"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RYTUTBRRUTURYTN"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["R"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["O"][0][0] == cubo["O"][0][2]) and
        (cubo["R"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["O"][0][1] == cubo["B"][0][2]) and
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        #arruma a parte verde
        (cubo["R"][0][0] == cubo["G"][0][2]) and
        (cubo["G"][0][1] == cubo["G"][0][2])):
        move = "RYTUTBRRUTURYTN"
        solve += move
        alg(move, cubo)
    
    #caso V
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["G"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2])):
        move = "TYTUHTGGUHYHRGR"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["G"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2])):
        move = "TYTUHTGGUHYHRGR"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["G"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2])):
        move = "TYTUHTGGUHYHRGR"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["O"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["G"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["R"][0][1] == cubo["B"][0][2])):
        move = "TYTUHTGGUHYHRGR"
        solve += move
        alg(move, cubo)
    
    #caso Y
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2])):
        move = "BRUTURYTNRYTUTBRN"
        solve += "Y" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2])):
        move = "BRUTURYTNRYTUTBRN"
        solve += "YY" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2])):
        move = "BRUTURYTNRYTUTBRN"
        solve += "U" + move
        alg(move, cubo)
    elif ((alg("Y", cubo)["B"][0][0] == cubo["G"][0][2]) and 
        (cubo["B"][0][1] == cubo["B"][0][0]) and 
        #arruma a parte laranja
        (cubo["R"][0][0] == cubo["O"][0][2]) and
        (cubo["G"][0][1] == cubo["O"][0][2]) and
        #arruma a parte vermelha
        (cubo["R"][0][1] == cubo["R"][0][2]) and
        (cubo["O"][0][0] == cubo["R"][0][2]) and
        #arruma a parte verde
        (cubo["G"][0][0] == cubo["B"][0][2]) and
        (cubo["O"][0][1] == cubo["B"][0][2])):
        move = "BRUTURYTNRYTUTBRN"
        solve += move
        alg(move, cubo)
    return solve 
    
def Termina_cubo(solve, cubo):
    #Essa função rotaciona a face amarela, toda permutada, para estar no lugar certo
    if cubo["B"][0][0] == "O":
        move = "Y"
        solve += move
        alg(move, cubo)
    elif cubo["B"][0][0] == "G":
        move = "YY"
        solve += move
        alg(move, cubo)
    elif cubo["B"][0][0] == "R":
        move = "U"
        solve += move
        alg(move, cubo)
    return solve

def tratamento(X):
    #Essa função diminui o tamanho da solve, retirando movimentos desnecessários
    X = list(X)
    Z = 0
    """Essa verificação deve ser aplicada várias vezes, então para saber quando deve-se parar,
    é construído 2 vetores, um para cada verificação de diminuição de solve, de modo que
    a função só será encerrada quando todos esses vetores tiverem o mesmo tamanho, isto é, 
    quando o vetor solve passou pela função e não se alterou"""
    while Z != len(X):
        """A primeira verificação é se na solve ocorre 2 movimentos que se anulam, como por exemplo
        mover a face amarela no snetido horário e, em seguida, no sentido anti-horário"""
        #O vetor Z é rezetado cada vez que o vetor X passa pela verificação, sendo construído antes de possíveis otimizações
        Z = len(X)
        i = 0
        while i < len(X)-1:
            if ((X[i] == "Y" and X[i+1] == "U") or

                (X[i] == "U" and X[i+1] == "Y") or
                (X[i] == "B" and X[i+1] == "N") or
                (X[i] == "N" and X[i+1] == "B") or
                (X[i] == "O" and X[i+1] == "P") or
                (X[i] == "P" and X[i+1] == "O") or
                (X[i] == "G" and X[i+1] == "H") or
                (X[i] == "H" and X[i+1] == "G") or
                (X[i] == "R" and X[i+1] == "T") or
                (X[i] == "T" and X[i+1] == "R") or
                (X[i] == "W" and X[i+1] == "E") or
                (X[i] == "E" and X[i+1] == "W")):
                del X[i : i+1]
                #Se uma otimização foi feita, nenhuma mais será nesse ciclo, para que não haja problemas com índices fora de range
                i += 100
            else:
               i += 1           
        #Na mesma lógica do vetor Z, o vetor Y é construído igualmente como um operador.
        Y = 0
        i = 0
        """Nesse estágio ocorrem sucessivas verificações se 3 movimentos da solve são iguais,
         pois como 270° = -90°, é benéfico verificar esses casos e otimizá-los"""
        while Y != len(X):
            Y = len(X) 
            i = 0
            while i < len(X)-2:
                if X[i] == "Y" and X[i+1] == "Y" and X[i+2] == "Y":
                    X[i] = "U"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "U" and X[i+1] == "U" and X[i+2] == "U":
                    X[i] = "Y"
                    del X[i+1 : i+2]
                    i += 100
                else:
                    i += 1
            i = 0
            while i <= len(X)-2:
                if X[i] == "B" and X[i+1] == "B" and X[i+2] == "B":
                    X[i] = "N"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "N" and X[i+1] == "N" and X[i+2] == "N":
                    X[i] = "B"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "O" and X[i+1] == "O" and X[i+2] == "O":
                    X[i] = "P"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "P" and X[i+1] == "P" and X[i+2] == "P":
                    X[i] = "O"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "G" and X[i+1] == "G" and X[i+2] == "G":
                    X[i] = "H"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "H" and X[i+1] == "H" and X[i+2] == "H":
                    X[i] = "G"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "R" and X[i+1] == "R" and X[i+2] == "R":
                    X[i] = "T"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "T" and X[i+1] == "T" and X[i+2] == "T":
                    X[i] = "R"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "W" and X[i+1] == "W" and X[i+2] == "W":
                    X[i] = "E"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
            i = 0
            while i < len(X)-2:
                if X[i] == "E" and X[i+1] == "E" and X[i+2] == "E":
                    X[i] = "W"
                    del X[i+1 : i+2]
                    i += 100
                else: 
                    i += 1
    return X

def monta_cubo(cubo):
    #A função monta cubo reúne cada função e aplica todas elas em ordem, retornando o cubo resolvido e a solve que o resolveu
    solve = cruz(cubo)
    solve = cantos1(solve, cubo)
    solve = seg_cam(solve, cubo)
    solve = cruz_amarela(solve, cubo)
    solve = oll_de_cruz(solve, cubo)
    solve = pll(solve, cubo)
    solve = Termina_cubo(solve, cubo)
    solve = tratamento(solve)
    return solve 
            
            
# Recebe uma scramble
a =  input("Scramble: ")
#Traduz ela para a linguagem do programa
scramble = traducao_GpI(a)
#Aplica ela no cubo resolvido
alg(scramble, cubo)
#Resolve a partir do cubo embaralhado
solução1 = monta_cubo(cubo)
#Traduz a solve para a linguagem usual
solução = traducao_IpG(solução1)
#Mostra na tela a solve e a quantidade de movimentos
print("Solve: ", solução,"\n Quantidade de movimentos: ",  len(solução1), "\n \n")
#Mostra o cubo na tela
mostra_cubo(cubo)

