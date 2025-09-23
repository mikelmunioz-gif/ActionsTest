# src/accionestest/math_utils.py

def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide a entre b. Lanza ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b
