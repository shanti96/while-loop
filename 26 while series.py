#26. Write a program to print the following series till n terms.
#2 , 22 , 222 , 2222 _ _ _ _ _ n terms
n=int(input("enter the number"))
s=input("enter the number")
i=1
while i<=n:
    print(s*i,",",end="")
    i+=1