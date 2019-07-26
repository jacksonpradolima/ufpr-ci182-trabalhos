#--------------------------------------------------------------------------------------------
#Mostra a configuração atual do cubo:
def Cprint():
    print([pos[0][0]]+[pos[1][0]]+[pos[2][0]]+[pos[3][0]]+[pos[4][0]]+[pos[5][0]])
    print([pos[0][1]]+[pos[1][1]]+[pos[2][1]]+[pos[3][1]]+[pos[4][1]]+[pos[5][1]])
    print([pos[0][2]]+[pos[1][2]]+[pos[2][2]]+[pos[3][2]]+[pos[4][2]]+[pos[5][2]],"\n \n")

#-------------------------------------------------------------------------------------------
#Rotações:

#Movimento R (Face direita sentido horário):
def movR():
    aux = pos.copy() #cria-se uma cópia da lista pos atual
    pos[1] = [[aux[1][0][0],aux[1][0][1],aux[4][0][2]],[aux[1][1][0],aux[1][1][1],aux[4][1][2]],[aux[1][2][0],aux[1][2][1],aux[4][2][2]]] #reatribui-se os elementos novos com base nos elementos da cópia
    pos[2] = [[aux[2][2][0],aux[2][1][0],aux[2][0][0]],[aux[2][2][1],aux[2][1][1],aux[2][0][1]],[aux[2][2][2],aux[2][1][2],aux[2][0][2]]]
    pos[3] = [[aux[5][2][2],aux[3][0][1],aux[3][0][2]],[aux[5][1][2],aux[3][1][1],aux[3][1][2]],[aux[5][0][2],aux[3][2][1],aux[3][2][2]]]
    pos[4] = [[aux[4][0][0],aux[4][0][1],aux[3][2][0]],[aux[4][1][0],aux[4][1][1],aux[3][1][0]],[aux[4][2][0],aux[4][2][1],aux[3][0][0]]]
    pos[5] = [[aux[5][0][0],aux[5][0][1],aux[1][0][2]],[aux[5][1][0],aux[5][1][1],aux[1][1][2]],[aux[5][2][0],aux[5][2][1],aux[1][2][2]]]

#Movimento R' (Face direita sentido anti-horário, equivalente a rotacionar sentido horário 3 vezes):
def movRi():
    movR()
    movR()
    movR()
    
#Movimento L (Face esquerda sentido horário):
def movL():
    aux = pos.copy()
    pos[0] = [[aux[0][2][0],aux[0][1][0],aux[0][0][0]],[aux[0][2][1],aux[0][1][1],aux[0][0][1]],[aux[0][2][2],aux[0][1][2],aux[0][0][2]]]
    pos[1] = [[aux[5][0][0],aux[1][0][1],aux[1][0][2]],[aux[5][1][0],aux[1][1][1],aux[1][1][2]],[aux[5][2][0],aux[1][2][1],aux[1][2][2]]]           
    pos[3] = [[aux[3][0][0],aux[3][0][1],aux[4][2][0]],[aux[3][1][0],aux[3][1][1],aux[4][1][0]],[aux[3][2][0],aux[3][2][1],aux[4][0][0]]]
    pos[4] = [[aux[1][0][0],aux[4][0][1],aux[4][0][2]],[aux[1][1][0],aux[4][1][1],aux[4][1][2]],[aux[1][2][0],aux[4][2][1],aux[4][2][2]]]
    pos[5] = [[aux[3][2][2],aux[5][0][1],aux[5][0][2]],[aux[3][1][2],aux[5][1][1],aux[5][1][2]],[aux[3][0][2],aux[5][2][1],aux[5][2][2]]]

#Movimento L' (Face esquerda sentido anti-horário):
def movLi():
    movL()
    movL()
    movL()


#Movimento U (Face superior sentido horário):
def movU():
    aux = pos.copy()
    pos[0] = [[aux[1][0][0],aux[1][0][1],aux[1][0][2]],[aux[0][1][0],aux[0][1][1],aux[0][1][2]],[aux[0][2][0],aux[0][2][1],aux[0][2][2]]]
    pos[1] = [[aux[2][0][0],aux[2][0][1],aux[2][0][2]],[aux[1][1][0],aux[1][1][1],aux[1][1][2]],[aux[1][2][0],aux[1][2][1],aux[1][2][2]]]
    pos[2] = [[aux[3][0][0],aux[3][0][1],aux[3][0][2]],[aux[2][1][0],aux[2][1][1],aux[2][1][2]],[aux[2][2][0],aux[2][2][1],aux[2][2][2]]]
    pos[3] = [[aux[0][0][0],aux[0][0][1],aux[0][0][2]],[aux[3][1][0],aux[3][1][1],aux[3][1][2]],[aux[3][2][0],aux[3][2][1],aux[3][2][2]]]
    pos[5] = [[aux[5][2][0],aux[5][1][0],aux[5][0][0]],[aux[5][2][1],aux[5][1][1],aux[5][0][1]],[aux[5][2][2],aux[5][1][2],aux[5][0][2]]]

#Movimento U' (Face superior sentido anti-horário):
def movUi():
    movU()
    movU()
    movU()

#Movimento D (Face inferior sentido horário):
def movD():
    aux = pos.copy()
    pos[0] = [[aux[0][0][0],aux[0][0][1],aux[0][0][2]],[aux[0][1][0],aux[0][1][1],aux[0][1][2]],[aux[3][2][0],aux[3][2][1],aux[3][2][2]]]
    pos[1] = [[aux[1][0][0],aux[1][0][1],aux[1][0][2]],[aux[1][1][0],aux[1][1][1],aux[1][1][2]],[aux[0][2][0],aux[0][2][1],aux[0][2][2]]]
    pos[2] = [[aux[2][0][0],aux[2][0][1],aux[2][0][2]],[aux[2][1][0],aux[2][1][1],aux[2][1][2]],[aux[1][2][0],aux[1][2][1],aux[1][2][2]]]
    pos[3] = [[aux[3][0][0],aux[3][0][1],aux[3][0][2]],[aux[3][1][0],aux[3][1][1],aux[3][1][2]],[aux[2][2][0],aux[2][2][1],aux[2][2][2]]]
    pos[4] = [[aux[4][2][0],aux[4][1][0],aux[4][0][0]],[aux[4][2][1],aux[4][1][1],aux[4][0][1]],[aux[4][2][2],aux[4][1][2],aux[4][0][2]]]

#Movimento D' (Face inferior sentido anti-horário):
def movDi():
    movD()
    movD()
    movD()

#Movimento F (Face frontal sentido horário):
def movF():
    aux = pos.copy()
    pos[0] = [[aux[0][0][0],aux[0][0][1],aux[4][0][0]],[aux[0][1][0],aux[0][1][1],aux[4][0][1]],[aux[0][2][0],aux[0][2][1],aux[4][0][2]]]
    pos[1] = [[aux[1][2][0],aux[1][1][0],aux[1][0][0]],[aux[1][2][1],aux[1][1][1],aux[1][0][1]],[aux[1][2][2],aux[1][1][2],aux[1][0][2]]]
    pos[2] = [[aux[5][2][0],aux[2][0][1],aux[2][0][2]],[aux[5][2][1],aux[2][1][1],aux[2][1][2]],[aux[5][2][2],aux[2][2][1],aux[2][2][2]]]
    pos[4] = [[aux[2][2][0],aux[2][1][0],aux[2][0][0]],[aux[4][1][0],aux[4][1][1],aux[4][1][2]],[aux[4][2][0],aux[4][2][1],aux[4][2][2]]]
    pos[5] = [[aux[5][0][0],aux[5][0][1],aux[5][0][2]],[aux[5][1][0],aux[5][1][1],aux[5][1][2]],[aux[0][2][2],aux[0][1][2],aux[0][0][2]]]


#Movimento F' (Face frontal sentido anti-horário):
def movFi():
    movF()
    movF()
    movF()

#Movimento B (Face traseira sentido horário):
def movB():
    aux = pos.copy()
    pos[0] = [[aux[5][0][2],aux[0][0][1],aux[0][0][2]],[aux[5][0][1],aux[0][1][1],aux[0][1][2]],[aux[5][0][0],aux[0][2][1],aux[0][2][2]]]
    pos[2] = [[aux[2][0][0],aux[2][0][1],aux[4][2][2]],[aux[2][1][0],aux[2][1][1],aux[4][2][1]],[aux[2][2][0],aux[2][2][1],aux[4][2][0]]]
    pos[3] = [[aux[3][2][0],aux[3][1][0],aux[3][0][0]],[aux[3][2][1],aux[3][1][1],aux[3][0][1]],[aux[3][2][2],aux[3][1][2],aux[3][0][2]]]
    pos[4] = [[aux[4][0][0],aux[4][0][1],aux[4][0][2]],[aux[4][1][0],aux[4][1][1],aux[4][1][2]],[aux[0][0][0],aux[0][1][0],aux[0][2][0]]]
    pos[5] = [[aux[2][0][2],aux[2][1][2],aux[2][2][2]],[aux[5][1][0],aux[5][1][1],aux[5][1][2]],[aux[5][2][0],aux[5][2][1],aux[5][2][2]]]

#Movimento B' (Face traseira sentido anti-horário):
def movBi():
    movB()
    movB()
    movB()
    
#Movimento M (Camada vertical do meio sentido horário análogo a face direita):
def movM():
    aux = pos.copy()
    pos[1] = [[aux[1][0][0],aux[4][0][1],aux[1][0][2]],[aux[1][1][0],aux[4][1][1],aux[1][1][2]],[aux[1][2][0],aux[4][2][1],aux[1][2][2]]]
    pos[3] = [[aux[3][0][0],aux[5][2][1],aux[3][0][2]],[aux[3][1][0],aux[5][1][1],aux[3][1][2]],[aux[3][2][0],aux[5][0][1],aux[3][2][2]]]
    pos[4] = [[aux[4][0][0],aux[3][2][1],aux[4][0][2]],[aux[4][1][0],aux[3][1][1],aux[4][1][2]],[aux[4][2][0],aux[3][0][1],aux[4][2][2]]]
    pos[5] = [[aux[5][0][0],aux[1][0][1],aux[5][0][2]],[aux[5][1][0],aux[1][1][1],aux[5][1][2]],[aux[5][2][0],aux[1][2][1],aux[5][2][2]]]

#Movimento M'(Camada vertical do meio sentido anti-horário análogo a face direita):
def movMi():
    movM()
    movM()
    movM()
    
#Movimento E (Camada horizontal do meio sentido horário análogo a face superior):
def movE():
    aux = pos.copy()
    pos[0] = [[aux[0][0][0],aux[0][0][1],aux[0][0][2]],[aux[1][1][0],aux[1][1][1],aux[1][1][2]],[aux[0][2][0],aux[0][2][1],aux[0][2][2]]]
    pos[1] = [[aux[1][0][0],aux[1][0][1],aux[1][0][2]],[aux[2][1][0],aux[2][1][1],aux[2][1][2]],[aux[1][2][0],aux[1][2][1],aux[1][2][2]]]
    pos[2] = [[aux[2][0][0],aux[2][0][1],aux[2][0][2]],[aux[3][1][0],aux[3][1][1],aux[3][1][2]],[aux[2][2][0],aux[2][2][1],aux[2][2][2]]]
    pos[3] = [[aux[3][0][0],aux[3][0][1],aux[3][0][2]],[aux[0][1][0],aux[0][1][1],aux[0][1][2]],[aux[3][2][0],aux[3][2][1],aux[3][2][2]]]

#Movimento E' (Camada horizontal do meio sentido anti-horário análogo a face superior):
def movEi():
    movE()
    movE()
    movE()
#--------------------------------------------------------------------------------------------------------------------------------------------
#Função que executa o algoritmo informado por string (Para evitar erros, todo algortimo deve ser seguido de um espaço no final):
def exealg(alg):
    k = 0
    while k < len(alg):
        if alg[k] == "L":
            if alg[k+1] == "i":
                movLi()
            else:
                movL()
        elif alg[k] == "F":
            if alg[k+1] == "i":
                movFi()
            else:
                movF()
        elif alg[k] == "R":
            if alg[k+1] == "i":
                movRi()
            else:
                movR()
        elif alg[k] == "B":
            if alg[k+1] == "i":
                movBi()
            else:
                movB()
        elif alg[k] == "D":
            if alg[k+1] == "i":
                movDi()
            else:
                movD()
        elif alg[k] == "U":
            if alg[k+1] == "i":
                movUi()
            else:
                movU()
        elif alg[k] == "M":
            if alg[k+1] == "i":
                movMi()
            else:
                movM()
        elif alg[k] == "E":
            if alg[k+1] == "i":
                movEi()
            else:
                movE()
        elif alg[k] == "S":
            if alg[k+1] == "e":
                edgeswap()
            elif alg[k+1] == "c":
                cornerswap()
        elif alg[k] == "P":
            parityswap()
        k = k + 1       
#----------------------------------------------------------------------------------------------------------------------------------------
#Função que retorna a inversão de um algortimo dado por string:
def invalg(alg):
    k = 0
    alginv = str()
    while k < len(alg):
        if alg[k] == "L":
            if alg[k+1] == "i":
                alginv = "L" + alginv
            else:
                alginv = "Li" + alginv
        elif alg[k] == "F":
            if alg[k+1] == "i":
                alginv = "F" + alginv
            else:
                alginv = "Fi" + alginv
        elif alg[k] == "R":
            if alg[k+1] == "i":
                alginv = "R" + alginv
            else:
                alginv = "Ri" + alginv
        elif alg[k] == "B":
            if alg[k+1] == "i":
                alginv = "B" + alginv
            else:
                alginv = "Bi" + alginv
        elif alg[k] == "D":
            if alg[k+1] == "i":
                alginv = "D" + alginv
            else:
                alginv = "Di" + alginv
        elif alg[k] == "U":
            if alg[k+1] == "i":
                alginv = "U" + alginv
            else:
                alginv = "Ui" + alginv
        elif alg[k] == "M":
            if alg[k+1] == "i":
                alginv = "M" + alginv
            else:
                alginv = "Mi" + alginv
        elif alg[k] == "E":
            if alg[k+1] == "i":
                alginv = "E" + alginv
            else:
                alginv = "Ei" + alginv
        elif alg[k] == "S":
            if alg[k+1] == "e":
                alginv = "Se" + alginv
            else:
                alginv = "Sc" + alginv
        elif alg[k] == "P":
            alginv = "P" + alginv
        alginv = alginv + " "           #acrescenta-se um espaço no final da string para evitar erros com a contagem [k+1]
        k = k + 1                   
    return alginv
#---------------------------------------------------------------------------------
#Algoritmos Fundamentais do Método Blindfolded:

#Permutação dos meios:
def edgeswap():
    exealg("RURiUiRiFRRUiRiUiRURiFi ")

#Permutação dos cantos:
def cornerswap():
    exealg("RUiRiUiRURiFiRURiUiRiFR ")

#Resolução de "paridade":
def parityswap():
    exealg("RUiRiUiRURDRiUiRDiRiUURiUi ")

#--------------------------------------------------------------------------------
#Função que verifica se os meios estão resolvidos
def edgesolved():
    i = 0
    while i < 6:                         
        if not(pos[i][0][1] == i and 
        	pos[i][1][0] == i and 
        	pos[i][1][2] == i and 
        	pos[i][2][1] == i):
            return False
        i = i + 1
    return True


#Função que verifica se os cantos estão resolvidos
def cornersolved():
    i = 0
    while i < 6:                         
        if not(pos[i][0][0] == i and 
        	pos[i][0][2] == i and 
        	pos[i][2][0] == i and 
        	pos[i][2][2] == i):
            return False
        i = i + 1
    return True
#--------------------------------------------------------------------------------------------------------------------------------------------
#Separação em casos - Meios:

#Função que verifica se a peça do buffer está em sua posição
def edgebuf():
    if (pos[2][0][1] == 2 and pos[5][1][2] == 5) or (pos[2][0][1] == 5 and pos[5][1][2] == 2):
        return True
    else:
        return False

#Função que verifica qual é a peça que deverá permutar e retorna o algoritmo de preparação(prep) para a permutação
def solvingEdges():
    if(edgebuf() == True and not(pos[5][0][1] == 5)) or (pos[2][0][1] == 5 and pos[5][1][2] == 3): #Se (o buffer está em sua posição e a peça X não está resolvida) ou (a peça X está no buffer)
        prep = "MDLL "                                                                             #O algoritmo que leva a posição da peça X até a posição de troca é esse
    elif(edgebuf() == True and not(pos[5][2][1] == 5)) or (pos[2][0][1] == 5 and pos[5][1][2] == 1):
        prep = "MiDiLL "
    elif(edgebuf() == True and not(pos[5][1][0] == 5)) or (pos[2][0][1] == 5 and pos[5][1][2] == 0):
        prep = "LEL "
    elif(edgebuf() == True and not(pos[0][0][1] == 0)) or (pos[2][0][1] == 0 and pos[5][1][2] == 5):
        prep = "LLi " #chuncho
    elif(edgebuf() == True and not(pos[0][1][2] == 0)) or (pos[2][0][1] == 0 and pos[5][1][2] == 1):
        prep = "Li "
    elif(edgebuf() == True and not(pos[0][2][1] == 0)) or (pos[2][0][1] == 0 and pos[5][1][2] == 4):
        prep = "LL "     
    elif(edgebuf() == True and not(pos[0][1][0] == 0)) or (pos[2][0][1] == 0 and pos[5][1][2] == 3):
        prep = "L "
    elif(edgebuf() == True and not(pos[1][0][1] == 1)) or (pos[2][0][1] == 1 and pos[5][1][2] == 5):
        prep = "MMDLL "
    elif(edgebuf() == True and not(pos[1][1][2] == 1)) or (pos[2][0][1] == 1 and pos[5][1][2] == 2):
        prep = "ELi "
    elif(edgebuf() == True and not(pos[1][2][1] == 1)) or (pos[2][0][1] == 1 and pos[5][1][2] == 4):
        prep = "DiLL "
    elif(edgebuf() == True and not(pos[1][1][0] == 1)) or (pos[2][0][1] == 1 and pos[5][1][2] == 0):
        prep = "EL "  
    elif(edgebuf() == True and not(pos[2][1][2] == 2)) or (pos[2][0][1] == 2 and pos[5][1][2] == 3):
        prep = "EELi "
    elif(edgebuf() == True and not(pos[2][2][1] == 2)) or (pos[2][0][1] == 2 and pos[5][1][2] == 4):
        prep = "DDLL "
    elif(edgebuf() == True and not(pos[2][1][0] == 2)) or (pos[2][0][1] == 2 and pos[5][1][2] == 1):
        prep = "EEL "
    elif(edgebuf() == True and not(pos[3][0][1] == 3)) or (pos[2][0][1] == 3 and pos[5][1][2] == 5):
        prep = "MMDiLL "  
    elif(edgebuf() == True and not(pos[3][1][2] == 3)) or (pos[2][0][1] == 3 and pos[5][1][2] == 0):
        prep = "EiLi "
    elif(edgebuf() == True and not(pos[3][2][1] == 3)) or (pos[2][0][1] == 3 and pos[5][1][2] == 4):
        prep = "DLL "
    elif(edgebuf() == True and not(pos[3][1][0] == 3)) or (pos[2][0][1] == 3 and pos[5][1][2] == 2):
        prep = "EiL "
    elif(edgebuf() == True and not(pos[4][0][1] == 4)) or (pos[2][0][1] == 4 and pos[5][1][2] == 1):
        prep = "MiDLL "
    elif(edgebuf() == True and not(pos[4][1][2] == 4)) or (pos[2][0][1] == 4 and pos[5][1][2] == 2):
        prep = "DiMiDLL "
    elif(edgebuf() == True and not(pos[4][2][1] == 4)) or (pos[2][0][1] == 4 and pos[5][1][2] == 3):
        prep = "MDiLL "
    elif(edgebuf() == True and not(pos[4][1][0] == 4)) or (pos[2][0][1] == 4 and pos[5][1][2] == 0):
        prep = "DiMDiLL "
    return prep

#--------------------------------------------------------------------------------------------------------------------------------------------
#Separação em casos - Cantos:

#Função que verifica se a peça do buffer está em sua posição
def cornerbuf():
    if (pos[0][0][0] == 0 and pos[5][0][0] == 5 and pos[3][0][2] == 3) or (pos[0][0][0] == 3 and pos[5][0][0] == 0 and pos[3][0][2] == 5) or (pos[0][0][0] == 5 and pos[5][0][0] == 3 and pos[3][0][2] == 0):
        return True
    else:
        return False

#Função que verifica qual é a peça que deverá permutar e retorna o algoritmo de preparação(prep) para a permutação
def solvingCorners():
    if(cornerbuf() == True and not(pos[5][0][2] == 5)) or (pos[0][0][0] == 5 and pos[5][0][0] == 2 and pos[3][0][2] == 3):  #Se (o buffer está em sua posição e a peça X não está resolvida) ou (a peça X está no buffer)
        prep = "RR "                                                                                                        #O algoritmo que leva a posição da peça X até a posição de troca é esse
    elif(cornerbuf() == True and not(pos[5][2][2] == 5)) or (pos[0][0][0] == 5 and pos[5][0][0] == 1 and pos[3][0][2] == 2):
        prep = "RRDi "
    elif(cornerbuf() == True and not(pos[5][2][0] == 5)) or (pos[0][0][0] == 5 and pos[5][0][0] == 0 and pos[3][0][2] == 1):
        prep = "FF "
    elif(cornerbuf() == True and not(pos[0][0][2] == 0)) or (pos[0][0][0] == 0 and pos[5][0][0] == 1 and pos[3][0][2] == 5):
        prep = "FiD "
    elif(cornerbuf() == True and not(pos[0][2][2] == 0)) or (pos[0][0][0] == 0 and pos[5][0][0] == 4 and pos[3][0][2] == 1):
        prep = "Fi "
    elif(cornerbuf() == True and not(pos[0][2][0] == 0)) or (pos[0][0][0] == 0 and pos[5][0][0] == 3 and pos[3][0][2] == 4):
        prep = "DiR "
    elif(cornerbuf() == True and not(pos[1][0][0] == 1)) or (pos[0][0][0] == 1 and pos[5][0][0] == 5 and pos[3][0][2] == 0):
        prep = "FRi "
    elif(cornerbuf() == True and not(pos[1][0][2] == 1)) or (pos[0][0][0] == 1 and pos[5][0][0] == 2 and pos[3][0][2] == 5):
        prep = "Ri "
    elif(cornerbuf() == True and not(pos[1][2][2] == 1)) or (pos[0][0][0] == 1 and pos[5][0][0] == 4 and pos[3][0][2] == 2):
        prep = "RiDi "
    elif(cornerbuf() == True and not(pos[1][2][0] == 1)) or (pos[0][0][0] == 1 and pos[5][0][0] == 0 and pos[3][0][2] == 4):
        prep = "FiRiDi "
    elif(cornerbuf() == True and not(pos[2][0][0] == 2)) or (pos[0][0][0] == 2 and pos[5][0][0] == 5 and pos[3][0][2] == 1):
        prep = "F "
    elif(cornerbuf() == True and not(pos[2][0][2] == 2)) or (pos[0][0][0] == 2 and pos[5][0][0] == 3 and pos[3][0][2] == 5):
        prep = "RiF "
    elif(cornerbuf() == True and not(pos[2][2][2] == 2)) or (pos[0][0][0] == 2 and pos[5][0][0] == 4 and pos[3][0][2] == 3):
        prep = "RRF "
    elif(cornerbuf() == True and not(pos[2][2][0] == 2)) or (pos[0][0][0] == 2 and pos[5][0][0] == 1 and pos[3][0][2] == 4):
        prep = "DR "
    elif(cornerbuf() == True and not(pos[3][0][0] == 3)) or (pos[0][0][0] == 3 and pos[5][0][0] == 5 and pos[3][0][2] == 2):
        prep = "RDi "
    elif(cornerbuf() == True and not(pos[3][2][2] == 3)) or (pos[0][0][0] == 3 and pos[5][0][0] == 4 and pos[3][0][2] == 0):
        prep = "DFi "
    elif(cornerbuf() == True and not(pos[3][2][0] == 3)) or (pos[0][0][0] == 3 and pos[5][0][0] == 2 and pos[3][0][2] == 4):
        prep = "R "
    elif(cornerbuf() == True and not(pos[4][0][0] == 4)) or (pos[0][0][0] == 4 and pos[5][0][0] == 1 and pos[3][0][2] == 0):
        prep = "D "
    elif(cornerbuf() == True and not(pos[4][0][2] == 4)) or (pos[0][0][0] == 4 and pos[5][0][0] == 2 and pos[3][0][2] == 1):
        prep = "RRi " #chuncho
    elif(cornerbuf() == True and not(pos[4][2][2] == 4)) or (pos[0][0][0] == 4 and pos[5][0][0] == 3 and pos[3][0][2] == 2):
        prep = "Di "
    elif(cornerbuf() == True and not(pos[4][2][0] == 4)) or (pos[0][0][0] == 4 and pos[5][0][0] == 0 and pos[3][0][2] == 3):
        prep = "DD "
    return prep

#--------------------------------------------------------------------------------------------------------------------------------------------
#Posição identidade (Para testes):
#pos = [[[int(j) for i in range(3)] for k in range (3)] for j in range(6)]


#--------------------------------------------------------------------------------------------------------------------------------------------
#Execução principal do código(De forma resumida, é a aplicação do método blindfolded programada):

pos = []
for k in range(6):
    M = []
    for i in range(3):
        M.append([int(i) for i in input().split()])
    pos.append(M)

Cprint()

algT = str()  #Algoritmo Total
n = 0         #Quantidade de Permutações dos meios

while edgesolved() == False:   #Enquanto os meios não estão resolvidos
    prep = solvingEdges()      #Verificar a peça a ser permutada e obter algoritmo de preparação
    exealg(prep)               #Executar preparação
    edgeswap()                 #Permutação dos meios
    exealg(invalg(prep))        #Executar o inverso do algoritmo de preparação
    algT = algT + prep + "Se" + invalg(prep) #Algoritmo total recebe: ele mesmo + a preparação + Se(notação da permutação) + o inverso da preparação
    n = n + 1

if not(n%2 == 0):  #Se a quantidade de permutações executadas não for par
    parityswap()   #Algoritmo de resolução de paridade

while cornersolved() == False:    #Execução análoga para os cantos
    prep = solvingCorners()
    exealg(prep)
    cornerswap()
    exealg(invalg(prep))
    algT = algT + prep + "Sc" + invalg(prep)

print(algT.replace(" ",""))
#---------------------------------------------------------------------------------------------------------------------------------------------







