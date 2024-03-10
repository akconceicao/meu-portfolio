# import re
# implementar um programa simples que conta o número de vogais em uma
# palavra fornecida como entrada.

def count_vowels(word):

    # def clean_text(word):
    #   return re.sub(r'[^a-zA-Z]', '', word.lower())
    # cleaned_text = clean_text(word) - dá o mesmo resultado com mais código

    vowels = 'aãeiouAEIOUéíêô'
    count = 0

    for char in word:
        if char in vowels:
            count += 1
    return count


word = input("Digite uma palavra: ")

num_vowels = count_vowels(word)

print("Total de vogais:", num_vowels)
