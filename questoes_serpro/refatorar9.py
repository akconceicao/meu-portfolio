# Refatore o código para ser recursivo, ao invés de usar um loop
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado = resultado * i
        return resultado


numero = 5
fatorial_numero = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", fatorial_numero)
