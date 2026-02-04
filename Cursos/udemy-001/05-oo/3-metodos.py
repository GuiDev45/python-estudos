class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

    # Esse método __str__(self) é usado para dar um nome pra instância, ao invés de vir os valores onde ela está alocada <__main__.Game object at 0x000001F1CE0386E0>
    def __str__(self):
        return f"Game: {self.name}"
    
game1 = Game()
print(game1) # Game:

game1.name = "Fallout 4"
print(game1) # Game: Fallout 4

# Método Construtor
class GameConstructor:
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note

# Fica mais fácil instânciar o objeto dessa forma
game2 = GameConstructor("Final Fantasy 7 Rebirth", 2025, False, 9.2)

print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")
