def power(num):
    return num ** 2


def is_even(x):
    return x % 2 == 0


def div_num(x, y):
    return x / y


def reverse_string(s):
    return s[::-1]


print(power(5))
print(power(9))
print(is_even(27))
print(is_even(30))
print(div_num(10, 2))
print(div_num(6, 2))
print(reverse_string("Python"))
print(reverse_string("Javascript"))


movies_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park", "The Matrix"]

ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 9.8, 8.0],
    "Inception": [8.0, 7.0, 8.5],
    "Jurassic Park": [7.5, 7.0, 8.0],
    "The Matrix": [8.8, 9.2, 8.5],
}


def average_rating(movie_name):
    return sum(ratings[movie_name]) / len(ratings[movie_name])


def check_movie(movie_name):
    return movie_name in movies_list


def recommend_movie(movie_name):
    return f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"


print(f"Média de Avaliações do filme The Matrix: {average_rating('The Matrix')}")
print(f"Inception está na lista: {check_movie('Inception')}")
print(recommend_movie("Inception"))

# Não é que lambda seja ruim.
"""
Use lambda quando a função for:

✔ Muito curta
✔ Usada uma única vez
✔ Passada como argumento
✔ Não precisa de nome próprio

EX:
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))

Importante!
Em Python, muitas vezes nem lambda é a melhor opção.

Em vez disso:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

Prefira:
even_numbers = [x for x in numbers if x % 2 == 0]
"""

