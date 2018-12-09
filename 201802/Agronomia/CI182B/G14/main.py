# f - fertilidade do solo (CE e V%)
# h -  disponibilidade de agua
# o - oxigenação do solo
# e - erossão
# m - mecanização

#inicialização das variáveis auxiliares
f = 100 # variável para fertilidade do solo
h = 0 #variável para disponibilidade de água
h1 = 100 #variável para disponibilidade de água
o1 = 100 #variável para oxigenação do solo
e1 = 100 #variável para erossão
m1 = 100 #variável para mecanização

print("\t\tCurso de Agronomia\n")
print("\t\tTrabalho da Disciplina de Programação\n")
print("\t\tCapacidade e Aptidão do Solo\n")
print("\tAcademicos: EDUARDA, JOÃO E THIAGO\n")

while(f==100):
   # leitura do CE - condutibilidade eletrica
   ce = float(input("Qual a condutividade elétrica do solo?\n"))
   # leitura do V% - saturação de bases
   v = float(input("\nQual a saturação por bases do solo?\n"))
   # verificação do nível de fertilidade
   if ce < 4 and v > 80:
      f = 0
   elif ce < 4 and v > 50:
       f = 1
   elif 4 < ce < 8 and 35 < v < 50:
         f = 2
   elif 8 < ce < 15 and v < 35:
      f = 3
   elif ce > 15 and v < 35:
      f = 4
   else: print("\nERRO: Valor de condutividade elétrica e/ou saturação por bases do solo inválidos\n")

# leitura do h - Disponibilidade de agua
while(h1==100):
   h = int(input("\nQual a disponibilidade de água, h pode ser:\n0 - Não há definição\n1 - DE 3 A 5 MESES DE ESTIAGEM\n2 - DE 4 A 6 MESES DE ESTIAGEM\n3 - De 7 a 9 MESES DE ESTIAGEM\n4 - MAIS DE 9 MESES DE ESTIAGEM \n"))
   if h==0:
       h1 = 0
   elif h == 1:
        h1 = 1
   elif h == 2:
        h1 = 2
   elif h == 3:
        h1 = 3
   elif h == 4: 
        h1 = 4
   else: print("\nERRO: Valor de disponibilidade de h2o inválido\n")

# leitura do e - Declividade
while(e1==100):
   e = float (input("\nQual o percentual(%) de declividade (0 a 45%)?\n"))
   if e < 3:
       e1 = 0 
   elif 3 <= e < 8:
        e1 = 1
   elif 8 <= e < 13:
        e1 = 2
   elif 13 <= e < 20:
        e1 = 3
   elif 20 <= e <= 45:
        e1 = 4
   else: print("\nERRO: Valor de declividade inválido\n")

# leitura do o - oxigenação do solo
while(o1==100):
   o = int(input("\nQual a oxigenação do solo?\n0 - DRENADO\n1- MODERADAMENTE DRENADO\n2 - MAL DRENADO\n3 - MAIS QUE MAL DRENADO\n4 - INUNDAÇÕES FREQUENTES\n"))
   if o == 0:
       o1 = 0
   elif o == 1:
         o1 = 1
   elif o == 2:
         o1 = 2
   elif o == 3:
      o1 = 3
   elif o == 4:
        o1 =4
   else: print("\nERRO: Valor de oxigenação inválido\n")

#leitura da mecanização m
while(m1==100):
   m = int(input("\nQual a quantidade de pedras no perfil do solo?\n0 - NÃO PEDREGOSA\n1 - MODERADAMENTE PEDREGOSA\n2 - PEDREGOSA\n3 - MUITO PEDREGOSA\n4 - EXTREMAMENTE PEDREGOSA\n"))
   if m == 0:
       m1 = 0 
   elif m == 1:
        m1 = 1 
   elif m == 2:
        m1 = 2
   elif m == 3:
        m1 = 3 
   elif m == 4:
        m1 = 4
   else: print("\nERRO: Valor de percentual de pedras inválido\n")

# validando para que o solo é adequado apartir das respostas do usuário
print("\n\t RESULTADO: \n")
if f == 0 and h == 1 and o == 1 and e1 == 0 and m == 1:
   print("\t\tLAVOURA\n")
elif f == 1 and h == 2 and o == 1 and e1 == 1 and m == 2:
   print("\t\tLAVOURA\n")
elif f == 2 and h == 3 and o == 2 and e1 == 2 and m == 3:
   print("\t\tLAVOURA\n")
elif f == 2 and h == 2 and o == 3 and e1 == 2 and m == 2:
   print("\t\tPASTAGEM\n")
elif f == 3 and h == 3 and o == 3 and e1 == 3 and m == 3:
   print("\t\tPASTAGEM\n")
elif f == 4 and h == 4 and o == 4 and e1 == 4 and m == 3:
   print("\t\tPASTAGEM\n")
elif f == 2 and h == 2 and o == 1 and e1 == 3 and m == 2:
   print("\t\tREFLORESTAMENTO\n")
elif f == 3 and h == 3 and o == 1 and e1 == 3 and m == 3:
   print("\t\tREFLORESTAMENTO\n")
elif f == 4 and h == 4 and o == 2 and e1 == 4 and m == 3:
   print("\t\tREFLORESTAMENTO\n")
else: print("\nAREA DE PRESERVAÇÃO AMBIENTAL\n")

