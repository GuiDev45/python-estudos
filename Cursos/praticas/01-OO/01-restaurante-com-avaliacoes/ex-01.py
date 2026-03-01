class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def ativar(self):
        # Altera o estado do restaurante para True
        self.ativo = True
        print(f"O Restaurante {self.nome} foi ativado com sucesso!")
    
    def desativar(self):
        # Altera o estado do restaurante para False
        self.ativo = False
        print(f"O Restaurante {self.nome} foi desativado com sucesso!")

        # Retorno amigável do objeto
    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"{self.nome} | Categoria: {self.categoria} | Status: {status}"
    
# Criando uma instância do restaurante
meu_restaurante = Restaurante("Sabor Supremo", "Italiana")
meu_restaurante_02 = Restaurante("Tokyo Sushi", "Japonesa")

print(meu_restaurante)
# Saída: Sabor Supremo | Categoria: Italiana | Status: Inativo

meu_restaurante.ativar()
# Saída: O Restaurante Sabor Supremo foi ativado com sucesso!

print(meu_restaurante)
# Saída: Sabor Supremo | Categoria: Italiana | Status: Ativo 

meu_restaurante.desativar()
# O Restaurante Sabor Supremo foi desativado com sucesso!

print(meu_restaurante)
# Sabor Supremo | Categoria: Italiana | Status: Inativo
