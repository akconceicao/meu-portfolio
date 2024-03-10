gameList = ["Resident Evil 4", "Star Wars", "Red Dead 2", "Burn", "Le gordin"]

# length
print(len(gameList))
# indice
print(gameList.index("Burn"))

# adicionar item ao final da lista
gameList.append("GTA 5")

# ordenar a lista
gameList.sort()
print(gameList)

# copiar uma lista para a outra
gameReset = gameList.copy()
gameReset.remove("Burn")
print(gameReset)

# remove todos os itens da lista
