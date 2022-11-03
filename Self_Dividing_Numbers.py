a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    while i!=0:
        r=i%10
        if r==0 or t%r!=0:
            break
        else:
            i=i//10
    if i==0:
        print(t,end=' ')