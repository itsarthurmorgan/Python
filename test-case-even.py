def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

num = int(input("Enter the number of elements: "))
lst = []
for i in range(num):
    ele = int(input("Enter element: "))
    lst.append(ele)

print("Original list:", lst)
print("Even numbers:", is_even_num(lst))
