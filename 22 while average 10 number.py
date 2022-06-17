#22. Write a program to accept 10 numbers from 
# the user and display it’s average.
n=1
p=0
while n<=10:
    s=int(input("enter the number"))
    p=p+s
    n=n+1
print(p)
a=p/10
print(a)    