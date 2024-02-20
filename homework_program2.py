def calculate_property_tax(property_value):
    return property_value * 0.0065


def main():
    list_of_properties = []

    for property_index in range(1, 4):
        property_value = int(input(f"What is the property value for property ? "))
        property_tax = calculate_property_tax(property_value)
        list_of_properties.append(property_tax)
        print("The property tax for property  is ", property_tax)

    total_property_tax = sum(list_of_properties)
    print("The expected property tax to be collected for the list is", total_property_tax)

    choice = input("Do you want to calculate the property tax for a new list of lots? (yes/no): ")
    if choice.lower() == 'yes':
        main()
    else:
        print("Stopping property tax calculations.")


main()

