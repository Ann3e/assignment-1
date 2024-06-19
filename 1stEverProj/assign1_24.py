# Write a program that acts as a simple calculator. It should take two
# numbers and an operator (+, -, *, /) as input and print the result.


no1= int(input('enter first number'))
no2= int(input('enter second number'))
print('enter + for addition')
print('enter - for subtraction')
print('enter * for multiplication')
print('enter / for division')
check='y'
while(check=='y'):
    sign = input('enter operator')

    if(sign=='+'):
        print(no1+no2)
    elif(sign =='-'):
        print(no1-no2)
    elif(sign=='*'):
        print(no1*no2)
    elif(sign=='/'):
        print(no1/no2)
    else:
        print('invalid operator')
    check=input('do u want to continue (y/n)')

