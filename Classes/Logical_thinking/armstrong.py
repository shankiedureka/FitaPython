#123 ==> 1,2,3
#length = 3
#1pow3, 2pow3, 3pow3
#add all 
#if i get same number 123, then it is armstrong

a = int(input('Enter the number : '))
original = a
power = len(str(original))
sum_of_digits = 0
while a>0:
    digits = a%10
    digits = digits**power
    sum_of_digits += digits
    a = a//10
if sum_of_digits == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")



