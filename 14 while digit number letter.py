#14. Write a program to display the number names of the digits of if the number is 231 then output should be
#Two a number entered by user,for example Three One
num=input("enter the number")
b=0
while b<len(num):
    s=int(num[b])
    if s==0:
        print("zero")
    elif s==1:
        print("one")
    elif s==2:
        print("two")
    elif s==3:
        print('three')
    elif s==4:
        print("four")
    elif s==5:
        print("five")
    elif s==6:
        print("six")
    elif s==7:
        print("seven")
    elif s==8:
        print("eight")
    elif s==9:
        print("nine")
    b=b+1                                            
