def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)


# Example usage
n = int(input("Enter a number: "))

if (n < 0):
    print("Invalid, Enter postive elements")
else:
    print(factorial1(n)) 
