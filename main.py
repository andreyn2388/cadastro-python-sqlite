import sqlite3

#  Conexão com o banco de dados
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# 2️ Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")
conexao.commit()

#  Entrada de dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#  Inserção dos dados no banco
cursor.execute(
    "INSERT INTO usuarios (nome, idade) VALUES (?, ?)",
    (nome, idade)
)
conexao.commit()

#  Consulta dos dados
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

#  Exibição dos dados
print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Idade: {usuario[2]}")

#  Fechamento da conexão
conexao.close()



