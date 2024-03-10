gameList = ["Fifa", "God of War", "Brun", "Uncharted"]
# iterando valores de uma lista
for game in gameList:
    print(game)

# quando a condição for atendida o loop será encerrado
for game in gameList:
    if game == "Brun":
        break
    print(game)

# quando a condição for atendida o loop vai para a próxima iteração
# pula o elemento da condição
for game in gameList:
    if game == "God of War":
        continue
    print(game)

# avaliação do jogo
# for i in range(5):
#     print("Hello World")

gameName = input("Digite o nome do jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo \n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo\n"))
    sum += note  # sum + note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating}")
