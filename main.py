import math

area_circle_choice = 1
circumference_choice = 2
area_square_choice = 3
exit_program = 4


def area_circle(radius):
    area = math.pi * radius ** 2
    return area


def circumference(radius):
    circumference_circle = round(2 * math.pi * radius, 3)
    return circumference_circle


def rectangle(length, width):
    perimeter_rectangle = round((2 * (length + width)), 3)
    area_rectangle = length * width
    return 'Perimeter is: ', perimeter_rectangle, 'Area is: ', area_rectangle


def show_menu():
    print()
    print('Welcome to Trigonometry')
    print('\t Menu')
    print('\t 1. Area of a circle')
    print('\t 2. Circumference of a circle')
    print('\t 3. Area and perimeter of a rectangle')
    print('\t 4. Exit Program')
    print()


def main():
    option = 0

    while option != exit_program:
        show_menu()
        option = int(input('Enter your choice: '))

        if option == area_circle_choice:
            radius = float(input('Enter the radius of the circle: '))
            print('The area of the circle is:', area_circle(radius))
        elif option == circumference_choice:
            radius = float(input('Enter the radius of the circle: '))
            print('The circumference of the circle is:', circumference(radius))
        elif option == area_square_choice:
            length = float(input('Enter the length of the rectangle: '))
            width = float(input('Enter the width of the rectangle: '))
            print(rectangle(length, width))
        elif option == exit_program:
            print('Exiting the program...')
        else:
            print('Invalid choice. Please enter a valid option.')


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#1. Modify the functions area_circle() and circumference() so that the radius is passed through
#parameters.
#2. Add one function to calculate the area and perimeter of a rectangle.Perimeter of a Rectangle = 2(a+b)
#area of Rectangle = a × b
#a. Function must use parameters.
#b. Round to 3 decimal places
#3. Add the rectangle (area and perimeter) option to the user menu.

