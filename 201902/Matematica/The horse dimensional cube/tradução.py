"""Para melhorar o programa e deixar ele mais fácil de usar, aqui é criado 2 programas que 
transformam a escrita usual na escrita que o programa entende e vice-versa"""

def traducao_IpG(X):
    """Aqui a solve pronta, o output do programa, entra e é traduzida para a linguagem usual, porém com uns adendos:
    Na linguagem usual, é escrito por padrão o movimento e depois o número 2, quando o movimento é duplo,
    por exemplo: U2, R2, etc. Além disso é sempre escrito o movimento no sentido horário.
    Porém aqui isso não ocorre, então por padrão o 2 vem antes e, dependendo da solve, pode
    haver 2 movimentos no sentido anti-hórario, como por exemplo 2U'"""
    fim = ""
    for j in range(len(X)-1):
        if X[j] == X[j+1]:
            X[j] = "2"
    for i in X:
        #Movimentos na face U
        if i == "Y":
            fim += "U "
        elif i == "U":
            fim += "U' "
        #Movimentos na face B
        elif i == "B":
            fim += "F "
        elif i == "N":
            fim += "F' "
        #Movimentos na face O
        elif i == "O":
            fim += "L "
        elif i == "P":
            fim += "L' "
        #Movimentos na face R
        elif i == "T":
            fim += "R' "
        elif i == "R":
            fim += "R "
        #Movimentos na face W
        elif i == "W":
            fim += "D "
        elif i == "E":
            fim += "D' "
        #Movimentos na face G
        elif i == "G":
            fim += "B "
        elif i == "H":
            fim += "B' "
        elif i == "2":
            fim += "2"
    return fim
  
def traducao_GpI(X):
    #Essa função traduz uma scramble na notação usual para a notação que o programa entende.
    X = X.split()
    algoritmo = ""
    for i in range(len(X)):
        if X[i] == "L'":
            algoritmo += "P"
        elif X[i] == "F'":
            algoritmo += "N"
        elif X[i] == "D'":
            algoritmo += "E"
        elif X[i] == "R'":
            algoritmo += "T"
        elif X[i] == "U'":
            algoritmo += "U"
        elif X[i] == "B'":
            algoritmo += "H"
        
        elif X[i] == "L2":
            algoritmo += "PP"
        elif X[i] == "F2":
            algoritmo += "NN"
        elif X[i] == "D2":
            algoritmo += "EE"
        elif X[i] == "R2":
            algoritmo += "TT"
        elif X[i] == "U2":
            algoritmo += "UU"
        elif X[i] == "B2":
            algoritmo += "HH"
        
        elif X[i] == "L":
            algoritmo += "O"
        elif X[i] == "F":
            algoritmo += "B"
        elif X[i] == "D":
            algoritmo += "W"
        elif X[i] == "U":
            algoritmo += "Y"
        elif X[i] == "B":
            algoritmo += "G"
        elif X[i] == "R":
            algoritmo += "R"
    return algoritmo
