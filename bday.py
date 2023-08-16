# Take input from the user for birthdays in the format "name:dd-mm-yyyy"
data = input("Enter birthdays (name:dd-mm-yyyy separated by commas): ")

birthdays = data.split(",")


birthday_dict = {}  

for birthday in birthdays:
    name, bday = birthday.split(":")
    birthday_dict[name] = bday.strip()

print(birthday_dict)

name = input("Enter a name to search: ")

if name in birthday_dict:
    print("The birthday of", name, "is", ":".join([name, birthday_dict[name]]))
else:
    print("No data found for", name)
