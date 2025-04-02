# 0 1 1 2 3 5 8 13 21 
number_of_fibo = int(input())
first = 0
second = 1
count = 2
print(first)
print(second)
while count < number_of_fibo:
    next = first+second
    print(next)
    first = second
    second = next
    count += 1



