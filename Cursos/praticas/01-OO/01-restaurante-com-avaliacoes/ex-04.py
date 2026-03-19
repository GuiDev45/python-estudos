class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # Com @classmethod usa direto pela classe Restaurante.metodo()
    # Se fosse só com o self seria: r1 = Restaurante("Pizzaria", "Italiana") e depois r1.metodo()
    @classmethod
    def criar_restaurante(cls, nome, categoria):
        restaurante = cls(nome, categoria)  # cria instância
        restaurante.ativo = True            # ativa automaticamente
        return restaurante                  # retorna a instância


# usando o factory
meu_restaurante_01 = Restaurante.criar_restaurante("Pizzaria", "Italiana")

print(meu_restaurante_01.nome)       # Pizzaria
print(meu_restaurante_01.categoria)  # Italiana
print(meu_restaurante_01.ativo)      # True

# self -> "eu já existo"
# cls -> "vou criar alguém"