#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.

count = 0                   
start = 0                   
for letter in range(len(s[:-2])):
    if s[start:(start+3)] == "bob":
        count += 1
        start += 1
    else: 
        start += 1

print("Number of times bob occurs is: " + str(count))