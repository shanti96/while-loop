#38.Write a Python program to find those numbers which are divisible
# by 7 and multiple of 5, between 1500 and 2700 (both included).
n=1500
i=2700
while n<=i:
    if n%7==0:
        print(n,"7 by divisible")
    if n%5==0:
        print(n,"5 by multipels")
    n+=1        
