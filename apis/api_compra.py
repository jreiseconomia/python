from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens, você pode restringir mais tarde
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)


# Banco de dados fictício
jogadores = {"player1": {"saldo": 100}, "player2": {"saldo": 150}}
itens_loja = {
    1: {"nome": "Espada Mágica", "preco": 50},
    2: {"nome": "Poção de Vida", "preco": 30},
    3: {"nome": "Escudo de Ferro", "preco": 40},
}
compras_realizadas = []

# Modelo para compra
class Compra(BaseModel):
    jogador: str
    item_id: int

@app.get("/")
def home():
    return {"mensagem": "API de Compras para o Jogo de Tabuleiro"}

@app.get("/itens", response_model=dict)
def listar_itens():
    return itens_loja

@app.post("/comprar")
def comprar_item(compra: Compra):
    if compra.jogador not in jogadores:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")

    if compra.item_id not in itens_loja:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    item = itens_loja[compra.item_id]
    jogador = jogadores[compra.jogador]

    if jogador["saldo"] < item["preco"]:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    # Processar a compra fictícia
    jogador["saldo"] -= item["preco"]
    compras_realizadas.append({"jogador": compra.jogador, "item": item["nome"], "preco": item["preco"]})

    return {"mensagem": "Compra realizada com sucesso!", "saldo_restante": jogador["saldo"]}

@app.get("/compras", response_model=List[dict])
def listar_compras():
    return compras_realizadas
