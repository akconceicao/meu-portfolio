import sqlite3

conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

dados = [
    (1, 'Joao', 28),
    (2, 'Maria', 25),
    (3, 'Pedro', 30),
    (4, 'Alberto', 35),
    (5, 'Kely', 33)
]

# Criando a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT PRIMARY KEY,
        nome TEXT,
        idade INT
    )
''')

# Inserindo os dados na tabela
cursor.executemany('''
    INSERT OR REPLACE INTO usuarios (id, nome, idade) 
    VALUES (?, ?, ?)
''', dados)

# Confirmar a operação
conexao.commit()

# Fechar a conexão
conexao.close()

print("Dados inseridos com sucesso.")
