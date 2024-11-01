def soma(a, b):
    return a + b

def divisao(a, b):
    try:  
        return a / b  
    except ZeroDivisionError:  
        raise ZeroDivisionError("Division by zero is not allowed")
