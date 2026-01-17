# pprint é do próprio python, basicamente usado para visualizar melhor o dicionário no terminal
import pprint

filmsDict = {
    "inception": {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
     "The Lord of the Ring": {
        "yearRelease": 2001,
        "imdbRating": 9.5,
        "genre": ["Action", "Fantasy"]
    },
     "The Batman": {
        "yearRelease": 2023,
        "imdbRating": 8.5,
        "genre": ["Action", "Fantasy", "Adventure"]
    },
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informação dentro de um dicionario aninhado
print(filmsDict["The Batman"]["genre"])

# 2 - Adicionar um novo item
filmsDict["inception"]["director"] = "Christopher Nolan"
print(filmsDict["inception"])