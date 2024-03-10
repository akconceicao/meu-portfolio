gameDict = {
    "name": "Fifa 23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "genre": ["esporte", "família"]
}

print(gameDict)
print(len(gameDict))
print(type(gameDict))

# recuperar elemento do dict
print(gameDict["genre"])
print(gameDict.get('gamePrice'))

# recuperar as chaves do dict
print(gameDict.keys())
print(gameDict.values())

# buscar itens com chave e valor
print(gameDict.items())

# adicionar itens no dict
gameDict["player"] = 2
print(gameDict)

gameDict.update({"player": 7})
print(gameDict)

# remover itens do dict
gameDict.pop("gamePrice")
print(gameDict)
