import pprint

gameDict = {
    "RE4": {
        "yearLaunch": 2023,
        "genre": ["ação", "aventura"]
    },
    "mario odissey": {
        "yearLaunch": 2019,
        "genre": ["aventura", "3d"]
    },
    "le gordin": {
        "yearLaunch": 2015,
        "genre": ["pança", "comida"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gameDict)

# buscar informação dentro de um dict
print(gameDict["le gordin"]["genre"])

gameDict["le gordin"]["player"] = 5
print(gameDict)

del gameDict["mario odissey"]
pp.pprint(gameDict)
