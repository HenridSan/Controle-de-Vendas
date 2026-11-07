import pytest
from logica import converter_numero, criar_produto

def test_numero_com_virgula():
    assert converter_numero("12,50") == 12.50


def test_numero_invalido():
    with pytest.raises(ValueError):
        converter_numero("abc")


def test_criar_produto_comida():
    gastos = [{"descricao": "queijo", "valor": 8.0}]
    produto = criar_produto("comida", "bolo", "assar", gastos, 10, 2)
    assert produto["nome"] == "bolo"
    assert produto["receita"] == "assar"
    assert produto["vendidos"] == 0


def test_criar_produto_pronto():
    produto = criar_produto("pronto", "fone", "  ", [], 10, 35.0)
    assert produto["receita"] == ""


def test_produto_sem_nome():
    with pytest.raises(ValueError):
        criar_produto("comida", "  ", "", [], 10, 8.0)


def test_quantidade_zero():
    with pytest.raises(ValueError):
        criar_produto("comida", "bolo", "assar", [], 0, 8.0)

