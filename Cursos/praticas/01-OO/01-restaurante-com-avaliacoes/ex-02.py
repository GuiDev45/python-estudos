class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False
    
    # O "rosto" do objeto para o usuário
    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"Restaurante {self.nome} | Categoria: {self.categoria} | Ativo: {status}"
    
    # A "identidade" técnica do objeto
    def __repr__(self):
        return f"Restaurante(nome='{self.nome}', categoria='{self.categoria}')"
    
meu_restaurante = Restaurante("Pizzaria", "Italiana")

print(str(meu_restaurante))
# Saída: Restaurante Pizzaria | Categoria: Italiana | Ativo: Inativo
meu_restaurante.ativar()
print(meu_restaurante)
# Saída: Restaurante Pizzaria | Categoria: Italiana | Ativo: Ativo

print(repr(meu_restaurante))
# Saída: Restaurante(nome='Pizzaria', categoria='Italiana')
