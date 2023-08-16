# Find the mean,median,mode of the given numbers.


import statistics

num = int(input("Enter the total number of elements: "))
listnum = []
for i in range(num):
    new_num = int(input(f"Enter the value of element {i + 1}: "))
    listnum.append(new_num)

print("The mean, median, and mode of the numbers will be:")

mean = statistics.mean(listnum)
print("Mean:", mean)

median = statistics.median(listnum)
print("Median:", median)

try:
    mode = statistics.mode(listnum)
    print("Mode:", mode)
except statistics.StatisticsError:
    print("No unique mode found.")
