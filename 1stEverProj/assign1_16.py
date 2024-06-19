# Write a program in python that counts the frequency of each character in
# a string.

string=input('enter a string')
ans={}
for x in string:
    ans[x]= string.count(x)
print(ans)