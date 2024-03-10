def MoveDisco(origem, destino):
    print(f"Movimento: {origem} -> {destino}")


def MoveTorre(n, origem, destino, auxiliar):
    if n == 1:
        MoveDisco(origem, destino)
    else:
        MoveTorre(n - 1, origem, auxiliar, destino)
        MoveDisco(origem, destino)
        MoveTorre(n - 1, auxiliar, destino, origem)


# Exemplo de uso com 3 discos e pinos A, B e C
MoveTorre(3, 'A', 'C', 'B')
