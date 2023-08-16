

filename = input("Enter the full path of the filename: ")

with open(filename, 'r') as file:
    text = file.read()
words = text.split()
unique_words = sorted(set(words))
for word in unique_words:
    print(word)
# else:
#     print("File not found.")
