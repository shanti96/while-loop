#21. Write a python program to sum the sequence:
#1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!
i=int(input("enter the number"))
p=1
n1=0
n2=0
n3=1
print(1,"+",end="")
while p<=i:
    n1=n2
    n2=n3
    n3=n1+n2
    p=p+1
    print("1","/",n3,"!","+",end="")