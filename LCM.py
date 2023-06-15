x=int(input('enter number='))
y=int(input('enter number='))
if x>y:
    b=x
else:
    b=y
while(True) :
    if b%x==0 and b%y==0:
        lcm=b
        break
    b+=1 
print('LCM is =',lcm)                 