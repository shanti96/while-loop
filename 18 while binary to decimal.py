#18. Write a program to convert binary to decimal.
a=input('enter the number')
b=len(a)
b=b-1
c=0
b1=0
i=1
while b>=c:
    n=int(a[b])
    b=b-1
    if n==1:
        b1=b1+i
    i=i*2    
print(b1)