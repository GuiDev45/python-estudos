class Item:
    def __init__(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo       # "arma", "poção", "armadura"
        self.valor = valor

    def __str__(self):
        return f"{self.nome} ({self.tipo}, valor: {self.valor})"