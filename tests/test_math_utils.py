import pytest
from accionestest import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
