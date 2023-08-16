def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Temperature Conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius_temp = float(input("Enter temperature in Celsius: "))
    converted_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp:.2f} Celsius is equal to {converted_temp:.2f} Fahrenheit")
elif choice == 2:
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    converted_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp:.2f} Fahrenheit is equal to {converted_temp:.2f} Celsius")
else:
    print("Invalid choice. Please choose 1 or 2.")
