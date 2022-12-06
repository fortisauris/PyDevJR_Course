import pytest
from session21 import vyber_hodnotu, vrat_hodnotu

@pytest.fixture()
def falosny_input():
    input_name = 'Frantisek'
    return input_name


@pytest.mark.ine
def test_value():
    assert vyber_hodnotu(5) is True
    assert vyber_hodnotu(-5) is False

@pytest.mark.string
def test_name(falosny_input):
    assert falosny_input == 'Frantisek'

@pytest.mark.ine
def test_vacsi():
    assert vyber_hodnotu(21) is not False

@pytest.mark.parametrize('inp', [-21,'str',None ])
def test_mensi(inp):
    assert vyber_hodnotu(inp) is not True

@pytest.mark.parametrize('inp, output', [(1, 9), (2, 18), (-9, -81)])
def test_mensi_2(inp, output):
    assert vrat_hodnotu(inp) == output
