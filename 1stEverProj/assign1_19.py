# 19. Write a python program that removes all punctuation from a given string.

string =eval(input('enter a string to remove puntuation'))
for x in string:
    if x in ['!','&','?','@',"'"]:
        string.replace(x," ")
print(string)