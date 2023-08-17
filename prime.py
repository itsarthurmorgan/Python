print("Prime numbers less than 20 are:")

for num in range(20):
    if (num > 1):
        for j in range(2, num):

            if (num % j == 0):
                break
        else:
            print(num)
