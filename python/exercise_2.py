"""
    Exercise #2
    Description: Write a script that shows us on the screen all the even numbers from 1 to 120
"""

def print_numbers():
    # Variables
    counter = 1

    # Loop
    while counter<= 120:
        if counter % 2 == 0:
            print(counter)

        counter += 1