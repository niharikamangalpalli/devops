def divide(a, b):
    """
    Performs division of two numbers.
    Returns an error message if division by zero occurs.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except TypeError:
        return "Error: Invalid input type"
