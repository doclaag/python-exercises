"""
    Excercise #3
    Description: Function that prints all the squares of the first 60 natural numbers.
"""
def print_squares():
    # Variables
    counter = 1

    # Loop
    while counter <= 60:
        print(f'El cuadrado de {counter} es: {counter * counter}')
        counter += 1