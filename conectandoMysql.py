# CRUD
import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'root',
    database= 'aulaPython',
)

# Para executar essa conexão precisa de um cursor
cursor = conexao.cursor()
# Cursor é o cara que vai executar os comandos da conexão
#CREATE
nmProduto = "Todynho"
preco = 2.50
comando = f'INSERT INTO vendas(nmProduto, preco) VALUES ("{nmProduto}", "{preco}")'
cursor.execute(comando)
conexao.commit() # Edita o banco de dados -> INSERT
#READ
#UPDATE
#DELETE

cursor.close()
conexao.close()