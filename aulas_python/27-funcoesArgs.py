"""
  *args - utilizamos quando não se tem certeza do número de argumentos na função
  argumentos são passados como uma tupla
  
  **kwargs - alem dos valores podemos passar também as respectivas chaves
  argumentos são passados como dicionários
  """

# soma de numeros


def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n  # sum total = sum total + n
    print(f"Soma é: {sum_total}")


sum(7)
sum(7, 9)
sum(10, 19, 19, 9, 9, 2, 1)

# apresentação de cursos


def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")


print("###Curso###")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão computacional", category="IA", level="Avançado")
