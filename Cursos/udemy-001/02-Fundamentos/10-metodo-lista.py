filmsList = ["Inception", "The Dark Knight", "Pulp Fiction", "Interstellar"]

# 1 - Tamanho da lista
print(len(filmsList))

# 2 - Recuperar um item da lista pelo nome
print(filmsList.index("Interstellar"))

# 3 - Adicionar item ao final da lista
filmsList.append("The Lord of the Rings")
print(filmsList)

# 4 - Ordenar a lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsList)
