import re

text = 'Hello world! Its"s 2025 and regex is fun ... or not?' 

#1.  .(dot) any character except newline
print(re.findall(r'H.l',text))
print(re.search(r'H.l',text))
print(re.match(r'H.l',text))

#2. ^(start of a string)
print(re.findall(r'^Hello',text))
print(re.search(r'^Hello',text))
print(re.match(r'^Hello',text))

#3. $(end of the string)
#4. \(backslash) --> escape the special characters
print(re.findall(r'not\?$',text))
print(re.search(r'not\?$',text))
print(re.match(r'not\?$',text))

#5. *(zero or more) --> 0 or more preceding element
#6. +(one or more) ---> 1 or more preceding element
#7. ?(zero or one) ---> 0 or 1
tes = 'll lol loool looooooooool'
#* = 0 or more
#+ = 1 or more
#? = 0 or 1
print(re.findall(r'lo*l',tes))
print(re.findall(r'lo+l',tes))
print(re.findall(r'lo?l',tes))

#8. [](bracket) --> any one character inside the branket
tes = 'Regex is cool'
print(re.findall(r'[aeiou]',tes))

#9. [^](bracket with negate) --> any one character not inside the branket
tes = 'Regex is cool'
print(re.findall(r'[^aeiou]',tes))

#10. | (or)
tes = 'I like dog'
print(re.findall(r'cat|dog',tes))

#11. {}(exact number)
tes = 'll lol loool looooooooool'
print(re.findall(r'lo{3}l',tes))

#12. \d(digit)
text = 'Hello world! Its"s 2025 and regex is fun ... or not?'
print(re.findall(r'\d',text))
print(re.findall(r'\d+',text))

#12. \D(non digit)
text = 'Hello world! Its"s 2025 and regex is fun ... or not?'
print(re.findall(r'\D+',text))

#13. \w(word) - all words inside the string
text = 'Hello world! Its"s 2025 and regex is fun ... or not?'
print(re.findall(r'\w+',text))

#13. \W(non-word) - gets all punctuations and spaces
text = 'Hello world! Its"s 2025 and regex is fun ... or not?'
print(re.findall(r'\W+',text))


