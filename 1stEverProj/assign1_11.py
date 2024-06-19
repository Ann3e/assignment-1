# Write a python program that generates the first n numbers in the
# Fibonacci sequence.


n =int(input('enter n for fibonacci sequence '))
if(n==1):
    print(1)
if(n==2):
    print(1)
    print(1)
else:
    print(1)
    print(1)
    fib=1
    add=1
    while(n>0):
        ans=fib+add
        add=fib
        fib=ans
        print(ans)
        n=n-1
