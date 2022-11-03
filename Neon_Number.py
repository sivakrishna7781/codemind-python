n=int(input())
z=n*n
s=0
while z>0:
    r=z%10
    s=s+r
    z=z//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")
    