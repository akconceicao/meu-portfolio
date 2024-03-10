name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano do jogo\n"))
classification = float(input("Digite a nota do jogo\n"))

if classification > 8.0 or yearLaunch > 2015:
    print(f"O jogo {name} é bom. Recomendo")
else:
    print(f"O jogo {name} não é bom, não recomendo. ")
