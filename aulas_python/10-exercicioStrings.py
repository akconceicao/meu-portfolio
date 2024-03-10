# substituindo caractere repetido
name = "Fifa"

char = name[0].lower()
print(char)
new_name = name.replace(char, '$')
new_name = char + new_name[1:]
print(new_name)

# troca de caracteres

string1 = 'abc'
string2 = 'wxy'

new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

string3 = new_string1 + new_string2

print(string3)
