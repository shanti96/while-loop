a=1
b=0
while a<=11:
    c=int(input("enter the weight"))
    b=b+c
    a=a+1
avareage=b//11
if avareage%5==0:
    print(b,avareage,"divisible by 5")
else:
    print(b,avareage,"not are divisible")    