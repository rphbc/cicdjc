from main import soma, divisao

class Test_soma:
    def test_soma(self):
        assert soma(1, 2) == 3

    def test_divisao(self):
        assert divisao(1, 2) == 0.5
    