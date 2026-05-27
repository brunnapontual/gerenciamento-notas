import pytest
from aluno import Aluno


def test_criar_aluno():
    aluno = Aluno("Maria")
    assert aluno.nome == "Maria"
    assert aluno.notas == []


def test_deve_adicionar_nota():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(8)
    assert aluno.notas == [8]


def test_nao_deve_aceitar_nota_negativa():
    aluno = Aluno("Maria")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(-1)


def test_nao_deve_aceitar_nota_acima_de_10():
    aluno = Aluno("Maria")
    with pytest.raises(ValueError):
        aluno.adicionar_nota(11)


def test_deve_calcular_media():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(7)
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(9)
    assert aluno.calcular_media() == 8


def test_deve_retornar_zero_sem_notas():
    aluno = Aluno("Maria")
    assert aluno.calcular_media() == 0


def test_deve_retornar_aprovado():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(7)
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(9)
    assert aluno.verificar_situacao() == "Aprovado"


def test_deve_retornar_recuperacao():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(6)
    assert aluno.verificar_situacao() == "Recuperacao"


def test_deve_retornar_reprovado():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(2)
    aluno.adicionar_nota(4)
    aluno.adicionar_nota(3)
    assert aluno.verificar_situacao() == "Reprovado"


def test_media_exatamente_7_deve_ser_aprovado():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(7)
    aluno.adicionar_nota(7)
    assert aluno.verificar_situacao() == "Aprovado"


def test_media_exatamente_5_deve_ser_recuperacao():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(5)
    assert aluno.verificar_situacao() == "Recuperacao"


def test_deve_aceitar_nota_zero():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(0)
    assert aluno.notas == [0]


def test_deve_aceitar_nota_dez():
    aluno = Aluno("Maria")
    aluno.adicionar_nota(10)
    assert aluno.notas == [10]
