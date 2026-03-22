from .personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome, vida, nivel, mana):
        super().__init__(nome, vida, nivel)
        self.mana = mana

    def atacar(self, alvo):
        if self.mana >= 10:
            dano = 15
            alvo.receber_dano(dano)
            self.mana -= 10
            print(f"{self.nome} lançou magia em {alvo.nome} causando {dano} de dano! Mana restante: {self.mana}")
        else:
            print(f"{self.nome} não tem mana suficiente para atacar!")