"""
math_utils.py

A small utility module providing basic mathematical helper functions.
"""

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
    """
    Return the quotient of two numbers.
    Raises:
        ValueError: if b == 0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
