#11. Write a program to find the sum of the digits of 
# a number accepted from the user.
num=input("enter the number")
a=0
sum=0
while a<len(num):
    i=int(num[a])
    sum=sum+i
    a=a+1
print(sum)    