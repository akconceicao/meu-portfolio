passenger_km = float(input("Qual distância em kms você deseja percorrer: "))

if passenger_km <= 200:
    valor_passagem = passenger_km * 0.50
else:
    valor_passagem = passenger_km * 0.35
print(f"Preço da passagem = {valor_passagem:.2f}\n")

salario = float(input("Informe o seu salário mensal: "))
percentual_aumento = 0.15

if salario > 1250:
    percentual_aumento = 0.1
salario_aumentado = salario * percentual_aumento
print(f"Seu salário foi aumentado em {salario_aumentado} \n")
