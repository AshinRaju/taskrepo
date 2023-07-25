rows = 6
alphabet = 65

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        char = chr(alphabet)
        print(char, end=" ")
        alphabet +=1
    print()