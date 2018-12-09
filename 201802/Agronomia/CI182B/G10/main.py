import uuid
import hashlib
import datetime
from datetime import date

formatacaoData = "%m/%d/%Y"
now = datetime.datetime.now()

#senha 123
admin_hashed_psswd="f1e9ec4d2a8d93cdbe7109bedcce6020c1ff248a4396acfd5ac0a53a61792b53:30d24e545e2f4fbeb34e40f4fcac107a"

labelBook=["Num","Nome","Autor","Ano","Editora","Quantidade Estoque"]
labelEmprestado=["Usuario","Livro","Num","DataEmprestimo"]

books=[[1,"botanica","lorenzi",1990,"editora1",10],[2,"entomologia","lutz",1990,"editora2",10],[3,"genetica","thompson",1990,"editora1",10],
       [4,"programação","menezes",1990,"editora1",10],[5,"fisiologia","taiz",1990,"editora1",10],[6,"fisica","harley",1990,"editora1",10],
       [7,"calculo","adams",1990,"editora1",10]]

usuarios=[["aluno1","thais","agronomia"],["aluno2","ana","direito"],["aluno3","juliana","civil"],
          ["aluno4","lucas","Fisica"],["aluno5","yuri","mecanica"],["aluno6","paola","zootecnia"]]

emprestimos=[["aluno1","botanica",1,"10/15/2018"],["aluno2","entomologia",2,"11/24/2018"],["aluno3","genetica",6,"11/02/2018"]]

#Usar hash_password para cadastrar uma nova senha se quiser
def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

#hashed_password = hash_password(new_pass)
#print('The string to store in the db is: ' + hashed_password) o valor que será printado aqui é o valor criptografado da nova senha utilizada

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def autenticar():
    print("Login Bibliotecária\n")
    passwd=input("Senha: ")
    if check_password(admin_hashed_psswd, passwd):
        print('Senha correta!\n')
        return True
    else:
        print('Senha incorreta!\n')
        return False

def consultar_usuario():
    print("Insira o usuario que fará o empréstimo\n")
    user = input('Usuario: ')
    for info in usuarios:
        if user == info[0]:
            return True,user
    return False,user

def consulta_emprestados(user):
     qtd=0
     hoje=datetime.datetime.now()
     for info in emprestimos:
         if user == info[0]:
             dloc=datetime.datetime.strptime(info[3],formatacaoData)
             dif = hoje-dloc
             if dif.days > 15:
                return -1*dif.days
             qtd+=1
     return qtd

def consulta_livros():
    print("Por favor insira o nome do livro ou o autor\n")
    busca=input("Nome/Autor: ")
    print(*labelBook)
    for info in books:
        if (busca == info[1] or busca == info[2]) and info[5]>0:
            print(*info)
    print("Escolha o livro a partir do Num equivalente, caso não tenha sido encontrado nenhum livro, ou você não queira nenhuma da lista utilize -1\n")
    opcao=int(input("Num: "))
    return opcao
    
def escolha(limite,user):
    while limite > 0:
        print("Escolha o livro que você deseja emprestar\n")
        print("E você ainda pode realizar ", limite, " emprestimos\n")
        print("1-> Livro  2->Sair")
        indice=0
        opcao=int(input("Opcao :"))
        if opcao ==1:
            livro=consulta_livros()
            if livro!=-1:
                for info in books: 
                    if info[0]==livro:
                        books[indice][5]-=1
                        emprestimos.append([user,books[indice][1],books[indice][0],datetime.datetime.now().strftime("%m/%d/%Y")])
                        limite-=1
                        print("EMPRÉSTIMO REALIZADO COM SUCESSO\n")
                        break
                    else:
                        indice+=1
        elif opcao==2:
            print("Emprestimo cancelado")
            return
        if limite == 0:
            print("Você atingiu o limite de emprestimos, para poder emprestar outros primeiro devolva algum\n")
    
def emprestar(user):
    quantidade=consulta_emprestados(user)
    if  quantidade==0:
        print("O usuário selecionado é ", user," , e este poderá emprestar apenas três exemplares por vez e o prazo de expiração de cada empréstimo é de 15 dias!\n")
        escolha(3,user)
    elif quantidade==1:
        print("O usuário selecionado é ", user," , e este poderá emprestar apenas 2 exemplares por 15 dias pois já possui um exemplar emprestado!\n")
        escolha(2,user)
    elif quantidade==2:
        escolha(1,user)
        print("O usuário selecionado é  ", user," , e este poderá emprestar apenas 1 exemplar por 15 dias pois já possui dois exemplares emprestados!\n")
    elif quantidade==3:
        print("O usuário não pode emprestar nenhum livro pois já possui três emprestados, você deve devolver um primeiro!.\n")
    elif quantidade<0:
        print("O usuário não pode emprestar nenhum pois possui um livro com entrega atrasada em ", -1*quantidade , " dia(s)\n")


def main():	
    sair=False
    auth=False
    
    while sair==False:
        #print(*emprestimos)
        if auth==False:
            auth=autenticar()
            print("Autenticação realizada com sucesso!\n")
        encontrado=False
        
        if auth:
            while encontrado ==False:
                encontrado,user=consultar_usuario()
                if encontrado == False:
                    print("Usuario não encontrado, procure outro")
                    
            while encontrado == True:
                print("O que você desejar fazer?\n")
                print("1-> Emprestar  2-> Trocar Usuário")
                opcao=int(input("Opcao :"))
                if opcao ==1:
                    emprestar(user)
                elif opcao ==2:
                    encontrado=False
                else:
                    print("OPÇÃO INVÁLIDA!\n")
        else:
            print("Usuario nao encontrado\n")

        print("Deseja sair do programa? 1 ->Sim 2-> Não")
        op=int(input("Opção: "))

        if op==1:
            sair=True
            print("Programa finalizado\n")

            

if __name__=="__main__":
    main()

    
        
           

