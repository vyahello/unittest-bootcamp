import math


def add(num1: int, num2: int) -> int:
    """ Add two numbers  """

    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """ Subtract two numbers """

    return num1 - num2


def divide(num1: int, num2: int) -> float:
    """ Divide two numbers """

    return num1 / num2


def multiply(num1: int, num2: int) -> int:
    """ Multiply two numbers """

    return num1 * num2


def square(num1: int, num2: int) -> float:
    """ Square one numbers to second one """

    return math.pow(num1, num2)


def square_root(num: int) -> float:
    """ Square root of specific number """

    return math.sqrt(num)


def ceil(num: int) -> float:
    """ Ceil a specific number """

    return math.ceil(num)


def floor(num: int) -> float:
    """ Floor a specific number """

    return math.floor(num)


def factorial(num: int) -> float:
    """ Calculate factorial of given number """

    return math.factorial(num)
