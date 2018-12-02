# -*- coding: utf-8 -*-
import pandas as pd
import tkinter as tk
from tkinter import *

# Comandos para configuração da telas
root = Tk()  # Comandos principa
text = tk.Text()


def tela_inicial():
    root.resizable(0, 0)  # Edita o tamanho da tel

   # Leitura e "print" da tabela externa
    tabela = pd.read_table('Preco.csv', sep=",")
    text.insert(tk.END, str(tabela))
    text.config(state='disabled')
    text.pack()


def segunda_tela():
    master = Tk()  # Abre a tela
    Label(master, text="Salvar alterações feitas").grid(row=1,)
    master.title("Encerrar edição")  # Dá nome a tela
    Button(master, text='Encerrar', fg="blue", command=quit).grid(
        row=2, column=1, sticky=W, pady=4)

    # Edita a tabela
    tabela = pd.read_table('Preco.csv', sep=",")
    text.insert(tk.END, str(tabela))
    text.config(state='normal')
    text.pack()


def login():
    master = Tk()  # Abre a tela
    master.title("Acesso")  # Dá nome a tela

    # Escrita na tela
    Label(master, text="Login: ").grid(row=0)
    Label(master, text="Senha: ").grid(row=1)

    # Entradas
    login = Entry(master)
    senha = Entry(master, show="*")

    # Telinha branca
    login.grid(row=0, column=1)
    senha.grid(row=1, column=1)

    Button(master, text='Entrar', fg="blue", command=lambda: confere_salva(
        senha.get(), login.get())).grid(row=3, column=1, sticky=W, pady=4)


def encriptar(senha):
    cipher = ''
    for char in senha:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + 14 - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + 14 - 97) % 26 + 97)
    return cipher


def confere_salva(senha, login):
    segunda_tela()

    master = Tk()  # Abre a tela
    entradas.append(login)  # Colocar os logins na lista externa

    # Abre o arquivo com o código para comparação com a senha
    with open('Codigo', 'r') as c:
        codigo = c.read()
        # Verifica a senha codificada
        if str(codigo) == encriptar(senha):
            segunda_tela()
        else:
            master.title("Ops!")
            master.resizable(0, 0)  # Edita o tamanho da tela
            Label(master, text="Tente novamente").grid(row=0, column=1)

    # Salvando os logins
    with open('Usuário.txt', 'a', encoding='utf-8') as f:
        f.write("Login: ")
        f.write(login)
        f.write(" - ")
        f.write("Senha: ")
        f.write(senha)
        f.write("//")


# Programa principal

# Abrir tela
root.geometry("600x500")
root.title("Centro Acadêmico de Matemática")
root.resizable(0, 0)  # Edita o tamanho da tela
root.configure()

# Iniciar o programa
tela_inicial()
entradas = []  # lista para salvar os logins
entrar = tk.Button(root, text="Entar", fg="blue", command=login)
entrar.pack()
root.mainloop()
