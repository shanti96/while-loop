#15. Write a program to print the Fibonacci series 
# till n terms (Accept n from user)
a=int(input("enter the number"))
i=1
f1=0
f2=1
f3=0
while i<=a:
    print(f3,",",end="")
    f1=f2
    f2=f3
    f3=f1+f2
    i+=1