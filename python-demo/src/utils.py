def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def farewellMsg(name):
    """Return a farewell message."""
    return f"Goodbye, {name}!"

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("The divisor cannot be zero.")
    return a / b