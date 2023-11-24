"""
    Excercise #4
    Description: Ask the user for 2 numbers and do all the basic operations of a calculator and display it on the screen.
"""

def calculator():
    # Variables
    number_one = int(input('Ingrese el primer número: '))
    number_two = int(input('Ingrese el segundo número: '))

    # Operations
    addition = number_one + number_two
    subtraction = number_one - number_two
    multiplication = number_one * number_two
    division = number_one / number_two
    exponentiation = number_one ** number_two
    modulus = number_one % number_two

    # Print Results
    print('Suma: ', addition)
    print('Resta: ', subtraction)
    print('Multiplicación: ', multiplication)
    print('División: ', division)
    print('Exponente: ', exponentiation)
    print('Módulo: ', modulus)