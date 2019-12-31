#Importando as bibliotecas
from tkinter import*
from PIL import ImageTk, Image
import tkinter as tk

#Criando função associada ao primeiro botão
def create_window1():
    #Salvando em uma variável o que foi fornecido pelo usuário na entry_box

    global entry_box
    box = entry_box.get()
    
    #Criando uma nova interface
    window = Toplevel(root)
    window.geometry("1500x780+0+0")
    window.configure(bg="white smoke")
    window.title("New Application")
    
    #Inserindo uma frase na interface
    label_saud = Label(window, text="Oi {}, que bom ter você aqui! Escolha algumas opções para escolhermos alguns looks para você:".format(box),font=("arial", 17, "bold"), fg="white", bg="cadet blue").place(x=100, y=100)

   
    #Inserindo botões na interface, que serão utilizados na escolha de gênero 
    bottom_homem = Button(window, text="HOMEM", font=("arial", 30, "bold"),
                width =8, height=2, bg="lightblue", command=apos_homem).place(x=1000, y=300)

    bottom_mulher = Button(window, text="MULHER", font=("arial", 30, "bold"),
                width =8, height=2, bg="lightblue", command=apos_mulher).place(x=100, y=300)
    
    #Colocando imagens na interface
    back = Label(window)
    back.la = PhotoImage(file = 'perfeita.png')
    back['image'] = back.la
    back.place(x=400,y=200)
        
    

#Criando uma nova interface para ser mostrada se o usuário clicar em "mulher"  
def apos_mulher():
    #Criando uma nova interface
    window2 = Toplevel(root)
    window2.title("New Application")
    window2.geometry("1500x780+0+0")
    window2.configure(bg="white smoke")

    #Adicionando um background a interface
    back = Label(window2)
    back.la = PhotoImage(file = '3k.png')
    back['image'] = back.la
    back.place(x=0,y=0)


    #Adicionando um texto na interface
    label_escolha = Label(window2, text="Escolha um clima:",font=("arial", 30), fg="snow", bg="black").place(x=550, y=170)

    #Colocando botões nessa janela que possibilita o usuário escolher o tipo de clima
    bottom_quente= Button(window2, text="QUENTE/NORMAL", font=("arial", 30, "bold"),
                width = 30, height=2, bg="turquoise4", fg="snow" ,command=mulher_quente).place(x=350, y=300)

    bottom_frio = Button(window2, text="NORMAL/FRIO", font=("arial", 30, "bold"),
                width = 30, height=2, bg="lightblue", fg="black", command=mulher_frio).place(x=350, y=500)

    
#Função criada para ser acionada se o usuário clicar no clima quente      
def mulher_quente():
    #Criando uma nova interface
    window3 = Toplevel(root)
    window3.title("New Application")
    window3.geometry("1500x780+0+0")
    window3.configure(bg="cadet blue")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window3)
    back.la = PhotoImage(file = 'bckg.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Adicionando textos na interface
    heading = Label(window3, text="Escolha uma ocasião:", font=("italic", 30, "bold"), fg="snow", bg="cadet blue").place(x=500, y=100)

    #Colocando botões na interface que possibilitarão o usuário escolher entre a ocasião casual ou social
    bottom_o1= Button(window3, text="C a s u a l", font=("arial", 20, "bold"), fg="snow",
                width = 20, height=2, bg="black", command=mulher_quente_casual).place(x=530, y=250)
    
    bottom_o2= Button(window3, text="S o c i a l", font=("arial", 20, "bold"),fg="snow",
                width = 20, height=2, bg="black", command=mulher_quente_social).place(x=530, y=450)
    

#Função criada para ser acionada se o usuário clicar na ocasião social    
def mulher_quente_social():
    #Criando uma nova interface
    window4 = Toplevel(root)
    window4.geometry("1500x780+0+0")
    window4.title("New Application")
    window4.configure(bg="white")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window4)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Inserindo uma frase na interface
    heading = Label(window4, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window4, text="Você está em um clima médio para quente e quer uma roupa social.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)


    #Inserindo imagens na interface
    back = Label(window4)
    back.la = PhotoImage(file = 'mqs1.png')
    back['image'] = back.la
    back.place(x=150,y=200)

    back = Label(window4)
    back.la = PhotoImage(file = 'mqs2.png')
    back['image'] = back.la
    back.place(x=750,y=200)

   
#Função criada para ser acionada se o usuário clicar na ocasião casual    
def mulher_quente_casual():
    #Criando uma nova interface
    window4 = Toplevel(root)
    window4.geometry("1500x780+0+0")
    window4.configure(bg="white")
    window4.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window4)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Inserindo uma frase na interface
    heading = Label(window4, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window4, text="Você está em um clima médio para quente e quer uma roupa casual.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)

    #Inserindo imagens na interface
    back = Label(window4)
    back.la = PhotoImage(file = 'mqc1.png')
    back['image'] = back.la
    back.place(x=150,y=250)

    back = Label(window4)
    back.la = PhotoImage(file = 'mqc2.png')
    back['image'] = back.la
    back.place(x=750,y=200)
    

#Função criada para ser acionada se o usuário clicar no clima frio
def mulher_frio():
    #Criando uma nova interface
    window3 = Toplevel(root)
    window3.geometry("1500x780+0+0")
    window3.configure(bg="cadet blue")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window3)
    back.la = PhotoImage(file = 'bckg.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Adicionando textos na interface
    heading = Label(window3, text="Escolha uma ocasião:", font=("italic", 30, "bold"), fg="snow", bg="cadet blue").place(x=500, y=100)

    #Colocando botões na interface que possibilitarão o usuário escolher entre a ocasião casual ou social
    bottom_o1= Button(window3, text="C a s u a l", font=("arial", 20, "bold"), fg="snow",
                width = 20, height=2, bg="black", command=mulher_frio_casual).place(x=530, y=250)
    
    bottom_o2= Button(window3, text="S o c i a l", font=("arial", 20, "bold"),fg="snow",
                width = 20, height=2, bg="black", command=mulher_frio_social).place(x=530, y=450)

    
#Função criada para ser acionada se o usuário clicar na ocasião social 
def mulher_frio_social():
    #Criando uma nova interface
    window4 = Toplevel(root)
    window4.geometry("1500x780+0+0")
    window4.configure(bg="white")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window4)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)

    #Inserindo uma frase na interface
    heading = Label(window4, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window4, text="Você está em um clima médio para frio e quer uma roupa social.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)


    #Inserindo imagens na interface
    back = Label(window4)
    back.la = PhotoImage(file = 'mfs1.png')
    back['image'] = back.la
    back.place(x=200,y=300)

    back = Label(window4)
    back.la = PhotoImage(file = 'mfs2.png')
    back['image'] = back.la
    back.place(x=700,y=300)
    
#Função criada para ser acionada se o usuário clicar na ocasião casual
def mulher_frio_casual():
    #Criando uma nova interface
    window5 = Toplevel(root)
    window5.geometry("1500x780+0+0")
    window5.configure(bg="white")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window5)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)

    #Inserindo uma frase na interface
    heading = Label(window5, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window5, text="Você está em um clima médio para frio e quer uma roupa casual.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)

    #Inserindo imagens na interface
    back = Label(window5)
    back.la = PhotoImage(file = 'mfc1.png')
    back['image'] = back.la
    back.place(x=200,y=320)

    
    back = Label(window5)
    back.la = PhotoImage(file = 'mfc2.png')
    back['image'] = back.la
    back.place(x=700,y=300)



#Criando uma nova interface para ser mostrada se o usuário clicar em "homem"   
def apos_homem():
    #Criando uma nova interface
    window2 = Toplevel(root)
    window2.geometry("1500x780+0+0")
    window2.configure(bg="white smoke")

    #Adicionando um background a interface
    back = Label(window2)
    back.la = PhotoImage(file = '3k.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Inserindo uma frase na interface
    label_escolha = Label(window2, text="Escolha um clima:",font=("arial", 30), fg="snow", bg="gray").place(x=550, y=170)

    #Inserindo botões na interface, que serão utilizados na escolha de clima
    bottom_quente= Button(window2, text="QUENTE/NORMAL", font=("arial", 30, "bold"),
                width = 30, height=2, bg="turquoise4", fg="snow" ,command=homem_quente).place(x=350, y=300)

    bottom_frio = Button(window2, text="NORMAL/FRIO", font=("arial", 30, "bold"),
                width = 30, height=2, bg="lightblue", fg="black", command=homem_frio).place(x=350, y=500)


#Função criada para ser acionada se o usuário clicar no clima quente
def homem_quente():
    #Criando uma nova interface
    window3 = Toplevel(root)
    window3.geometry("1500x780+0+0")
    window3.configure(bg="cadet blue")
    window3.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window3)
    back.la = PhotoImage(file = 'bckg.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Adicionando textos na interface
    heading = Label(window3, text="Escolha uma ocasião:", font=("italic", 30, "bold"), fg="snow", bg="cadet blue").place(x=500, y=100)

    #Colocando botões na interface que possibilitarão o usuário escolher entre a ocasião casual ou social
    bottom_o1= Button(window3, text="C a s u a l", font=("arial", 20, "bold"), fg="snow",
                width = 20, height=2, bg="black", command=homem_quente_casual).place(x=530, y=250)
    
    bottom_o2= Button(window3, text="S o c i a l", font=("arial", 20, "bold"),fg="snow",
                width = 20, height=2, bg="black", command=homem_quente_social).place(x=530, y=450)


#Função criada para ser acionada se o usuário clicar na ocasião social
def homem_quente_social():
    #Criando uma nova interface
    window6 = Toplevel(root)
    window6.geometry("1500x780+0+0")
    window6.configure(bg="white")
    window6.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window6)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)

    #Inserindo uma frase na interface
    heading = Label(window6, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window6, text="Você está em um clima médio para quente e quer uma roupa social.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)


    #Inserindo imagens na interface
    back = Label(window6)
    back.la = PhotoImage(file = 'hqs1.png')
    back['image'] = back.la
    back.place(x=160,y=200)

    
    back = Label(window6)
    back.la = PhotoImage(file = 'hqs2.png')
    back['image'] = back.la
    back.place(x=740,y=270)

#Função criada para ser acionada se o usuário clicar na ocasião casual
def homem_quente_casual():
    #Criando uma nova interface
    window7 = Toplevel(root)
    window7.geometry("1500x780+0+0")
    window7.configure(bg="white")
    window7.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window7)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Inserindo uma frase na interface
    heading = Label(window7, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window7, text="Você está em um clima médio para quente e quer uma roupa casual.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)

    #Inserindo imagens na interface
    back = Label(window7)
    back.la = PhotoImage(file = 'hqc1.png')
    back['image'] = back.la
    back.place(x=200,y=200)

    back = Label(window7)
    back.la = PhotoImage(file = 'hqc2.png')
    back['image'] = back.la
    back.place(x=750,y=200)


#Função criada para ser acionada se o usuário clicar no clima frio  
def homem_frio():
    #Criando uma nova interface
    window3 = Toplevel(root)
    window3.geometry("1500x780+0+0")
    window3.configure(bg="cadet blue")
    window3.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window3)
    back.la = PhotoImage(file = 'bckg.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    
    #Adicionando textos na interface
    heading = Label(window3, text="Escolha uma ocasião:", font=("italic", 30, "bold"), fg="snow", bg="cadet blue").place(x=500, y=100)

    #Colocando botões na interface que possibilitarão o usuário escolher entre a ocasião casual ou social
    bottom_o1= Button(window3, text="C a s u a l", font=("arial", 20, "bold"), fg="snow",
                width = 20, height=2, bg="black", command=homem_frio_casual).place(x=530, y=250)
    
    bottom_o2= Button(window3, text="S o c i a l", font=("arial", 20, "bold"),fg="snow",
                width = 20, height=2, bg="black", command=homem_frio_social).place(x=530, y=450)


#Função criada para ser acionada se o usuário clicar na ocasião casual
def homem_frio_casual():
    #Criando uma nova interface
    window8 = Toplevel(root)
    window8.geometry("1500x780+0+0")
    window8.configure(bg="white")
    window8.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window8)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)


    #Inserindo uma frase na interface
    heading = Label(window8, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window8, text="Você está em um clima médio para frio e quer uma roupa casual.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)

    #Inserindo imagens na interface
    back = Label(window8)
    back.la = PhotoImage(file = 'hfc1.png')
    back['image'] = back.la
    back.place(x=200,y=290)


    back = Label(window8)
    back.la = PhotoImage(file = 'hfc2.png')
    back['image'] = back.la
    back.place(x=700,y=200)
    
#Função criada para ser acionada se o usuário clicar na ocasião social   
def homem_frio_social():
    #Criando uma nova interface
    window9 = Toplevel(root)
    window9.geometry("1500x780+0+0")
    window9.configure(bg="white")
    window9.title("New Application")

    #Inserindo uma imagem que servirá de background para a interface final
    back = Label(window9)
    back.la = PhotoImage(file = 'novaback.png')
    back['image'] = back.la
    back.place(x=0,y=0)
    

    #Inserindo uma frase na interface
    heading = Label(window9, text="Selecionamos alguns looks para você:", font=("italic", 30), fg="white", bg="SkyBlue3").place(x=350, y=30)
    heading2 = Label(window9, text="Você está em um clima médio para frio e quer uma roupa social.", font=("italic", 20), fg="white", bg="SkyBlue3").place(x=250, y=100)


    #Inserindo imagens na interface 
    back = Label(window9)
    back.la = PhotoImage(file = 'hfs1.png')
    back['image'] = back.la
    back.place(x=180,y=250)

    back = Label(window9)
    back.la = PhotoImage(file = 'hfs2.png')
    back['image'] = back.la
    back.place(x=680,y=250)



#Criando uma nova janela com a instância de TK
root = Tk()
root.title("New Application")
root.geometry("1500x780+0+0")
root.configure(background="grey")

#Criando uma repartição para a janela
top = Frame(root, width=1520, height=100, bg = "gray80", bd=3, relief="raise")
top.pack(side=TOP)

#Criando uma repartição na janela para a inserção de imagem
canv = Canvas(root, width=1520, height=680)
canv.pack(side=BOTTOM)

#Inserindo imagem na repartição criada
img = ImageTk.PhotoImage(Image.open("semser.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=NW, image=img)

#Colocando frases na janela
heading = Label(top, text="Olá, bem-vindo ao seu Closet Virtual", font=("italic", 40),bg="gray80", fg="gray21").place(x=220, y=25)
label_inicio = Label(root, text="Antes de começar, por favor, digite o seu nome: ", font=("arial", 17), fg="gray21", bg="light blue").place(x=430, y=300)

#Inserindo uma caixa de entrada de dados
entry_box = Entry(root, width=20, font=("italic", 17) ,bg="white")
entry_box.place(x=540, y=400)

#Inserindo botão e colocando uma função como comando 
bottom = Button(root, text="START", font=("arial", 30, "bold"), fg="gray21",
                width = 10, height=2, bg="lightblue", command=create_window1).place(x=550, y=500)


root.mainloop()
