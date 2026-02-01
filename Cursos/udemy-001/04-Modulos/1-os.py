import os
import subprocess

# 1 - Consultar funcionalidades do módulo os
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
subprocess.run("ver", shell=True)

# 4 - Configurações das Máquinas
subprocess.run("systeminfo", shell=True)

# 5 - Limpar a Tela do Terminal
subprocess.run("cls", shell=True)