#12. Write a program to find the product of the digits of 
# a number accepted from the user.
a=input("enter the number")
b=len(a)
c=0
i=1
while c<b:
    s=int(a[c])
    i=s*i
    c=c+1
print(i)