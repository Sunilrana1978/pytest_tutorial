import pytest

from src.example_4 import add


def test_add_1():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(100, 200) == 300
    assert add("sunil", "kumar") == "sunilkumar"

@pytest.mark.parametrize("num1,num2,expected", [(1,2,3), (2,3,5), (100,200,300),("sunil","kumar","sunilkumar")])
def test_eval(num1,num2, expected):
    assert add(num1,num2) == expected


