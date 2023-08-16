def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()  # Sort the sides in ascending order

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Input
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Check if it's a right triangle
if is_right_triangle(a, b, c):
    print("It's a right triangle.")
else:
    print("It's not a right triangle.")
