
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        email_addresses = file.read().splitlines()
        
        if email_addresses:
            result = ';'.join(email_addresses)
            print("Email addresses separated by semicolons:")
            print(result)
        else:
            print("The file is empty.")
except FileNotFoundError:
    print("File not found.")
