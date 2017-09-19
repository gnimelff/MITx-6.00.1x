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
