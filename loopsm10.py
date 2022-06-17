num=5
a=1
while a<=10:
   gess=int(input("gesses the number")) 
   if gess<=10 and gess >=1:
       if gess==5:
        print("wow you guessed the correct number")
        break
       if gess<5:
          print(gess,"its lessthan")
          print("try again")
       if gess>5:
           print(gess,"its greaterthan")
           print("try again")
       if a==5:
          print("your 5 chance are finish")
          break
   else:
       print("gesses is wrong")
   a=a+1