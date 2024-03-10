# funcao q receba 2 argumentos : 1 e o 2o nome
def full_name(fname, lname):
    print(f"Nome completo: {fname}{lname}")


full_name("Rodrigo ", "Macedo")

# crie uma função que some dois números via parametros


def sum(a, b):
    return a + b


print(sum(10, 50))

# argumentos default numa função


def address(country="Brasil"):
    print(f"Eu moro no {country}")


address()
address("Canadá")


def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo \n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note  # sum = sum + note
    print(f"Média de avaliação do jogo {game_name} é: {sum / qtdRating}")


rating = int(input("Digite quantas avaliações deseja fazer no jogo \n"))
rating_game(rating)
