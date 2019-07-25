from tkinter import *
from datetime import datetime
import tkinter.ttk as ttk
import sqlite3

class janela():
	#Janela
	win = Tk()
	win.title("AgropopsOS 2.0.0")
	win.configure(background = "khaki1")


	#Aqui ficam as variaveis, por isso o "Var"
	nome = StringVar()
	quant = StringVar()
	preco = StringVar()


	#Texto 
	label_nome = Label(win , text = "Nome:" , bg = "khaki1" , fg = "black" , font = "Arial 12")
	label_quantidade = Label(win , text = "Quantidade:" , bg = "khaki1" , fg = "black" , font = "Arial 12")
	label_preco = Label(win , text = "Preço unitário:" , bg = "khaki1" , fg = "black" , font = "Arial 12")
	label_hora = Label(win , text = datetime.now() , bg = "khaki1" , fg = "black" , font = "Arial 8")
	label_marca = Label(win , text = "AgropopsOS®" , bg = "khaki1" , fg = "black", font = "Arial 7")


	#Caixa de entrada
	entnome = Entry(win , width = 20 , bg = "white" , textvariable = nome)
	entquant = Entry(win , width = 20 , bg = "white" , textvariable = quant)
	entpreco = Entry(win , width = 20 , bg = "white" , textvariable = preco)


	#botao
	botao_adicionar = Button(win , width = 20 , bg = "gray" , fg = "white" , text = "Adicionar")
	botao_atualizar = Button(win , width = 20 , bg = "gray" , fg = "white" , text = "Atualizar selecionado")
	botao_fechar = Button(win , width = 20 , bg = "red" , fg = "white" , text = "Fechar")
	botao_deletar = Button(win , width = 20 , bg = "gray" , fg = "white" , text = "Deletar selecionado")
	botao_visualizar = Button(win , width = 20, bg = "gray" , fg = "white" , text = "Ver lista")
	botao_pesquisar = Button(win , width = 20, bg = "gray" , fg = "white" , text = "Pesquisar")

	#Lista
	lista = Listbox(win , width = 100 , font = "Calibri 12" , selectmode = EXTENDED)
	scroll_lista = Scrollbar(win)
	scroll_listax = Scrollbar(win , width = 17)

	#Posicionamento dos elementos na grade 
	label_nome.grid(row = 0 , column = 0 , sticky = W)
	label_quantidade.grid(row = 1 , column = 0 , sticky = W)
	label_preco.grid(row = 2 , column = 0)
	entnome.grid(row = 0 , column = 1 , padx = 50)
	entquant.grid(row = 1 , column = 1)
	entpreco.grid(row = 2 , column = 1)
	lista.grid(row = 0 , column = 2 , rowspan = 10 , sticky = NS)
	scroll_lista.grid(row = 0 , column = 6 , rowspan = 10 , sticky = NS)
	scroll_listax.grid(row = 10 , column = 2 , sticky = EW)
	botao_adicionar.grid(row = 4 , column = 0 , columnspan = 2)
	botao_atualizar.grid(row = 5 , column = 0 , columnspan = 2)
	botao_pesquisar.grid(row = 6 , column = 0 , columnspan = 2)
	botao_visualizar.grid(row = 7 , column = 0 , columnspan = 2)
	botao_deletar.grid(row = 8 , column = 0 , columnspan = 2)
	botao_fechar.grid(row = 9 , column = 0 , columnspan = 2)
	label_marca.grid(row = 10 , column = 0 , sticky = W)

	#	Scroll
	lista.configure(yscrollcommand = scroll_lista.set)
	lista.configure(xscrollcommand = scroll_listax.set)
	scroll_lista.configure(command = lista.yview)
	scroll_listax.configure(command = lista.xview , orient = HORIZONTAL)



































	def run(self):
		
		janela.win.mainloop()