from .personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, vida, nivel, forca):
        super().__init__(nome, vida, nivel)
        self.forca = forca

    def atacar(self, alvo):
        dano = self.forca * 2
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")