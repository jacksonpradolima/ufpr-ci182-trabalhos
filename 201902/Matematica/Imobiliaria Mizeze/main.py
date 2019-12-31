#importando a biblioteca Tkinter
from tkinter import*
#Abrindo janela principal
janela = Tk()
janela.title("New Application")
janela.geometry("1450x700+0+0")

#Informações que serão printadas na tela
Titulo1 = Label(janela, text="Olá, seja bem-vindo a Imobiliária MZZ", font =("Times", 42, "bold"),fg="black").place(x=200,y=100)
Titulo2 = Label(janela, text="Escolha o que você deseja fazer hoje:", font =("Times", 35, "bold"),fg="gray40").place(x=275,y=200)

#Variáveis a serem utilizadas depois
casas, casa, aceitadas, filtros = [], [], [], []

#Chamada quando clicado o botão "próxima" da tela 4
def proxima_casa(janela4):
        #Destrui a tela 4
        janela4.destroy()
        #Deleta a casa da posição 0 da matriz "filtros"
        del(filtros[0])
        #Abre uma nova tela 4
        janela4 = Toplevel(janela)
        janela4.geometry("1450x700+0+0")
        # Printa na tela a próxima casa que condiz com o que deseja o comprador
        casa = Label(janela4, text="Casa:", font=("Times", 25, "bold"), fg="black").place(x=100, y=140)

        nome = Label(janela4, text=filtros[0][0], font=("Times", 18,), fg="gray40").place(x=240, y=202)
        Nome = Label(janela4, text="Proprietário:", font=("Times", 18, "bold"), fg="black").place(x=100, y=200)

        endereço = Label(janela4, text=filtros[0][1], font=("Times", 18), fg="gray40").place(x=240, y=232)
        Endereço = Label(janela4, text="Endereço:", font=("Times", 18, "bold"), fg="black").place(x=100, y=230)

        bairro = Label(janela4, text=filtros[0][2], font=("Times", 18), fg="gray40").place(x=240, y=262)
        Bairro = Label(janela4, text="Bairro:", font=("Times", 18, "bold"), fg="black").place(x=100, y=260)

        area = Label(janela4, text=filtros[0][3], font=("Times", 18), fg="gray40").place(x=240, y=292)
        Area = Label(janela4, text="Área:", font=("Times", 18, "bold"), fg="black").place(x=100, y=290)

        quartos = Label(janela4, text=filtros[0][4], font=("Times", 18), fg="gray40").place(x=240, y=322)
        Quartos = Label(janela4, text="Quartos:", font=("Times", 18, "bold"), fg="black").place(x=100, y=320)

        banheiros = Label(janela4, text=filtros[0][5], font=("Times", 18), fg="gray40").place(x=240, y=352)
        Banheiros = Label(janela4, text="Banheiros:", font=("Times", 18, "bold"), fg="black").place(x=100, y=350)

        descricao = Label(janela4, text=filtros[0][6], font=("Times", 18), fg="gray40").place(x=240, y=382)
        Descricao = Label(janela4, text="Descrição:", font=("Times", 18, "bold"), fg="black").place(x=100, y=380)

        valor = Label(janela4, text=filtros[0][8], font=("Times", 18), fg="gray40").place(x=240, y=412)
        Valor = Label(janela4, text="Valor:", font=("Times", 18, "bold"), fg="black").place(x=100, y=410)

        contato = Label(janela4, text="Para mais informações, entre em contato conosco", font=("Times", 10, "bold"),fg="black").place(x=900, y=550)
        telefone = Label(janela4, text="Telefone: (41)99948-2502", font=("Times", 10, "bold"), fg="black").place(x=915,y=575)
        email = Label(janela4, text="Email: imobiliariamzz@gmail.com", font=("Times", 10, "bold"), fg="black").place(x=910, y=600)

        #Se ainda houver mais de uma casa na matriz filtros, o usuário ainda pode clicar no batão "proximo" para aparecer a próxima casa
        if len(filtros)>1:
            proximo = Button(janela4, text="Próxima", width=18, height=2, bg="snow", command=lambda: proxima_casa(janela4)).place(x=450, y=500)
        # Se não houver mais de uma casa, printamos "Não há mais casas disponíveis"
        else:
            mensagem = Label(janela4, text="Não há mais casas disponíveis!", font=("Times", 35), fg="black").place(x=150, y=500)

#Chamada quando clicado o botão "procurar" da tela 2
def procurar (janela2, entry_bairro, entry_area, entry_quartos, entry_banheiro, entry_valor):
   global aceitadas
   global filtros
   a=0

   #O comando ".get()" pega todo o texto que foi digitado pelo usuário
   bairro = entry_bairro.get()
   area = int(entry_area.get())
   banheiros = int(entry_banheiro.get())
   valor = float(entry_valor.get())
   quartos = int(entry_quartos.get())
   #Para cada casa(linha) da matriz "aceitadas" verificaremos se as especificações condizem com as desejadas pelo usuaário
   for i in range(len(aceitadas)):
       if bairro == aceitadas[i][2]:
           if area <= aceitadas[i][3]:
               if quartos <= aceitadas[i][4]:
                   if banheiros <= aceitadas[i][5]:
                       if valor >= aceitadas[i][8]:
                           #Se todas as condições condizerem, colocamos a casa em uma matriz "filtros" na qual só há casas com os filtros selecionados
                           filtros.append(aceitadas[i])
                       else:
                           a = a + 1
                   else:
                       a = a + 1
               else:
                   a = a + 1
           else:
               a = a + 1
       else:
           a = a + 1
   #Para o caso de nenhuma casa condizer com a casa que o comprador deseja, será aberto uma nova página na qual será printado "Não possuem casas com a sua descrição!"
   if a == len(aceitadas):
       janela5 = Toplevel()
       janela5.geometry("1450x700+0+0")
       encontradas = Label(janela5, text="Não possuem casas com a sua descrição!", font=("Times", 20, "bold")).place(x=100, y=140)
   #Para o caso de haverem casas na matriz filtros
   else:
       # Abre uma nova janela
       janela4 = Toplevel(janela)
       janela4.geometry("1450x700+0+0")
       # Printa na tela a casa que condiz com o que deseja o comprador
       casa = Label(janela4, text="Casa:", font=("Times", 25, "bold"), fg="black").place(x=100, y=140)

       nome = Label(janela4, text=filtros[0][0], font=("Times", 18,), fg="gray40").place(x=240, y=202)
       Nome = Label(janela4, text="Proprietário:", font=("Times", 18, "bold"), fg="black").place(x=100, y=200)

       endereço = Label(janela4, text=filtros[0][1], font=("Times", 18), fg="gray40").place(x=240, y=232)
       Endereço = Label(janela4, text="Endereço:", font=("Times", 18, "bold"), fg="black").place(x=100, y=230)

       bairro = Label(janela4, text=filtros[0][2], font=("Times", 18), fg="gray40").place(x=240, y=262)
       Bairro = Label(janela4, text="Bairro:", font=("Times", 18, "bold"), fg="black").place(x=100, y=260)

       area = Label(janela4, text=filtros[0][3], font=("Times", 18), fg="gray40").place(x=240, y=292)
       Area = Label(janela4, text="Área:", font=("Times", 18, "bold"), fg="black").place(x=100, y=290)

       quartos = Label(janela4, text=filtros[0][4], font=("Times", 18), fg="gray40").place(x=240, y=322)
       Quartos = Label(janela4, text="Quartos:", font=("Times", 18, "bold"), fg="black").place(x=100, y=320)

       banheiros = Label(janela4, text=filtros[0][5], font=("Times", 18), fg="gray40").place(x=240, y=352)
       Banheiros = Label(janela4, text="Banheiros:", font=("Times", 18, "bold"), fg="black").place(x=100, y=350)

       descricao = Label(janela4, text=filtros[0][6], font=("Times", 18), fg="gray40").place(x=240, y=382)
       Descricao = Label(janela4, text="Descrição:", font=("Times", 18, "bold"), fg="black").place(x=100, y=380)

       valor = Label(janela4, text=filtros[0][8], font=("Times", 18), fg="gray40").place(x=240, y=412)
       Valor = Label(janela4, text="Valor:", font=("Times", 18, "bold"), fg="black").place(x=100, y=410)

       contato = Label(janela4, text="Para mais informações, entre em contato conosco", font=("Times", 10, "bold"), fg="black").place(x=900, y=550)
       telefone = Label(janela4, text="Telefone: (41)99948-2502", font=("Times", 10, "bold"), fg="black").place(x=915, y=575)
       email = Label(janela4, text="Email: imobiliariamzz@gmail.com", font=("Times", 10, "bold"), fg="black").place(x=910, y=600)

       #Se haver mais de uma casa em filtros, para saber a próxima o usuário aperta o botão "proximo"
       if len(filtros)>1:
           proximo = Button(janela4, text="Próxima", width = 18, height = 2, bg="snow", command= lambda: proxima_casa(janela4)).place(x=450, y=500)
       #Se não houver mais de uma casa, printamos "Não há mais casas disponíveis"
       else:
           mensagem = Label(janela4, text="Não há mais casas disponíveis!", font=("Times", 35), fg="black").place(x=150,y=500)

#Chamada quando clicado o botão "enviar" da tela 1
#Tem por objetivo salvar todas as informaaçoes da casa que foram escritas
def salvando(janela1, entry_nome, entry_endereço, entry_bairro, entry_area, entry_quartos, entry_banheiro,entry_descrição,  entry_email, entry_valor):
  #Variáveis global que é modificada dentro da função
  global casa
  casa=[]
  #A seguir será realizado o mesmo procedimento para todos os dados "N" dados fornecidos pelo usuário
  #O comando ".get()" pega todo o texto que foi digitado pelo usuário
  nome = entry_nome.get()
  #colocamos essa variável dentro da lista
  casa.append(nome)
  #A cada 2 linhas acontece a mesma coisa relatada acima
  endereço = entry_endereço.get()
  casa.append(endereço)
  bairro = entry_bairro.get()
  casa.append(bairro)
  area = entry_area.get()
  casa.append(area)
  quartos = entry_quartos.get()
  casa.append(quartos)
  banheiros = entry_banheiro.get()
  casa.append(banheiros)
  descrição = entry_descrição.get()
  casa.append(descrição)
  email = entry_email.get()
  casa.append(email)
  valor = entry_valor.get()
  casa.append(valor)
  #Verifica se o usuário digitou em todos os campos
  if (casa[0]!="")and(casa[1]!="")and(casa[2]!="")and(casa[3]!="")and(casa[4]!="")and(casa[5]!="")and(casa[6]!="")and(casa[7]!="")and(casa[8]!=""):
      casa[3]=int(casa[3])
      casa[4] = int(casa[4])
      casa[5] = int(casa[5])
      casa[8] = float(casa[8])

      # Colocamos a lista na matriz "casas" na qual cada linha terá a informação de uma casa
      casas.append(casa)

      # Printamos na tela avisando o usuário que sua proposta foi enviada
      analise = Label(janela1, text="Sua proposta foi enviada!", font=("Times", 25), fg="black").place(
          x=380, y=580)
      analise1 = Label(janela1, text="Aguarde a resposta da imobiliária!", font=("Times", 25), fg="black").place(
          x=380, y=650)
  #Se o usuário não digitou em algum campo
  else:
      analise2 = Label(janela1, text="Campo obrigatório não preenchido", font=("Times", 25), fg="black").place(
          x=380, y=650)

#Chamada quando clicado o botão "vender" da tela principal
#Tem por objetivo fornecer um formulário para o usuário colocar os dados de sua casa que pretende vender
def catalogo():

    #Cria uma nova janela
    janela1 = Toplevel(janela)
    janela1.geometry("1450x700+0+0")

    #Títulos da tela
    heading2 = Label(janela1, text="Primeiros passos", font=("Times", 42, "bold"), fg="black").place(
        x=450, y=100)
    heading3 = Label(janela1, text="Dados da casa:", font=("Times", 35, "bold"), fg="gray40").place(
        x=90, y=200)

    #A seguir a variável "entry_N" é o espaço para se escrever o "N" do proprietário
    # A seguir a variável "N" printa "N" na tela

    #Exemplo

    #A variável "entry_nome" é o espaço para quem deseja escrever
    #A variável "Nome" printa "Nome:" na tela
    entry_nome = Entry(janela1, width=100, bg="snow")
    entry_nome.place(x=250, y=305)
    Nome = Label(janela1, text="Nome completo:", font=("Times", 15), fg="black")
    Nome.place(x=90, y=300)

    entry_endereço = Entry(janela1, width=100, bg="snow")
    entry_endereço.place(x=250, y=330)
    Endereço = Label(janela1, text="Endereço:", font=("Times", 15), fg="black")
    Endereço.place(x=90, y=325)

    entry_bairro = Entry(janela1, width=100, bg="snow")
    entry_bairro.place(x=250, y=355)
    Bairro = Label(janela1, text="Bairro:", font=("Times", 15), fg="black")
    Bairro.place(x=90, y=350)

    entry_area = Entry(janela1, width=100, bg="snow")
    entry_area.place(x=250, y=380)
    Area = Label(janela1, text="Área (m²):", font=("Times", 15), fg="black")
    Area.place(x=90, y=375)

    entry_quartos = Entry(janela1, width=100, bg="snow")
    entry_quartos.place(x=250, y=405)
    Quartos = Label(janela1, text="Qtdde de quartos:", font=("Times", 15), fg="black")
    Quartos.place(x=90, y=400)

    entry_banheiro = Entry(janela1, width=97, bg="snow")
    entry_banheiro.place(x=270, y=430)
    Banheiro = Label(janela1, text="Qtdde de banheiros:", font=("Times", 15), fg="black")
    Banheiro.place(x=90, y=425)

    entry_descrição = Entry(janela1, width=100, bg="snow")
    entry_descrição.place(x=250, y=455)
    Descrição = Label(janela1, text="Descrição:", font=("Times", 15), fg="black")
    Descrição.place(x=90, y=450)

    entry_email = Entry(janela1, width=100, bg="snow")
    entry_email.place(x=250, y=480)
    Email = Label(janela1, text="Email:", font=("Times", 15), fg="black")
    Email.place(x=90, y=475)

    entry_valor = Entry(janela1, width=100, bg="snow")
    entry_valor.place(x=250, y=505)
    Valor = Label(janela1, text="Valor (R$):", font=("Times", 15), fg="black")
    Valor.place(x=90, y=500)

    #Botão que aparece na tela para ser pressionado para enviar todos os dados para a imobiliária
    #Chama a função "salvando"
    Enviar = Button(janela1, text="Enviar", width=18, height=2, bg="snow",
                    command=lambda: salvando(janela1, entry_nome, entry_endereço, entry_bairro, entry_area,
                                             entry_quartos, entry_banheiro, entry_descrição, entry_email, entry_valor))
    Enviar.place(x=380, y=580)

#Chamada pelo botão "comprar" da tela principal
def instrucoes():
  #Abrindo tela 2
  janela2 = Toplevel(janela)
  janela2.geometry("1450x700+0+0")
  #Printando na tela 2
  heading1 = Label(janela2, text="Casas disponíveis:", font=("Times", 42, "bold"), fg="black").place(
      x=200, y=100)
  heading2 = Label(janela2, text="Filtros:", font=("Times", 30, "bold"), fg="gray40").place(
      x=100, y=200)
  #A seguir o comprador terá a oportunidade de escolher algumas especificações que ele deseja que haja em sua casa
  #A variável "entry_N" é o espaço para se escrever o "N" do proprietário
  #A variável "N" printa "N" na tela

  #Exemplo

  # A variável "entry_bairro" é o espaço para quem deseja escrever
  # A variável "Bairro" printa "Bairro:" na tela
  entry_bairro = Entry(janela2, width=100, bg="snow")
  entry_bairro.place(x=250, y=305)
  Bairro = Label(janela2, text="Bairro:", font=("Times", 15), fg="black")
  Bairro.place(x=90, y=300)

  entry_area = Entry(janela2, width=100, bg="snow")
  entry_area.place(x=250, y=330)
  Area = Label(janela2, text="Área (m²):", font=("Times", 15), fg="black")
  Area.place(x=90, y=325)

  entry_quartos = Entry(janela2, width=100, bg="snow")
  entry_quartos.place(x=250, y=355)
  Quartos = Label(janela2, text="Qtdde de quartos:", font=("Times", 15), fg="black")
  Quartos.place(x=90, y=350)

  entry_banheiro = Entry(janela2, width=97, bg="snow")
  entry_banheiro.place(x=270, y=380)
  Banheiro = Label(janela2, text="Qtdde de banheiros:", font=("Times", 15), fg="black")
  Banheiro.place(x=90, y=375)

  entry_valor = Entry(janela2, width=100, bg="snow")
  entry_valor.place(x=250, y=405)
  Valor = Label(janela2, text="Valor (R$):", font=("Times", 15), fg="black")
  Valor.place(x=90, y=400)

  #Depois de colocar todas as especificações da casa que ele ambiciona, o comprador clicara no botão "enviar"
  Procurar = Button(janela2, text="Procurar", width=18, height=2, bg="snow", command= lambda: procurar(janela2, entry_bairro, entry_area, entry_quartos, entry_banheiro, entry_valor))
  Procurar.place(x=350, y=550)

#Chamada quando clicado no botão "funcionario" da tela principal
def propostas():
    #Abrindo uma nova janela
  janela3 = Toplevel(janela)
  janela3.geometry("1450x700+0+0")

  # Verificancdo se há propostas a serem analisadas pela imobiliária
  if len(casas)>0:
      #Printando as informaçoes da primeira casa disponível para avaliação
      Título = Label(janela3, text="Propostas em análise:", font=("Times", 42, "bold"), fg="black").place(x=350, y=80)

      casa = Label(janela3, text="Casa:", font=("Times", 25, "bold"), fg="black").place(x=100, y=160)

      nome = Label(janela3, text=casas[0][0], font=("Times", 18,), fg="gray40").place(x=240, y=202)
      Nome = Label(janela3, text="Proprietário:", font=("Times", 18, "bold"), fg="black").place(x=100, y=200)

      endereço = Label(janela3, text=casas[0][1], font=("Times", 18), fg="gray40").place(x=240, y=232)
      Endereço = Label(janela3, text="Endereço:", font=("Times", 18, "bold"), fg="black").place(x=100, y=230)

      bairro = Label(janela3, text=casas[0][2], font=("Times", 18), fg="gray40").place(x=240, y=262)
      Bairro = Label(janela3, text="Bairro:", font=("Times", 18, "bold"), fg="black").place(x=100, y=260)

      area = Label(janela3, text=casas[0][3], font=("Times", 18), fg="gray40").place(x=240, y=292)
      Area = Label(janela3, text="Área:", font=("Times", 18, "bold"), fg="black").place(x=100, y=290)

      quartos = Label(janela3, text=casas[0][4], font=("Times", 18), fg="gray40").place(x=240, y=322)
      Quartos = Label(janela3, text="Quartos:", font=("Times", 18, "bold"), fg="black").place(x=100, y=320)

      banheiros = Label(janela3, text=casas[0][5], font=("Times", 18), fg="gray40").place(x=240, y=352)
      Banheiros = Label(janela3, text="Banheiros:", font=("Times", 18, "bold"), fg="black").place(x=100, y=350)

      descricao = Label(janela3, text=casas[0][6], font=("Times", 18), fg="gray40").place(x=240, y=382)
      Descricao = Label(janela3, text="Descrição:", font=("Times", 18, "bold"), fg="black").place(x=100, y=380)

      valor = Label(janela3, text=casas[0][8], font=("Times", 18), fg="gray40").place(x=240, y=412)
      Valor = Label(janela3, text="Valor:", font=("Times", 18, "bold"), fg="black").place(x=100, y=410)

      #Botão "Aceitar" que deverá ser utilizado caso o funcionário queira aceitar a proposta do proprietário
      #Tal botão chama a função "aceitar"
      Aceitar = Button(janela3, text="Aceitar", width=18, height=2, bg="snow", command=lambda: aceitar(janela3)).place(x=200, y=550)

      # Botão "Negar" que deverá ser utilizado caso o funcionário queira negar a proposta do proprietário
      #Tal botão chama a função "negar"
      Negar = Button(janela3, text="Negar", width=18, height=2, bg="snow", command=lambda: negar(janela3)).place(x=400, y=550)

  #Se não houver casas disponíveis para avaliação é printado "Não há casas a avaliar"
  else:
      Acabou = Label(janela3, text="Não há casas a avaliar.", font=("Times", 35, "bold"), fg="black").place(x=400, y=350)

#Chamada quando clicado o botão "aceitar" da tela 3
def aceitar(janela3):
  global casas
  global aceitadas
  #A casa aceitada é colocada na matriz que contém todas as casas aceitas
  aceitadas.append(casas[0])
  #Deleta tal casa da matriz casas para que haja uma nova casa na posição 0 da matriz a ser analisada pelo funcionário
  del(casas[0])
  #Fechando a tela 3
  janela3.destroy()
  janela3 = Toplevel(janela)
  janela3.geometry("1450x700+0+0")

      #Verificancdo se há propostas a serem analisadas pela imobiliária
  if len(casas) > 0:
     # Printando as informaçoes da casa disponível para avaliação
     Título = Label(janela3, text="Propostas em análise:", font=("Times", 42, "bold"), fg="black").place(x=350,
                                                                                                              y=80)

     casa = Label(janela3, text="Casa:", font=("Times", 25, "bold"), fg="black").place(x=100, y=160)

     nome = Label(janela3, text=casas[0][0], font=("Times", 18,), fg="gray40").place(x=240, y=202)
     Nome = Label(janela3, text="Proprietário:", font=("Times", 18, "bold"), fg="black").place(x=100, y=200)

     endereço = Label(janela3, text=casas[0][1], font=("Times", 18), fg="gray40").place(x=240, y=232)
     Endereço = Label(janela3, text="Endereço:", font=("Times", 18, "bold"), fg="black").place(x=100, y=230)

     bairro = Label(janela3, text=casas[0][2], font=("Times", 18), fg="gray40").place(x=240, y=262)
     Bairro = Label(janela3, text="Bairro:", font=("Times", 18, "bold"), fg="black").place(x=100, y=260)

     area = Label(janela3, text=casas[0][3], font=("Times", 18), fg="gray40").place(x=240, y=292)
     Area = Label(janela3, text="Área:", font=("Times", 18, "bold"), fg="black").place(x=100, y=290)

     quartos = Label(janela3, text=casas[0][4], font=("Times", 18), fg="gray40").place(x=240, y=322)
     Quartos = Label(janela3, text="Quartos:", font=("Times", 18, "bold"), fg="black").place(x=100, y=320)

     banheiros = Label(janela3, text=casas[0][5], font=("Times", 18), fg="gray40").place(x=240, y=352)
     Banheiros = Label(janela3, text="Banheiros:", font=("Times", 18, "bold"), fg="black").place(x=100, y=350)

     descricao = Label(janela3, text=casas[0][6], font=("Times", 18), fg="gray40").place(x=240, y=382)
     Descricao = Label(janela3, text="Descrição:", font=("Times", 18, "bold"), fg="black").place(x=100, y=380)

     valor = Label(janela3, text=casas[0][8], font=("Times", 18), fg="gray40").place(x=240, y=412)
     Valor = Label(janela3, text="Valor:", font=("Times", 18, "bold"), fg="black").place(x=100, y=410)

     # Botão "Aceitar" que deverá ser utilizado caso o funcionário queira aceitar a proposta do proprietário
     # Tal botão chama a função "aceitar"
     Aceitar = Button(janela3, text="Aceitar", width=18, height=2, bg="snow",
                           command=lambda: aceitar(janela3)).place(x=200, y=550)

     # Botão "Negar" que deverá ser utilizado caso o funcionário queira negar a proposta do proprietário
     # Tal botão chama a função "negar"
     Negar = Button(janela3, text="Negar", width=18, height=2, bg="snow", command=lambda: negar(janela3)).place(
              x=400, y=550)
  # Se não houver casas disponíveis para avaliação é printado "Não há casas a avaliar"
  else:
     Acabou = Label(janela3, text="Não há casas a avaliar.", font=("Times", 35, "bold"), fg="black").place(x=400, y=350)

#Chamada quando clicado o botão "negar" da tela 3
def negar(janela3):
  global casas
  # Deleta tal casa da matriz casas para que haja uma nova casa na posição 0 da matriz a ser analisada pelo funcionário
  del(casas[0])
  #Fechando a tela 3
  janela3.destroy()
  janela3 = Toplevel(janela)
  janela3.geometry("1450x700+0+0")

      #Verificancdo se há propostas a serem analisadas pela imobiliária
  if len(casas) > 0:
     # Printando as informaçoes da primeira casa disponível para avaliação
     Título = Label(janela3, text="Propostas em análise:", font=("Times", 42, "bold"), fg="black").place(x=350,
                                                                                                              y=80)

     casa = Label(janela3, text="Casa:", font=("Times", 25, "bold"), fg="black").place(x=100, y=160)

     nome = Label(janela3, text=casas[0][0], font=("Times", 18,), fg="gray40").place(x=240, y=202)
     Nome = Label(janela3, text="Proprietário:", font=("Times", 18, "bold"), fg="black").place(x=100, y=200)

     endereço = Label(janela3, text=casas[0][1], font=("Times", 18), fg="gray40").place(x=240, y=232)
     Endereço = Label(janela3, text="Endereço:", font=("Times", 18, "bold"), fg="black").place(x=100, y=230)

     bairro = Label(janela3, text=casas[0][2], font=("Times", 18), fg="gray40").place(x=240, y=262)
     Bairro = Label(janela3, text="Bairro:", font=("Times", 18, "bold"), fg="black").place(x=100, y=260)

     area = Label(janela3, text=casas[0][3], font=("Times", 18), fg="gray40").place(x=240, y=292)
     Area = Label(janela3, text="Área:", font=("Times", 18, "bold"), fg="black").place(x=100, y=290)

     quartos = Label(janela3, text=casas[0][4], font=("Times", 18), fg="gray40").place(x=240, y=322)
     Quartos = Label(janela3, text="Quartos:", font=("Times", 18, "bold"), fg="black").place(x=100, y=320)

     banheiros = Label(janela3, text=casas[0][5], font=("Times", 18), fg="gray40").place(x=240, y=352)
     Banheiros = Label(janela3, text="Banheiros:", font=("Times", 18, "bold"), fg="black").place(x=100, y=350)

     descricao = Label(janela3, text=casas[0][6], font=("Times", 18), fg="gray40").place(x=240, y=382)
     Descricao = Label(janela3, text="Descrição:", font=("Times", 18, "bold"), fg="black").place(x=100, y=380)

     valor = Label(janela3, text=casas[0][8], font=("Times", 18), fg="gray40").place(x=240, y=412)
     Valor = Label(janela3, text="Valor:", font=("Times", 18, "bold"), fg="black").place(x=100, y=410)

     # Botão "Aceitar" que deverá ser utilizado caso o funcionário queira aceitar a proposta do proprietário
     # Tal botão chama a função "aceitar"
     Aceitar = Button(janela3, text="Aceitar", width=18, height=2, bg="snow",
                           command=lambda: aceitar(janela3)).place(x=200, y=550)

     # Botão "Negar" que deverá ser utilizado caso o funcionário queira negar a proposta do proprietário
     # Tal botão chama a função "negar"
     Negar = Button(janela3, text="Negar", width=18, height=2, bg="snow", command=lambda: negar(janela3)).place(
              x=400, y=550)
  # Se não houver casas disponíveis para avaliação é printado "Não há casas a avaliar"
  else:
     Acabou = Label(janela3, text="Não há casas a avaliar.", font=("Times", 35, "bold"), fg="black").place(x=400, y=350)

#Botões que aparecem na tela principal
   #Abre a tela 1 chamando a função "catalogo"
Vender = Button(janela, text="Vender", width = 18, height = 2, bg="snow", command=catalogo).place(x=400, y=350)
   #Abre a tela 2 chamando a função "instruçoes"
Comprar = Button(janela, text="Comprar", width = 18, height = 2, bg="snow", command=instrucoes).place(x=750, y=350)
   #Abre a tela 3 chamando a funçao "propostas"
Funcionario = Button(janela, text="Você é funcionário?", width =18, height = 2, bg = "snow", command=propostas).place(x=1200, y = 650)


janela.mainloop()