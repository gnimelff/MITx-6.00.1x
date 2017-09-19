'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
'''

vowels = "aeiou"
v = 0									
for c in s:								
    if c in vowels:						
        v += 1							

print("Number of vowels: " + str(v))
