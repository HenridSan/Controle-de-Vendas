from dados import carregar, salvar
from logica import vender_um, restantes


def ficha_de_exemplo():
    return {
        "tipo": "comida",
        "nome": "pao de queijo",
        "receita": "Bater e assar durante 30 min.",
        "gastos": [{"descricao": "queijo", "valor": 12.0}],
        "quantidade": 10,
        "preco": 2.0,
        "vendidos": 0,
    }


def test_carregar_sem_arquivo(tmp_path):
    caminho = tmp_path / "produto.json"
    assert carregar(caminho) == {"produto": []}


def test_salvar_e_carregar(tmp_path):
    caminho = tmp_path / "produto.json"
    dados = {"produto": [ficha_de_exemplo()]}
    salvar(dados, caminho)
    assert carregar(caminho) == dados


def test_venda_continua(tmp_path):
    caminho = tmp_path / "produto.json"
    dados = {"produto": [ficha_de_exemplo()]}
    vender_um(dados["produto"][0])
    salvar(dados, caminho)


    dados_lidos = carregar(caminho)
    assert dados_lidos["produto"][0]["vendidos"] == 1
    assert restantes(dados_lidos["produto"][0]) == 9
