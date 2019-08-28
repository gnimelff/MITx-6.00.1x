#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.

bobCount = 0

for i in range(len(s)):
  if s[i:i+3] == 'bob':
    bobCount += 1

print('Number of times bob occurs is : ' + str(bobCount))
