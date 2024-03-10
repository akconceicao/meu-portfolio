def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


numero = 5
print("O fatorial de", numero, "é:", fatorial(numero))
