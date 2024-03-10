def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    media = total / len(notas)
    return media


notas = [8.5, 7.2, 9.0, 5.5]
media_aluno = calcular_media(notas)
print("A média do aluno é:", media_aluno)
