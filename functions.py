#function 1 
#function 2
#function 3 
import math
area_circle_choice = 1
circumference = 2
exit_program = 3

def area_circle():
    radius = float(input('Enter the radius of the circle'))
    area = math.pi * radius**2
    return area

def circumference():
    radius = float(input('Enter the radius of the circle'))
    circumference_circle = round(2 * math.pi * radius,3)
    return circumference_circle

def show_menu():
    print()
    print('Welcome to Trigonometry')
    print('\t Menu')
    print('\t 1. Area of a circle')
    print('\t 2. Circumference of a circle')
    print('\t 3. Exit Program')
    print()

#define main function is a must : "driver function"
    
def main():
    #control: while loop

    #control variable
    option = 0

    while option != exit_program:

        show_menu()

        option = int(input('Enter your choice: '))

        if option == area_circle_choice:
            #area_function = area_circle() :slides
            print('The area of the circle is:',area_circle() )


    