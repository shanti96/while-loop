#35. Write a program to print all the factors of 
# a number using a while loop .
i=int(input("enter the number"))
n=1
while n<=i:
    if i%n==0:
        print(n,end=",")
    n+=1    