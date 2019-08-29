# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

first_letter = 0
length = 1
longest = 1

for i in range(len(s) -1 ):
    if s[i + 1] >= s[i]:
        length += 1
    else:
        length = 1

    if length > longest:
        longest = length
        first_letter = i + 2 - longest

print("Longest substring in alphabetical order is: " + s[first_letter:(first_letter + longest)])


_________________

start = 0
count = 0
longestString = s[0]
testString = ''

for letter in range(len(s) -1):
  if s[letter + 1] >= s[letter]:
    count += 1
    testString = s[start:(start+(count+1))]
    if len(testString) > len(longestString):
      longestString = testString
  else:  
    count = 0
    start = (letter + 1)

print('Longest substring in alphabetical order is: ' + longestString)
