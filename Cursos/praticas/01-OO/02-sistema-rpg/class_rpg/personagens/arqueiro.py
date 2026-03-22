from .personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome, vida, nivel, precisao):
        super().__init__(nome, vida, nivel)
        self.precisao = precisao

    def atacar(self, alvo):
        dano = self.precisao * 3
        alvo.receber_dano(dano)
        print(f"{self.nome} atirou uma flecha em {alvo.nome} causando {dano} de dano!")