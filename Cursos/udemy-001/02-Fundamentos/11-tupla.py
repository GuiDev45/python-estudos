filmsTuple = ("Inception", "The Dark Knight", "Pulp Fiction", "Interstellar")
print(type(filmsTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(filmsTuple[:2])

# 2 - Buscar o último item da tupla
print(filmsTuple[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsTuple[2:])

# 5 - Recuperar um item da tupla pelo nome
print(filmsTuple.index("Pulp Fiction"))
