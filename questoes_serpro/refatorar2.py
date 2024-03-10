
def calcular_media(notas):
    soma = 0  # Inicialize a soma como zero
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)  # Use len(notas) para obter o número de notas
    return media


notas = [8.5, 7.2, 9.0, 5.5]
media = calcular_media(notas)
print("A média é:", media)
