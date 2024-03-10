import sqlite3

# Conectando ao banco de dados

conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

# Atualizar a idade de Maria para 26
cursor.execute('UPDATE usuarios SET idade = ? WHERE nome = ?', (26, 'Maria'))

# Confirmar a operação
conexao.commit()

# Fechar a conexão
conexao.close()

print("Idade de Maria atualizada com sucesso.")
