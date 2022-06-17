#13. Write a program to reverse the number accepted by the user.
a=input("enter the number")
b=len(a)
c=0
while c<len(a):
    b=b-1
    s=int(a[b])
    print(s,end="")
    c=c+1