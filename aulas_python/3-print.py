# utilizando o input

name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano\n"))
gamePrice = float(input("Digite o preço\n"))

print("Dados do Jogo")
print("=============")
# Alternativa 1
# print("Nome do jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)

# Alternativa 2
# print("Nome do Jogo:", name, "\nAno de Lançamento:",
#       yearLaunch, "\nPreço do Jogo:", gamePrice)

#Alternativa 3

print(f"Nome do Jogo: {name} \nAno de Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice}")


