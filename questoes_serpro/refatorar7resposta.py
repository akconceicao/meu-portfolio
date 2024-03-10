def contar_vogais(palavra):
    vogais = 'aãeéiou'
    return sum(1 for letra in palavra.lower() if letra in vogais)


texto = "Python é uma linguagem de programação"
total_vogais = contar_vogais(texto)
print("O total de vogais é:", total_vogais)
