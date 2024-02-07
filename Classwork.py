
#adding tabs
menu_text = "Main Menu. Choose an option: \n"
menu_text += "\t1. Add User\n\t2. Edit User\n"
menu_text += "\t3. Remove user \n\t4. Exit App"

print(menu_text)

#question 2 slope
x1 = int(input('Enter x1 value: '))
x2 = int(input('Enter x2 value: '))
y1 = int(input('Enter y1 value: '))
y2 = int(input('Enter y2 value: '))

m = (y2- y1) / (x2-x1)

print('M = ', round(m,3))
print(f"M =  {m:.3f}")

#Question 3 
grade1 = float(input('Enter grade 1 = '))
grade2 = float(input('Enter grade 2 = '))
grade3 = float(input('Enter grade 3 = '))
totalGrades = [grade3,grade2,grade1]
AverageGrades = (sum(totalGrades)) // 3

print('Average', round(AverageGrades,2))

#Question 4, ask the user for the values needed in the equation, setuo the equation and print
AnnualRate = 0.10
FutureValue  = 10000
NumberofYears = 10
PresentValue = ((FutureValue)/((1 + AnnualRate)** NumberofYears))

print("The amount you need to deposit today = ", round(PresentValue,2))