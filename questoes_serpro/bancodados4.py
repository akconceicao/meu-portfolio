import sqlite3

conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

# Remover o usuário João
cursor.execute('DELETE FROM usuarios WHERE nome = ?', ('Joao',))

# Confirmar a operação
conexao.commit()

print("Usuário João removido com sucesso.")

# Eliminar a tabela "usuarios"
# cursor.execute('DROP TABLE IF EXISTS usuarios')

# Confirmar a operação
# conexao.commit()

# print("Tabela usuarios eliminada com sucesso.")
# Fechar a conexão
conexao.close()
