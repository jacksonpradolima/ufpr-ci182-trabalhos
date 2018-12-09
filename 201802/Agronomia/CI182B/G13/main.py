fazenda = []
arquivo=open("calcario.csv","w")
#aqui abre o arquivo csv 
arquivo.writelines(["1-Lavoura","  |  ","2-prnt","  |  ","3-CTC","  |  ","4-Soma de Bases","  |  ","5-Calcario T/ha","\n"])
#writelines recebe uma lista e escreve está lista no arquivo csv
calcario=[] 
prnt=[]
ctc=[]#nesta parte estão sendo criadas lista vazias que após a calculo,vão receber informações digitadas pelo usuário
v1=[]
v21=[]
v2 = "1"
contador = 0#atribui valores aos resultados dos calculos realizados
while v2 != "": #no laço enquanto v2 for diferente de vazio(enter) ele ira fazendo novos calculos, quando o usuário pressionar enter ai sai do laço.
    print("""
    __________________________________
    *****  CALCULO DE CORRETIVO  *****
    \t    Selecione apenas uma opção;
    \t1 - Cereais e Tubercúlos;
    \t2 - Leguminosas;
    \t3 - Hortaliças,Café e Frutas;
    \t   " Pressione enter para sair
    \t  (Na opção selecione a lavoura)"
    """)                         #o menu interativo dando as opções disponiveis ao usuário.
    v2 = input("selecine a lavoura desejada : ")
    if v2 != "": #v2 sendo diferente de vazio de vazio então as informações são perguntadas ao usuário
        prnt1= float(input("informe o prnt do corretivo:"))
        prnt.append("{:.2f}".format(prnt1)) #prnt.append atribui o valor inserido no prnt1
        ctc2= float(input("informe a ctc da analise de solo:"))
        ctc.append("{:.2f}".format(ctc2))  #ctc.append atribui o valor inserido no ctc2
        v13= float(input("informe o v% da analise de solo:"))
        v1.append("{:.2f}".format(v13))  #v1.append atribui o valor inserido no v13
        if v2=="1":
            calcario.append("{:.2f}".format(ctc2*(50-v13)*(100/prnt1)/100))
            v21.append("Cereais e Tubérculos")#v21.append atribui a opção selecionada para exportar no arquivo csv
        elif v2 == "2":
            calcario.append("{:.2f}".format(ctc2*(60-v13)*(100/prnt1)/100))
            v21.append("Leguminosas")
        elif v2 == "3":
            calcario.append("{:.2f}".format(ctc2*(70-v13)*(100/prnt1)/100))
            v21.append("Hortaliças,Café e Frutas")
        else:
          print("Inválido.")
        print("Será necessário ",calcario[contador],"T/ha")#
        contador +=1 #atribui valor o resultado para poder imprimir
contador2 = 0 #atribui valores as lista(prnt,ctc,calcario,v21,v1)

for i in range(contador):
    e=str(v21[contador2])#transforma float em string
    d=str(prnt[contador2])
    c=str(ctc[contador2])
    b=str(v1[contador2])
    a=str(calcario[contador2])
    contador2 += 1
    arquivo.writelines(["1-",e,"  |  ","2-",d," |  ","3-",c,"  |  ","4-",b,"  |  ","5-",a,"  |  "])
fazenda.append(calcario)
arquivo.close()#fecha o arquivo depois de salvar as informações
print("t/ha",fazenda,"prnt",prnt,"ctc",ctc,"v1",v1,)



