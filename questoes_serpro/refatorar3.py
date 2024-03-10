def contar_vogais(palavra):
    vogais = ['a', 'ã', 'e', 'i', 'o', 'u', 'A', 'E',
              'I', 'O', 'U']  # vogais = 'aeiouAEIOU'
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador


texto = "Python é umA linguagEm de prOgramação"
total_vogais = contar_vogais(texto)
print("O total de vogais é:", total_vogais)
