# Write a python program that checks if two strings are anagrams of each
# other.

string1=sorted(input('enter string 1'))
string2=sorted(input('enter string 2'))
if string1==string2:
    print('the two strings are anagrams of each other')
else:
    print('no they arnt anagrams')