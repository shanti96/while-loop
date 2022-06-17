#33. Write a Program to print all the characters in 
#the string ‘COMPUTER’ using a while loop .
i=input("enter the characters")
n=0
s=""
while n<len(i):
    p=i[n]
    s=s+p
    n=n+1
    print(p)    