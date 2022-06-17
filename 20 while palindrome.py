#20. Write a program to check whether a number is palindrome or not.
a=input("enter number")
n=-1
d=" "
b=0-len(a)
while n>=b:
    c=a[n]
    d=d+c
    n=n-1
print(d)
if int(a)==int(d):
    print("palindrome number")
else:
    print("not palindrome")