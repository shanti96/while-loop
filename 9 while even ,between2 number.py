#9. Write a program to display all even numbers that fall between two 
# numbers (exclusive both numbers)entered by the user.

num1=int(input("enter the number"))
num2=int(input("enter the second number"))
while num1<=num2:
    if num1%2==0:
        print("even number",num1)
    num1=num1+1    