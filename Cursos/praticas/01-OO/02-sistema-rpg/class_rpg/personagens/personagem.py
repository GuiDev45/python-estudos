from abc import ABC, abstractmethod
from inventario.inventario import Inventario

class Personagem(ABC):
    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self._vida = vida
        self.nivel = nivel
        self.inventario = Inventario()  # cada personagem TEM um inventário

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = max(0, valor)  # vida não pode ser negativa

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Nível: {self.nivel}")
        print("--------------------")

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano!")

    @abstractmethod
    def atacar(self, alvo):
        pass

    def usar_pocao(self):
        for item in self.inventario.itens:
            if item.tipo == "poção":
                self.vida += item.valor
                print(f"{self.nome} usou {item.nome} e recuperou {item.valor} de vida!")
                self.inventario.itens.remove(item)
                return
        print(f"{self.nome} não tem poção para usar!")