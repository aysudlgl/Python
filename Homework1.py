

def convert_temperature(start_temperature, end_temperature):
    for i in range(start_temperature, end_temperature + 1):
        temp_calc = (i - 32) * (5/9)
        if temp_calc >= 0 and temp_calc != 0:
            print(f"{i}°F ----> {temp_calc:.2f}°C")
        else:
            print(f"{i}°F ----> {temp_calc:.2f}°C ----> Freezing conditions. Take caution.")


def main():
    print("Welcome to the Temperature Table!")
    choice = 'yes'
    # i wanted to make it case insensitive
    while choice.lower() == 'yes':
        start_temperature = int(input("Enter the starting Temperature: "))
        end_temperature = int(input("Enter the ending temperature: "))
        convert_temperature(start_temperature, end_temperature)
        choice = input("Do you want to continue? (yes/no): ")

main()