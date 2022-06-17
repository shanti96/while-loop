#17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
#equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)

a=input("enter the number")
a1=int(a)
b=len(a)
c=0
n=0
while c<b:
    n=(int(a[c]))**b+n
    c=c+1
if a1==n:
    print("its armstrong number",n)
else:
    print("its not are armstrong number",n)       