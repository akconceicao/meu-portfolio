# Dado o seguinte array de produtos:
# [“Celular”, “Notebook”, “Televisão”, “Tablet”, “Câmera”, “Smartwatch”]
# a) Implemente um algoritmo de ordenação por seleção (Selection Sort) para ordenar os produtos em ordem alfabética.
# b) Apresente a quantidade de comparações e trocas realizadas durante o processo de ordenação.
def selection_sort(arr):
    arrayselection = 0

    for i in range(len(arr) - 1):
        indice_minimo = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        if i != indice_minimo:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    return arrayselection


produtos = ["Celular", "Notebook", "Televisão",
            "Tablet", "Câmera", "Smartwatch"]

arrayselection = selection_sort(produtos)

print("Produtos ordenados:", produtos)


# selection_sort é a função que realiza o algoritmo de ordenação por seleção.
# Ela rastreia as quantidades de comparações e trocas.
# O loop externo varre todo o array, exceto o último elemento.
# O loop interno encontra o índice do mínimo valor a partir do índice atual.
# Se o índice do mínimo valor não for igual ao índice atual, ocorre uma troca.
# No final, o código imprime os produtos ordenados, a quantidade de comparações e a quantidade de trocas realizadas.
