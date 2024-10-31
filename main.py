

def soma(a, b):
    return a + b

def divisao(a, b):
    try:  
        return a / b  
    except ZeroDivisionError:  
        raise ZeroDivisionError("Division by zero is not allowed")

class Test_soma:
    def test_soma(self):
        assert soma(1, 2) == 3

    def test_divisao(self):
        assert divisao(1, 0) == 0.5
    