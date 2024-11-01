def soma(a, c):
    return a + c

def divisao(a, b):
    try:  
        return a / b  
    except ZeroDivisionError:  
        raise ZeroDivisionError("Division by zero is not allowed")
