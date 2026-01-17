# Informações sobre o filme
name = input("Digite o nome do filme:\n")
yearRelease = int(input("Digite o ano de lançamento:\n"))
rating = float(input("Digite a nota de avaliação do filme:\n"))

# Verifica se o filme é recomendado
if rating > 8.0 and yearRelease > 2015:
    print(f"O filme {name} é muito bom. Recomendo assisti-lo")
else:
    print(f"O filme {name} ainda não atingiu uma boa nota.")