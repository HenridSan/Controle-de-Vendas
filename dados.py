#dados.py
#Guarda e le os produto em um arquivo

import json
import os

def carregar(caminho):
    if not os.path.exists(caminho):
        return {"produto": []}
    with open (caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar(dados, caminho):
    with open (caminho, "w", encoding="utf-8") as arquivo:
        return json.dump(dados, arquivo, ensure_ascii=False, indent=2)
