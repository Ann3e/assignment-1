# Write a python program that calculates the sum of the digits of a given
# number

enter= int(input('enter a number'))
sum=0
while enter>0:
    sum=sum+enter%10
    enter=enter//10
print(sum)