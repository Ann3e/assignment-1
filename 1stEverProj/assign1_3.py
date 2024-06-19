#  Write a python program that calculates the factorial of a given number.
number = int(input("enter number to calculate factorial"))
fac = 1
while number!=0:
    fac=number*fac
    number=number-1
print(fac)