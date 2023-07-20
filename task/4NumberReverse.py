n = int(input("Enter the number : "))
b = 0
while(n>0):
    a = n%10
    b = b*10 + a
    n = n//10
print("Reverse = ",b)