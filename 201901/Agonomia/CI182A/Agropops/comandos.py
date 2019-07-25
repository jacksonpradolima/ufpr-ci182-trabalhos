import sqlite3
from datetime import datetime
db = "banco.db"
#Conexão principal e criação da tabela

def iniciar():
	conn = sqlite3.connect(db)
	cur  = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS estoque(codigo INTEGER PRIMARY KEY, txtproduto TEXT, produto TEXT, txtquant TEXT, quant REAL, txtpreco TEXT, preco REAL, txthora TEXT, hora REAL)")
	
	conn.commit()
	conn.close()

def adicionar(txtproduto, produto, txtquant, quant, txtpreco, preco, txthora, hora):
	
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("INSERT INTO estoque VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)" , (txtproduto, produto, txtquant, quant, txtpreco, preco, txthora, hora))
	
	conn.commit()
	conn.close()



def deletar(codigo):
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("DELETE FROM estoque WHERE codigo = ?", (codigo,))
	
	conn.commit()
	conn.close()

def pesquisar(produto = "", quant = "", preco = ""):
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("SELECT * FROM estoque WHERE produto = ? or quant = ? or preco = ?", (produto, quant, preco))
	linhas = cur.fetchall()
	
	conn.commit()
	conn.close()

	return linhas

def atualizar(codigo, produto, quant, preco, hora):
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("UPDATE estoque SET produto = ?, quant = ?, preco = ?, hora = ? WHERE codigo = ?", (produto, quant, preco, hora, codigo))
	
	conn.commit()
	conn.close()

def visualizar():
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	cur.execute("SELECT * FROM estoque")
	linhas = cur.fetchall()
	
	
	conn.commit()
	conn.close()
	
	return linhas









