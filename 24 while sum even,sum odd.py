#24. Write a program to display sum of odd numbers and
# even numbers separately that fall between two
#numbers accepted from the user.(including both numbers) 100 and 500.
i=int(input("enter the number"))
p=int(input("enter the number"))
s=0
n=0
while i<=p:
    if i%2==1:
        s=s+i
    elif i%2==0:
        n=n+i
    i+=1    
print("total sum of odd number=",s) 
print("total sum of even number=",n)