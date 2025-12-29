import sqlite3
# Isso importa o banco de dados no Python.

#Agora vamos criar o banco:

conexao = sqlite3.connect("usuarios.db")

# Criando uma tabela (onde os dados ficam)

# Agora precisamos dizer como os dados serão guardados

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")

conexao.commit()

# usuarios → nome da tabela

# id → número automático

# nome → texto

# idade → número

# Recebendo dados do usuário
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

# Salvando os dados no banco

cursor.execute(
"insert into usuarios (nome, idade) values (?, ?)",
(nome,idade)
)

conexao.commit()

# Mostrando os dados cadastrados

cursor.execute("select * from usuarios")
usuarios = cursor.fetchall()

print("\nUsuarios cadastrados:")

for usuario in usuarios:
    print(usuario)

# fechar a conexao

conexao.close()


