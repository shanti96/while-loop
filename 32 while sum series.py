#32. Write a program to find the sum of following series:
#S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
i=int(input("enter the number"))
n=1
p=0
while n<=i:
    s=n**2
    p=p+s
    if s%2==1:
        print(s,"+",end="")
    elif s%2==0:
        print(s,"-",end="")  
    n=n+1
print(p)