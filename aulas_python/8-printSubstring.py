# string[início:fim] - índice 0 / índice final -1

# 1 busque toda string a partir da 1a posição

gameName = "fifa 23"

# o ultimo índice é excluído do slice

print(gameName[0:])
print(gameName[1:])
print(gameName[:5])
print(gameName[2:6])

"""string[início:fim:passo] - índice começa na posicao 0 - indice final -1
passo - determina o incremento. Por padrão esse número é o 1."""

# busque nos indices impares
print(gameName[1::2])
# inverter de trás pra frente
print(gameName[::-1])
