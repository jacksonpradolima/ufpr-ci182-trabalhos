
print("_"*168)
qm=input("Como se chama?")
verificacao=int(input("Digite '0' para começar'"))
if not verificacao==0:
    verificacao==int(input(f"{qm} digite o número 0"))
def num_true(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def imprime_matriz(m):
    for l in range(len(m)):
        for c in range(len(m[l])):
            print(f"-  {m[l][c]}  -",end=" ")
        print("\n")
import shelve
db=shelve.open('shelve.db')
estoque=db['lista']
retiradas=[]
del db['lista']

print("-="*38,"ESTOQUE DE PEÇAS","=-"*38)
login="JACKSON"
l=0
senha="ME_PASSA_COM_10"
s=0
verificacao=0
while verificacao==0:
   l=input("LOGIN:")
   s=input("SENHA:")
   if s==senha and l==login:
       verificacao+=1
       print(f"Seja bem vindo {qm}!!!")
   else:
       print("Senha ou Login incorretos, digite novamente")

contiunuar="sim"
while contiunuar=="sim" or contiunuar=="Sim" or contiunuar=="SIM":
    print("Escolha uma das opções e digite seu número correspondente")
    escolhas=["Adicionar Peças","Retirada de peças","Histórico de saída de peças","Estoque atual de peças"]
    for c in range(len(escolhas)):
        if c ==len(escolhas)-1:
            print(f" [{c}]{escolhas[c]}.", end=" ")
        else:
            print(f" [{c}]{escolhas[c]},", end=" ")
    escolhido=input(">")
    i=0
    while i==0:
        if num_true(escolhido)==True:
            escolhido=int(escolhido)
            if escolhido<len(escolhas):
                i+=1
            else:
                escolhido = input("Opção não existe, tente novamente:")
        else:
            escolhido=input("Opção não existe, tente novamente:")
    marcas_0=["Bosch","New Holland","Case","Massey Fergusson","John Deer","Skill","Outros"]
    implementos_00=["Trator","Colheitadeira","Plantadeira","Pulverizador","Carreta","Chupim","Outros"]
    implementos_01=[["Motor","Interior da cabine","Pneus","Tração","Outros"],["Motor","Interior da cabine","Pneus","Tração","Outros"],["Rolamentos","Hidráulica","Pneus","Discos","Outros"],["Motor","Bomba","Pneus","Bicos","Outros"],["Pneus","Caixa de Cambio","Outros"],["Transmissão , rolamentos, outros"],["Peça especifica"]]
    if escolhido==0:
        op=0
        while op==0:
            x=len(estoque)
            estoque.append([])
            nome_peca=input("Qual é o nome a peça:")
            codigo=input("Adicione um código de sua preferência:")
            print("Digite o número correspondente a marca:")
            for c in range(len(marcas_0)):
                print(f"{[c]}-{marcas_0[c]}")
            marca=input(">")
            j = 0
            while j == 0:
                if num_true(marca) == True:
                    marca=int(marca)
                    if marca< len(marcas_0):
                        j += 1
                    else:
                        marca = input("Opção não existe, tente novamente:")
                else:
                    marca = input("Opção não existe, tente novamente:")
            print("Escolha uma opção de implemento:")
            for c in range(len(implementos_00)):
                print(f"{[c]}-{implementos_00[c]}")
            implemento=input(">")
            k = 0
            while k == 0:
                if num_true(implemento) == True:
                    implemento=int(implemento)
                    if implemento< len(implementos_00):
                        k += 1
                    else:
                        implemento = input("Opção não existe, tente novamente:")
                else:
                    implemento = input("Opção não existe, tente novamente:")
            print("Escolha o tipo da peça")
            for c in range(len(implementos_01[implemento])):
                print(f"{[c]}-{implementos_01[implemento][c]}")

            tipo = input(">")
            k = 0
            while k == 0:
                if num_true(tipo) == True:
                    tipo=int(tipo)
                    if tipo < len(implementos_01[implemento]):
                        k += 1
                    else:
                        tipo = input("Opção não existe, tente novamente:")
                else:
                    tipo = input("Opção não existe, tente novamente:")
            estoque[x].append(nome_peca)
            estoque[x].append(codigo)
            estoque[x].append(marcas_0[marca])
            estoque[x].append(implementos_00[implemento])
            estoque[x].append(implementos_01[implemento][marca])
            contiunuar=input("Você deseja adicionar mais peças?('s' para adicionar)>")
            if contiunuar=="s":
                op=0
            else:
                op+=1
    elif escolhido==1:
        z=0
        x=0
        op1=0
        while op1==0:
            r=input("Retirar peça pelo seu nome ou pelo codigo?(digite a opção com letras minusculas e sem acento): ")
            p=0
            while p==0:
                if r=="nome" or r=="codigo":
                    p+=1
                else:
                    r=input("Opção inexistente, escolha uma opção válida:")
            procurar=0
            if r =="nome":
                x=0
                procurar="nome"
            elif r=="codigo":
                x=1
                procurar="codigo"
            retirar_=input(f"Digite o {procurar} que se deseja retirar:")
            while z==0:
                for c in range(len(estoque)):
                    if estoque[c][x]==retirar_:
                        z+=1
                        retiradas.append(estoque[c][x])
                        estoque.remove(estoque[c])
                        print(f"A peça de {procurar} {retirar_} foi removida")
                    else:
                        z=0
                if z==0:
                    retirar_=input(f"{procurar} não foi encontrado na lista, tente novamente ou digite 0: ")
                    if retirar_=="0":
                        z+=1
            op1=input("Para retirar outra peça digite '0', para continuar o programa digite outro numero qualquer:")
    elif escolhido==2:
        if len(retiradas)>0:
            print(f"Peças retiradas:{retiradas}")
        elif len(retiradas)==0:
            print("nenhuma peça foi retirada")
    elif escolhido==3:
        print("ESTOQUE:")
        imprime_matriz(estoque)
    contiunuar=input("Para continuar com o programa digite sim ou aperte enter para finalizar: ")
db=shelve.open('shelve.db')
db['lista']=estoque
a=input(f"BOM TRABALHO {qm}!!! >")
