n=input()
o=""
f=0
for d in n:
    if d=='6' and f==0:
        o=o+'9'
        f=1
    else:
        o=o+d
print(o)