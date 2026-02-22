from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

livro1 = Livro("1984", "George Orwell", 30.0, "084-3254")
revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")

# biblioteca_cidade.alterna_estado()
# biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
# biblioteca_cidade.receber_avaliacao("Sicrano", 9.5)

def main():
   # Biblioteca.listar_bibliotecas()
   print(vars(livro1))
   print(vars(revista1))

if __name__ == "__main__":
    main()