import pytest

from logica import custo_total, custo_por_unidade, lucro_por_unidade, restantes, total_recebido, lucro_real, vender_um

def novo_bolo():
    return {
        "tipo": "comida",
        "nome": "bolo de chocolate",
        "receita": "massa de chocolate, farinha, ovos. Bater a massa e assa durante 40 minutos.",
        "gastos": [
            {"descricao": "ovos", "valor": 8.0},
            {"descricao": "farinha", "valor": 5.0},
            {"descricao": "massa", "valor": 4.0},
        ],
        "quantidade": 10,
        "preco": 8.0,
        "vendidos": 0,
        }


def novo_produto():
    return {
        "tipo": "pronto",
        "nome": "fone de ouvido",
        "receita": "",
        "gastos": [
            {"descricao": "Compra em atacado", "valor": 200},
            {"descricao": "Taxa da plataforma", "valor": 20},
            {"descricao": "frete", "valor": 15},
        ],
        "quantidade": 10,
        "preco": 35.0,
        "vendidos": 0,
    }


def test_custo_total():
    bolo = novo_bolo()
    assert custo_total(bolo) == 17.0


def test_custo_por_unidade():
    bolo = novo_bolo()
    assert custo_por_unidade(bolo) == pytest.approx(1.7)


def test_custo_por_unidade_zero():
    bolo = novo_bolo()
    bolo["quantidade"] = 0
    assert custo_por_unidade(bolo) == 0


def test_lucro_por_unidade():
    bolo = novo_bolo()
    assert lucro_por_unidade(bolo) == pytest.approx(6.3)


def test_vender_diminui_estoque():
    bolo = novo_bolo()
    mensagem = vender_um(bolo)
    assert restantes(bolo) == 9
    assert bolo["vendidos"] == 1
    assert mensagem == "Venda realizada! Restam 9"


def test_nao_vende_sem_estoque():
    bolo = novo_bolo()
    bolo["quantidade"] = 1
    vender_um(bolo)
    mensagem = vender_um(bolo)
    assert mensagem == "Acabou o estoque!"
    assert bolo["vendidos"] == 1


def test_lucro_real_comeca_negativo():
    assert lucro_real(novo_bolo()) == -17.0


def test_lucro_real_apos_vender_tres():
    bolo = novo_bolo()
    for i in range(3):
        vender_um(bolo)
    assert lucro_real(bolo) == 7.0


def test_lucro_real_apos_venda_sete_produtos():
    fone = novo_produto()
    custo_total(fone) == 235.0
    for i in range(6):
        vender_um(fone)
    assert lucro_real(fone) == -25.0
    vender_um(fone)
    assert lucro_real(fone) == 10
