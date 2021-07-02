#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print: 
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

A = ''
B = ''
C = ''

for i in s:
    if A <= i:
        A = i
        B = B + A
        if len(B) > len(C):
            C = B
    else:
         A = i
         B = A
print("Longest substring in alphabetical order is:" + C)
