a=int(input())
b=[]
for i in range(0,a):
    c=int(input())
    b.append(c)

for i in range(0,a):
    dig = b[i]
    sum=0
    while dig>0:
        temp=dig%10
        sum = sum + temp
        # arm=arm*10+temp
        dig=dig//10
    print(sum)
