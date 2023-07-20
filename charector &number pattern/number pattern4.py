num=5
a=0
for i in range(num,0,-1):
    a+=1
    for j in range(1,i+1):
        print(a,end=' ')
    print('')