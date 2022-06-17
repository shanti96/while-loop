#39.Write a Python program to guess a number between 1 to 9
guess=6
i=1
while i<=9:
    n=int(input("enter the number"))
    if n==guess:
        print("your guesse are right")
        break
    elif n!=guess:
        print("guesse are not right")
    i+=1