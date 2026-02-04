class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

# Primeiro jogo (objeto)
game1 = Game() # Criando o objeto (instânciando a classe)
print(game1) # <__main__.Game object at 0x000001F1CE0386E0> esse é o objeto em memória

# Passando valores para as propriedades do objeto
game1.name = "Baldur's Gate 3"
game1.yearLaunch = 2023
game1.multiplayer = True
game1.note = 9.8

# Segundo jogo (objeto)
game2 = Game() # Criando o objeto (instânciando a classe)
game2.name = "Fallout 4"
game1.yearLaunch = 2015
game1.multiplayer = False
game1.note = 9


print("---Dados do Jogo---")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")
