def sequencia_crescente(numbers):
    if len(numbers) <= 1:
        return True
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True


lista_numeros = [int(x) for x in input(
    "Digite uma lista de números separados por espaço: ").split()]

if sequencia_crescente(lista_numeros):
    print("A sequência é crescente!")
else:
    print("A sequência não é crescente.")
1
