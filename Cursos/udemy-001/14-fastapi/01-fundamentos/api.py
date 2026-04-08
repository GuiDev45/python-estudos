from fastapi import FastAPI

app = FastAPI()

jogadores = {
    1: {
        "nome": "Rony",
        "idade":28,
        "time": "Vasco"
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

@app.get("/get-jogador-time")
def get_jogador_time(time:str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"Dados": "Não foi encontrado"}
    
#get-jogador/1 - Path Parameter

#get-jogador/?id=1 - Query Parameter
#get-jogador-time?time="fsfd"

