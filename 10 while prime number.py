#10. Write a program to check whether a number is prime or not.
num=int(input("enter the number"))
a=2
while a<=num//2:
    if num%a==0:
        print("not prime number",num)
        break
    a=a+1
else:
    print("its prime number",num)        