import sqlite3

conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

# Recuperar e imprimir todos os usuários com idade superior a 26

cursor.execute('SELECT * FROM usuarios WHERE idade > 26')

usuarios_acima_de_26 = cursor.fetchall()

print("Usuários com idade superior a 26:")

for usuario in usuarios_acima_de_26:
    print(usuario)

# Recuperar e imprimir o nome do usuário com id=2
cursor.execute('SELECT nome FROM usuarios WHERE id = ?', (2,))

nome_usuario_id_2 = cursor.fetchone()

if nome_usuario_id_2:

    print("\nNome do usuário com id=2:", nome_usuario_id_2[0])


# Fechar a conexão
conexao.close()
