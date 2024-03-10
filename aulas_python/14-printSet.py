gameSet = {"Fifa 23", "Burn", "Zelda", "RE4", "Pito"}

print(gameSet)

# buscar o tamanho do set
print(len(gameSet))

# true 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

gameSet.update(exampleSet)
print(gameSet)

# remover um item do set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)


# nao repete valor, assim como no set
# não possibilita recuperar valores por slice/fatiamento
