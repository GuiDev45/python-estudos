# Programa Principal
"""
 import math_operations - Dessa forma indica que o módulo todo está sendo importado.

 Caso não precise importar tudo, (dependendo do tamanho do módulo só quer usar algumas funções).
 Use:
 import math_operations 
 from math_operations import multiply, divide (nesse caso só está importanto o "multiply" e o "divide")
"""
import math_operations 
from math_operations import multiply, divide

import string_utils

print(math_operations.sum(5, 3))
print(math_operations.subtract(5, 3))

# Como já foi invocado o multiply e o divide, na chamada não precisa usar novamente o math_operations
print(multiply(5, 3))
print(divide(5, 3))

print(string_utils.capitalize("hello"))
print(string_utils.reverse_string("Python"))
print(string_utils.count("apple"))
