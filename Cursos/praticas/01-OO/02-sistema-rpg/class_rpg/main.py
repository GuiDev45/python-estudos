from personagens import Guerreiro, Mago, Arqueiro
from inventario import Item

# Criando personagens
arthur = Guerreiro("Arthur", 100, 1, forca=10)
merlin = Mago("Merlin", 80, 1, mana=30)
legolas = Arqueiro("Legolas", 90, 1, precisao=8)

# Criando itens
pocao = Item("Poção de Vida", "poção", 50)
espada = Item("Espada Longa", "arma", 15)
armadura = Item("Armadura de Couro", "armadura", 5)

# Adicionando itens
arthur.inventario.adicionar_item(pocao)
arthur.inventario.adicionar_item(espada)
merlin.inventario.adicionar_item(pocao)
legolas.inventario.adicionar_item(armadura)

# Status inicial
arthur.status()
merlin.status()
legolas.status()

# Batalhas
arthur.atacar(merlin)
merlin.status()

merlin.atacar(arthur)
arthur.status()

legolas.atacar(arthur)
arthur.status()

# Usando poção
arthur.usar_pocao()
arthur.status()