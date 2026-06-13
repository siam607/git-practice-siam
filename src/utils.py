def multiply(a, b):
    return a * b

def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Please provide numbers only"