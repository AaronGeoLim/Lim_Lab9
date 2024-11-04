number = int(input("Please enter the number of rows of the triangle: "))

x = 1

for i in range(number):
    for j in range(i + 1):
        print(x, end=' ')
        x += 1
    print()
