def count_character_frequency(file_path):
    character_frequency = {}

    with open(file_path, 'r') as file:
        content = file.read()

        for char in content:
            if char in character_frequency:
                character_frequency[char] += 1
            else:
                character_frequency[char] = 1

    return character_frequency


def classify_file(file_path):
    file_extension = file_path.split('.')[-1].lower()

    python_extensions = ['py']
    c_extensions = ['c', 'cpp', 'h']
    txt_extension = ['txt']

    if file_extension in python_extensions:
        return "Python Program"
    elif file_extension in c_extensions:
        return "C Program"
    elif file_extension in txt_extension:
        return "Text File"
    else:
        return "Some other file"


file_path = input("Enter the path to the file: ")
classification = classify_file(file_path)
count = count_character_frequency(file_path)
print(f"The given file is classified as: {classification}")
print(f"The character frequency in the given file: \n {count}")
