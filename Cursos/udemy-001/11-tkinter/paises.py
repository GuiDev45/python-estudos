import random

# Dicionário de países
paises = {
    "AR": "Argentina",
    "AU": "Austrália",
    "BE": "Bélgica",
    "BR": "Brasil",
    "CA": "Canadá",
    "CH": "Suiça",
    "CL": "Chile",
    "CM": "Camarões",
    "CN": "China",
    "CO": "Colômbia",
    "DE": "Alemanha",
    "EG": "Egito",
    "ES": "Espanha",
    "FR": "França"
}

paises_simbolo = [codigo.lower() for codigo in paises.keys()]

def dados_pais():
    simbolo = random.choice(paises_simbolo)

    imagem = f"img/{simbolo}.png"
    nome = paises[simbolo.upper()]

    return imagem, nome