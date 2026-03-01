class Restaurante:
    # Variável de Classe (compartilhada por todas as instâncias)
    total_restaurantes = 0

    # Iniciando os atributos do objeto
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

        # Usando a variável de classe para sempre receber + 1
        type(self).total_restaurantes += 1

    def __str__(self):
        return f"{self.nome} ({self.categoria})"
    
# Instânciando o objeto    
meu_restaurante_01 = Restaurante("Pizzaria", "Italiana")
meu_restaurante_02 = Restaurante("Sushi Code", "Japonesa")
meu_restaurante_03 = Restaurante("Burguer Byte", "Lanches")

# Chamando a variável (que é interna do objeto Restaurante)
print(f"Total criados: {Restaurante.total_restaurantes}")
# Saída: Total criados: 3

""""
Pergunta:
Quando usar variável de classe ao invés de instância?
R -> Quando usar a variável de classe, exemplo quando todos os restaurantes usam a mesma taxa.
e quando não usar, quando a propriedade é diferente, exemplo cada restaurante tem seu próprio nome etc.
"""

