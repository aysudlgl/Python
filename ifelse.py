'''
grade =  int(input('Enter your grade: '))
letter = 'F'

if(grade >= 69 and grade <= 69):
    letter == 'D'
elif (grade >= 69 and grade <= 79):
    letter = 'C'
elif(grade >= 79 and grade <= 89):
    letter == 'B' 
if letter == 'D' or letter == 'C' or letter == 'B':
    print('you passed, you grade letter is', letter) 
else:
    print('You did not pass, your letter grade is', letter)

user_menu = 'y'

while user_menu == 'y':

    grade = int(input('Enter your grade: '))
    letter = 'F'

if(grade >= 69 and grade <= 69):
    letter = 'D'
elif (grade >= 69 and grade <= 79):
    letter = 'C'
elif(grade >= 79 and grade <= 89):
    letter = 'B' 
if letter == 'D' or letter == 'C' or letter == 'B':
    print('you passed, you grade letter is', letter) 
else:
    print('You did not pass, your letter grade is', letter)
'''
#print a rectangle
#control variable
counter = 0
#ask the user how big the rectangle is
size = int(input('How big should the rectangle be: '))

while(counter < size):
    print('******')
    counter += 1
print ('rectangle done.')


cnt = 1

while cnt < 10:

#control variable for 2nd loop
    char = 0
    while char < cnt:
        print('*', end = '')
        char += 1

    print()
    cnt += 1    

##Multiplication table
print('********Multiplication Table*******')
base_num = int(input('Give me an integer to calculate '))

#use a set of dashes to arrange the output
print('----------')
#COUNT 0 TO 12

for i in range (13):
    result = base_num * i

    print(f"{base_num} x {i} = {result}")

    print('---------')

#print a table for temperatures

print('Enter the starting themperature')

start_Temp = int(input('Enter the starting themperature'))
end_Temp = int(input('Enter the ending temperature'))
end_Temp +=1
#while loop/control var
for fahr in range (start_Temp, end_Temp):
    celcius = (fahr - 32) * (5/9)
    #if some code then else then some code then print
    print(f"{fahr:0.2f}F----> {celcius:0.2f}*C")

print('----------')

#check for condition