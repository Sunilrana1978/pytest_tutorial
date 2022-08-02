from src.example import add ,concat

def test_add():
    assert add(10, 20) == 30

def test_concat():
        assert concat("foo", "bar") == "foobar"

class TestSample:
    def test_add(self):
        assert add(10, 20) == 30

    def test_concat(self):
        assert concat("foo", "bar") == "foobar"