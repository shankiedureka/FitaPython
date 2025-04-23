#regular expression or regex are sequence of characters that is used to
# define search patterns for string manipulation and matching

#email ---> <name>@<domain>.<com,in,org>
#pass ---> Aa@1
#phone ---> 10 (9,8,7,6)

#qwert
#1st character of your name

#Functions in regex
#findall()
#search()
#match()


#Meta characters which 
#image or video file ---> image , extension(.jpg,jpeg,png),size,resolution

#master computer
#workers
#computer computer computer

#user_1 ---> master(metadata--> user,worker_id) ---> worker_1
#user_2 ---> master ---> worker_2

import re

#^ --> start of a string
s = 'Hello world'
#re.search(<pattern>,text)
pattern = r'^Hello'
output = re.search(pattern,s)
print(output)

# $--> checks end of a string
s = 'Hello world'
pattern = r' world$'
output = re.search(pattern,s)
print(output)

#. --> wildcard(any characters)
#cat, cut, cot
text = "cat, cut, cot"
pattern = r'c.t'
output = re.findall(pattern,text)
print(output)
output = re.search(pattern,text)
print(output)
output = re.match(pattern,text)
print(output)

#findall ---> gives all possible results in the string in list
#search ---> return the 1st match in the string(it can be anywhere
#            in the string)
#match ---> return only if the 1st word or character matches

#if the name has mr mrs --> match()
#validate the country code of phone number --> match()
#log file, i wanted check where is the keyword error ---> search()
#list all the errors in the file ---> findall()



#strat the program
#entered into main
#error ---> some issue found
#error --> some issue also found