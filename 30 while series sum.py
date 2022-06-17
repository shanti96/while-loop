#30. Write a program to find the sum of following series
#1 + 8 + 27 …………n terms

n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    p=i**3
    sum=sum+p
    print(p, "+",end="")
    i=i+1
print(sum)    