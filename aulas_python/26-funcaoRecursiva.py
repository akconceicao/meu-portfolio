# fatorial de um número

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))


number = int(input("Digite o número para o fatorial \n"))
print(f"O fatorial de {number} é: {factorial(number)}")


def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))


num = int(input("Digite o número para a soma \n"))
print(f"A soma total de {num} é: {total_sum(num)}")
