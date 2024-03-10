def encontrar_primos(n):
    if n < 2:
        return []

    # Inicializa uma lista com números de 2 a n
    numeros = list(range(2, n + 1))
    primos = []

    while numeros:
        primo = numeros[0]
        primos.append(primo)

        # Remove todos os múltiplos do primo da lista
        numeros = [num for num in numeros if num % primo != 0]

    return primos


limite = 50
primos_ate_limite = encontrar_primos(limite)
print("Números primos até", limite, "são:", primos_ate_limite)
