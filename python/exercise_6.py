"""
    Excercise #6
    Description: Show all multiplication tables from 1 to 10. Showing the title of the table and then the multiplications from 1 to 10.
"""

def print_multiplication_tables():
    # Variables
    number = 1

    # Operations
    while number <= 10:
        print(f'Tabla del {number}')
        for multiplier in range(1, 11):
            print(f'{number} x {multiplier} = {number * multiplier}')
        number += 1
        print("\n")