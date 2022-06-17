#36. Accept two numbers from the user and display sum of 
# even numbers between them(including both)

i=int(input("enter the number"))
n=int(input("enter the number"))
p=0
while i<=n:
    if i%2==0:
        p=p+i
        print(p)
    i=i+1    