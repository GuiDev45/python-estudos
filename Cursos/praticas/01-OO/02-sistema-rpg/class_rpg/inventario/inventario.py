class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item.nome} adicionado ao inventário!")

    def listar_itens(self):
        print("Inventário:")
        if not self.itens:
            print("Vazio")
        for item in self.itens:
            print("-", item)