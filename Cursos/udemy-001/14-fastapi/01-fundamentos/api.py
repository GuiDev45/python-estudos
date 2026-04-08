from fastapi import FastAPI

app = FastAPI()

jogadores = {
    1: {
        "nome": "Rony",
        "idade":28,
        "time": "Palmeiras"
    },
    2:{
        "nome":"Gustavo Gomez",
        "idade": 29,
        "time": "Palmeiras"
    }
}

@app.get("/")
def inicio():
    return jogadores

@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador:int):
    return jogadores[id_jogador]

#get-jogador/1 - Path Parameter

#get-jogador/?id=1 - Query Parameter

