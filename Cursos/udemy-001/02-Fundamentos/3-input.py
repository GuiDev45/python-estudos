# Utilizando o Input

# A saída do input sempre sera String
name = input("Digite o nome do filme:\n")
year_launch = input("Digite o ano do filme:\n")
note_movie = input("Digite a nota do filme:\n")

print("Resultado:\n")
print(type(name)) #string
print(type(year_launch)) #string
print(type(note_movie)) #string

# ---------------------------------------------------------------

# Transformando o input em outros tipos
nick = input("Nick\n")
age = int(input("Idade:\n"))
height = float(input("Altura:\n"))

print("Resultado")
print(type(nick)) #string
print(type(age)) #int
print(type(height)) #float