# logica.py
# Cada produto e um dicionario nesse formato:
# bolo = {
#     "tipo": "comida",
#     "nome": "Bolo de Chocolate",
#     "receita": "Massa de chocolate, farinha, ovos. Bater a massa e assar durante 40 minutos.",
#     "gastos": [
#         {"descricao": "ovos", "valor": 10.0},
#         {"descricao": "farinha", "valor": 5.0},
#         {"descricao": "massa", "valor": 8.0}
#     ],
#     "quantidade": 10,     # Quantidade de produtos feitos ou disponiveis
#     "preco": 8.0,        # Preço de venda do produto
#     "vendidos": 0
# }


def custo_total(produto):
    total = 0
    for gasto in produto["gastos"]:
        total = total + gasto["valor"]
    return total


def custo_por_unidade(produto):
    if produto["quantidade"] <= 0:
        return 0
    return custo_total(produto) / produto["quantidade"]


def lucro_por_unidade(produto):
    return produto["preco"] - custo_por_unidade(produto)


def restantes(produto):
    return produto["quantidade"] - produto["vendidos"]


def total_recebido(produto):
    return produto["vendidos"] * produto["preco"]


def lucro_real(produto):
    return total_recebido(produto) - (custo_total(produto))


def vender_um(produto):
    if restantes(produto) <= 0:
        return "Acabou o estoque!"
    produto["vendidos"] = produto["vendidos"] + 1
    return f"Venda realizada! Restam {restantes(produto)}"
