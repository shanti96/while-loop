#19. Write a program to add first n terms of the following series using a while loop :
#1/1! + 1/2! + 1/3! + …….. + 1/n!
i=int(input("enter the number"))
n=1
while n<=i:
    print(1,'/',n,"!", "+",end=" ")
    n=n+1