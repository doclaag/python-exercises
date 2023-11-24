"""
    Excercise #5
    Description: Show all numbers between two numbers that the user says.
"""

def print_numbers_between():
    # Variables
    number_one = int(input('Ingrese el primer número: '))
    number_two = int(input('Ingrese el segundo número: '))

    # Operations
    if number_one < number_two:
        for number in range(number_one, number_two + 1):
            print(number)
    else:
        for number in range(number_two, number_one + 1):
            print(number)