from shelve import open
db= open('shelve.db')
x=["NOME","CÓDIGO","MARCA","IMPLEMENTO","TIPO"]
db['lista']=[x]
print(db['lista'])