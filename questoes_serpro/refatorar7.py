def contar_vogais(palavra):
    vogais = ['a', 'ã', 'e', 'é', 'i', 'o', 'u']
    contador = 0
    for letra in palavra:
        if letra.lower() in vogais:
            contador += 1
    return contador


texto = "Python é uma linguagem de programação"
total_vogais = contar_vogais(texto)
print("O total de vogais é:", total_vogais)
