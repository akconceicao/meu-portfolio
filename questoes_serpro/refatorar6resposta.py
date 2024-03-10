def calcular_media(notas):
    if not notas:
        return 0  # Retorna 0 se a lista de notas estiver vazia
    return sum(notas) / len(notas)


notas = [8.5, 7.2, 9.0, 5.5]
media_aluno = calcular_media(notas)
print("A média do aluno é:", media_aluno)
