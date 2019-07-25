from win import *
import comandos as com
from datetime import date


geral = janela()


def comando_visualizar():
    linhas = com.visualizar()
    geral.lista.delete(0, END)
    for i in linhas:
        geral.lista.insert(END, i)


def comando_pesquisar():
    geral.lista.delete(0, END)
    linhas = com.pesquisar(
        geral.nome.get(), geral.quant.get(), geral.preco.get())
    for i in linhas:
        geral.lista.insert(END, i)


def comando_adicionar():
    custo_total = float(geral.preco.get()) * float(geral.quant.get())

    com.adicionar("  PRODUTO:  ", geral.nome.get(), "  QUANTIDADE:  ", geral.quant.get(
    ), "  CUSTO TOTAL:  ", custo_total, "  DATA DE ENTRADA:  ", date.today())
    comando_visualizar()


def selecionar_produto(event):
    global selected
    index = geral.lista.curselection()[0]
    selected = geral.lista.get(index)
    geral.entnome.delete(0, END)
    geral.entnome.insert(END, selected[2])  # posição 0 é a INTEGER KEY
    geral.entquant.delete(0, END)
    geral.entquant.insert(END, selected[4])
    geral.entpreco.delete(0, END)
    geral.entpreco.insert(END, selected[6])


# conexão do evento com a list
geral.lista.bind('<<ListboxSelect>>', selecionar_produto)


def comando_atualizar():
    codigo = selected[0]
    custo_total = float(geral.preco.get()) * float(geral.quant.get())

    custo_atual = float(selected[6])
    quant_nova = float(geral.quant.get())
    quant_atual = float(selected[4])
    com.atualizar(codigo, geral.nome.get(), quant_nova +
                  quant_atual, custo_atual + custo_total, date.today())

    comando_visualizar()


def comando_deletar():
    codigo = selected[0]
    com.deletar(codigo)
    comando_visualizar()


geral.botao_visualizar.configure(command=comando_visualizar)
geral.botao_pesquisar.configure(command=comando_pesquisar)
geral.botao_adicionar.configure(command=comando_adicionar)
geral.botao_atualizar.configure(command=comando_atualizar)
geral.botao_deletar.configure(command=comando_deletar)
geral.botao_fechar.configure(command=geral.win.destroy)

com.iniciar()
geral.run()
