# def check_char(text):
#     type = {"Uppercase": 0, "Lowercase": 0}
#     for char in text:
#         if char.isupper():
#             type["Uppercase"] += 1
#         elif char.islower():
#             type["Lowercase"] += 1
#     print("Texto original:", text)
#     print("Número de letras maiúscula:", type["Uppercase"])
#     print("Número de letras minúsculas:", type["Lowercase"])


# check_char("A Melhor Forma de Prever o Futuro é Criá-lo")


def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd


print(check_numbers([1, 2, 3, 4, 5, 6, 6, 7]))
