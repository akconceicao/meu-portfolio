import re


def check_palindrome(text):
    # Função para remover espaços e pontuações e converter para letras minúsculas
    # ^[a-zA-Z] means any a-z or A-Z at the start of a line
    # [^a-zA-Z] means any character that IS NOT a-z OR A-Z

    def clean_text(input_text):
        return re.sub(r'[^a-zA-Z]', '', input_text.lower())

    cleaned_text = clean_text(text)
    # Verificar se a palavra ou frase é um palíndromo
    if cleaned_text == cleaned_text[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")


entrada = input("Digite uma palavra ou frase: ")
check_palindrome(entrada)
