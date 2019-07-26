m=[["-","-","-"],["-","-","-"],["-","-","-"]]
ind=1
gx=0 
go=0
empate=0
print('=== JOGO DA VELHA === ')
print("OBS:As linhas são de cima para baixo e colunas são da esquerda para direita. Todas começam de 1 e terminam em 3\n")

 #algoritmo de indentificação    
def jogador(ind):
  if ind%2==0:
    ind="x"
    return "x"
  if ind%2==1:
    ind="o"
    return "o" 
        
  #algoritmo que avalia vitoria    
def vitoria(linha,coluna):
  if m[linha-1][0]==jogador(ind) and m[linha-1][1]==jogador(ind) and m[linha-1][2]==jogador(ind):
    print("<::: O jogador dos ",jogador(ind)," GANHOU!! :::>")
    for i in m:
      print(i)
    return vitoria
        
  elif m[0][coluna-1]==jogador(ind) and m[1][coluna-1]==jogador(ind) and m[2][coluna-1]== jogador(ind):
    print("<::: O jogador dos",jogador(ind)," GANHOU!! :::>")
    for i in m:
      print(i)
    return vitoria
      
  elif m[0][0]==jogador(ind) and m[1][1]==jogador(ind) and m[2][2]==jogador(ind):
    print("<::: O jogador dos ",jogador(ind)," GANHOU!! :::>")
    for i in m:
      print(i)
    return vitoria
        
  elif m[2][0]==jogador(ind) and m[1][1]==jogador(ind) and m[0][2]==jogador(ind):
    print("<::: O jogador dos ",jogador(ind), "GANHOU!! :::>")
    for i in m:
      print(i)
    return vitoria
    
  #função da pergunta
def pergunta():
  for i in m:
    print(i)
  a=int(input("Qual a linha voce escolhe? "))
  b=int(input("Qual coluna voce escolhe? "))
  if conclusão(a,b)==True:
    return True
  return False 
  
  #função de erro
def conclusão(linha,coluna):
  if linha<1 or linha>3 or coluna<1 or coluna>3:  
    print("::: <-Erro->Você digitou algum número fora do limite. Digite novamente :::")
    pergunta()
    
  elif m[linha-1][coluna-1]==jogador(ind)or m[linha-1][coluna-1]==jogador(ind+1): 
    print("::: <-Erro->Você digitou uma posição já existente. Digite novamente :::")
    pergunta()
         
  else:  
    m[linha-1][coluna-1]=jogador(ind)
    if vitoria(linha,coluna)==vitoria:
      return True
  return False  
  
while True:      
  while True :
    ind+=1
    x=False
  
  #jogador x
    if jogador(ind)=="x": 
      print("<=== Vez do jogador dos x ===>")
    
  #algoritmo que avalia empate ou leva para funcao  
      if pergunta()==True:
        if jogador(ind)=="x":
          gx+=1
        elif jogador(ind)=="o":
          go+=1
        break
      elif ind==10:
        print("#=== DEU VELHA! EMPATOU!! ===#")
        for i in m:
         print(i)
        empate+=1
        break
  
  #jogador o
    elif jogador(ind)=="o":
      print("<=== Vez do jogador dos o ===>")
    
  #algoritmo que avalia vitoria 
      if pergunta()==True:
        if jogador(ind)=="x":
          gx+=1
        elif jogador(ind)=="o":
          go+=1
        break
      
  x=input("::: Vocês querem jogar novamente?(s/n) :::")
  
  #algoritmo de erro de letra invalida
  while x!="s" and x!="n":
    print("Letra inválida, digite novamente")
    x=input("::: Vocês querem jogar novamente?(s/n) :::")
    
  #algoritmo de confimação  
  if x=="s":
    x=True
    m=[["-","-","-"],["-","-","-"],["-","-","-"]]
    ind=1  
  else:
    break
   
print("< FIM DO JOGO! >")
print("<====== Dados do jogo =======>")
print("O jogador x ganhou: ",gx)
print("O jogador o ganhou: ",go)
print("Empate: ",empate)
  
sair=input("Aperte qualquer tecla para sair")
