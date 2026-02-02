import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Verificar algoritmos de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# OBS: Não são as melhores formas de usar hash no python.