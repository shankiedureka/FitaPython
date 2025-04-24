import re

#1. Validate email address
email = "some-one@example.com"
"some.one@example.com"
"some-one@example.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
print(re.match(pattern,email))


#validate a phone number
phone = "9777777777"
pattern = r'^[6-9]\d{9}$'
print(re.match(pattern,phone))