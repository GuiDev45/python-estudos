num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Potência do número {num1} por {num2} é: {exp}")
print(f"Resto da divisão de {num1} por {num2} é: {mod}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2

print(bigger)
print(smaller)
print(equal)
print(different)
