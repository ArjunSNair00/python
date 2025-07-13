a,b,c=map(int,input("Enter three numbers: ").split())
print("The largest number is: ",end='')
if a>b and a>c: 
    print(a)
elif b>c: #no need to check for a again as it is not the largest
    print(b)
else:
    print(c)
