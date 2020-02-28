a = int(input())
lis1=[]
lis2=[]

for i in range(0,a):
    k, b = input().split()
    lis1.append(int(k))
    lis2.append(int(b))

for i in range(0,a):
    sum= lis1[i] + lis2[i]
    print(sum)
