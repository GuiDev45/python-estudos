from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_cidade.alterna_estado()

biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
biblioteca_cidade.receber_avaliacao("Sicrano", 9.5)

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()