#8. Write a program to print a table of a number entered from the user.
num=int(input("enter the number"))
a=1
while a<=10:
    print(num,"*",a,"=", a*num)
    a=a+1