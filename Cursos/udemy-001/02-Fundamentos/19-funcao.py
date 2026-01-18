# 1 - Função para imprimir uma mensagem
def welcome():
    print("Bem-vindo ao sistema de filmes!")

# Chamando a função
welcome()

# 2 - Função para calcular a média de notas
def calculate_average():
    num_ratings = int(input("Digite quantas avaliações deseja fazer pro filme:\n"))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme:\n"))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    # Como não tem um print precisa do return, caso contrário não ia aparecer nada
    return average

print(f"A média da avaliação é: {calculate_average():.2f}" )

# 3 - Função para cadastrar um filme:
def create_movie():
    name = input("Digite o nome do filme\n")
    yearLaunch = int(input("Digite o ano do filme:\n"))
    moviePrice = float(input("Digite o preço do filme:\n"))
    rating = float(input("Digite a nota do filme:\n")) 
    print(f"{name} - {yearLaunch} - R$ {moviePrice:.2f} - {rating}")

create_movie()
