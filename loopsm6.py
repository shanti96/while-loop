i=2
a=int(input("enter number"))
while i<=a//2:
  if a%i==0:
    print(a,"is not prime number")
    break
  i=i+1
else:
    print("prime number is ",a)  