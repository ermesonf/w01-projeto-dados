import pytest
from src.contrato import Vendas
from datetime import datetime
from pydantic import ValidationError

def test_vendas_dados_validos():

    dados_validos = {
        "email": "comprador@exemplo.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "produto x",
        "quantidade": 3,
        "categoria": "categoria3",
    }
    
    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]

    # Testes com dados inválidos
def test_vendas_com_dados_invalidos():
    dados_invalidos = {
        "email": "comprador",
        "data": "não é uma data",
        "valor": -100,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3"
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)

# Teste de validação de categoria
def test_validacao_categoria():
    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": "categoria4",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)