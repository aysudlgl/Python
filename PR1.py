import random


print ("Hello World, My Name is BOB")
 # how to make a comment

#datatype float
num_people = 20.5555
print(num_people)

#format and rounding f-strings
print(f"Number of people: {num_people}")
print(f"Number of people: {num_people:.2f}")

print('Number of people:', num_people)
print('Number of people: ', round(num_people,2))
#adding tabs
menu_text = "Main Menu. Choose an option: \n"
menu_text += "\t1. Add User\n\t2. Edit User\n"
menu_text += "\t3. Remove user \n\t4. Exit App"

print(menu_text)

#format output
print('Results')
print('-------')
temp_farh = 98.66475
temp_calc = (temp_farh - 32) * (5/9)
temp_kelvin = temp_calc + 273.15
 # padding = add space to the left :< or right :> in the f format
print(f"Farenheit: {temp_farh:>10.4f}")
print(f"Celcius: {temp_calc:>10.4f}")
print(f"Kelvin: {temp_kelvin:>10.4f}")

rand1 = random.randint(0,2)
rand2 = random.randint(10,100)
rand3 = random.randint(-20,-10)

print(rand1)
print(rand2)
print(rand3)

rand4 = random.uniform(0.1, 0.5)
rand5 = random.random()

print(rand4)
print(rand5)

#random choice(S)
#select a number(or a string)

coin = random.choice(["Heads",'Tails'])
dice = random.choice([1,2,3,4,5,6,7])

print("Coin: ", coin)
print("Dice: ", dice )
