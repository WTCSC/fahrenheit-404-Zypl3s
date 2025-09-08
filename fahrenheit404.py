print("Welcome to the Fahrenheit to Celsius converter!")
def choose():
    global choice
    choice = input("Which conversion would you like to perform? (1) Fahrenheit to Celsius or (2) Celsius to Fahrenheit: ")
    if choice != "1" and choice != "2":
        print("Invalid choice. Please select 1 or 2.")
        choose()
    else:
        return choice

def again():
    agn = input("Would you like to convert another temperature? (Y / N): ")
    if agn.lower() == "y" or agn.lower() == "yes":
        choose()
        convert()
    else:
        print("Thank you for using the converter!")
        exit()
            
def convert():
    if choice == "1":
        temp = float(input("Enter temperature in Fahrenheit: "))
        converted = (float(temp) - 32) * 0.5555
        print(f"{temp} degrees Fahrenheit is {converted} degrees Celsius.")
        again()
    elif choice == "2":
        temp = float(input("Enter temperature in Celsius: "))
        converted = (float(temp) * 1.8) + 32
        print(f"{temp} degrees Celsius is {converted} degrees Fahrenheit.")
        again()
        
choose()
convert()