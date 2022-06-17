a=1
while a<=100:
    if a%3==0:
        print("Nav")    
    elif a%7==0:
        print("Gurukul")
    elif a%3==0 and a%7==0:
        print("NavGurukul")
    elif a%3!=0 and a%7!=0:
        print(a)    
    a=a+1            