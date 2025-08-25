import pytest
from multiplica_divide import multiplica, divide

def test_multiplica():
  assert multiplica(

def test_divide():
  assert divide(

def test_divide_zero():
  with pytest.raises(ValueError, match = "Não pode dividir por zero"):
    divide(10, 0)
