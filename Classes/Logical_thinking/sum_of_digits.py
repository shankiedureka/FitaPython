#First do modulo operation of a number with 10 --> you get last digit
#Then change the number to quotient value(do floor division with 10)

a = int(input('Enter the number : '))
original = a
sum_of_digits = 0
while a>0:
    digits = a%10
    sum_of_digits += digits
    a = a//10
print(sum_of_digits)
