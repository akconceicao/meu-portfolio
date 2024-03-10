def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)


numero = 5
fatorial_numero = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", fatorial_numero)
