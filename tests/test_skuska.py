from vstupy.skuska import nejaka_funkcia
import pytest

@pytest.fixture
def falosny_slovnik():
    slovnik = {'A' : 1,
               "B" : 2,
               'C' : 3
               }
    return slovnik


def test_nejaka(falosny_slovnik):
    assert list(nejaka_funkcia(falosny_slovnik)) == [1,2,3]