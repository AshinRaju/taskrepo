rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(chr(60 + j), end=" ")
    for j in range(i - 1, 0, -1):
        print(chr(60 + j), end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(chr(60 + j), end=" ")
    for j in range(i - 1, 0, -1):
        print(chr(60 + j), end=" ")
    print()