#31. Write a program to find the sum of following series:
#1 + 2 + 6 + 24 + 120 . . . . . n terms
n=int(input("enter the number"))
i=1
p=1
s=0
while i<=n:
    p=i*p
    s=p+s
    i=i+1
    print(s)  