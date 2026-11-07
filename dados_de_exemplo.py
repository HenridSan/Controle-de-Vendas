#dados_de_exemplo.py

import os
from logica import criar_produto
from dados import salvar

ARQUIVO = "produtos.json"

if os.path.exists(ARQUIVO):
    print("Ja existe um produto.json. Apague-o para poder recriar.")
else:
    bolo = criar_produto(
        "comida", "Bolo de chocolate", "Bater e assar durante 40 min.",
        [
            {"descricao": "ovos", "valor": 8.0},
            {"descricao": "farinha", "valor": 5.0},
            {"descricao": "massa de chocolate", "valor": 4.0},
        ],
        10, 8.0,
    )
    fone = criar_produto(
        "pronto", "fone", "",
        [
            {"discricao": "frete", "valor": 15.0},
            {"descricao": "compra em atacado", "valor": 200.0},
            {"descricao": "taxa da plataforma", "valor": 20.0},
        ],
        10, 35.0
    )
    salvar({"produtos": [bolo, fone]}, ARQUIVO)
    print("produtos de exemplos criados!")