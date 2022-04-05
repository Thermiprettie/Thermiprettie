#import datetime
#import random

#x = datetime.datetime.now()
#print (x)
#print(x.year)
#print (x.strftime("%A"))
#print (x.strftime("%B"))

from random import randint
#y=input("Enter your first num:")
#x=input("Enter your second num:")
#print(y)
#print(x)
y=randint(1,100)
x=randint(1,100)
print("your first number is:", x)
print("your first number is:", y)
v=input("what is your answer?: ")
c=y+x

if c == int(v):
    print("correct")
else:
    print("You dont know a thing")