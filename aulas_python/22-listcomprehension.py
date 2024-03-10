# liste valores de 0 a 10 q seja menor do que 4
# for i in range(10):
#     if i < 4:
#         print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gameList = ["Mario Odyssey", "DK Country", "Luigis Mansion"]

newList = [x for x in gameList if "a" in x]
print(newList)

gamesFinished = [x for x in gameList if x != "Mario Odyssey"]
print(gamesFinished)
