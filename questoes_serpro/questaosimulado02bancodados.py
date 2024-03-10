import sqlite3

conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        ID INT PRIMARY KEY, 
        Nome TEXT,
        Idade INT,
    )
''')

conexao.commit()

conexao.close()
