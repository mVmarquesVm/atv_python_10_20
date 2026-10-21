import pytest
from bubble_sort import bubble_sort


def checa_invariantes(original, resultado):
    """Propriedades que valem para qualquer entrada."""
    assert len(resultado) == len(original)          # não perdeu nem criou elemento
    assert sorted(resultado) == sorted(original)    # são os mesmos elementos
    assert all(resultado[i] <= resultado[i + 1] for i in range(len(resultado) - 1))


def test_lista_vazia():
    # Limite: o loop externo não executa (range(-1) é vazio).
    original = []
    resultado = bubble_sort(original.copy())
    assert resultado == []
    checa_invariantes(original, resultado)


def test_um_elemento():
    # Limite: não pode acessar índice inexistente.
    original = [5]
    resultado = bubble_sort(original.copy())
    assert resultado == [5]
    checa_invariantes(original, resultado)


def test_ja_ordenada():
    # Melhor caso: exercita o caminho do "else" (nunca troca).
    original = [1, 2, 3, 4, 5]
    resultado = bubble_sort(original.copy())
    assert resultado == [1, 2, 3, 4, 5]
    checa_invariantes(original, resultado)


def test_ordem_reversa():
    # Pior caso: exercita o "if" verdadeiro em todas as comparações.
    original = [5, 4, 3, 2, 1]
    resultado = bubble_sort(original.copy())
    assert resultado == [1, 2, 3, 4, 5]
    checa_invariantes(original, resultado)