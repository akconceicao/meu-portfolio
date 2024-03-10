def encontrar_primos(n):
    primos = []
    for num in range(2, n):
        is_primo = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)
    return primos


limite = 50
primos_ate_limite = encontrar_primos(limite)
print("Números primos até", limite, "são:", primos_ate_limite)
