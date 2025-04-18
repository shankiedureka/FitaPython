from collections import Counter

words = ['apple','banana','apple','orange','banana','mango']
words = ('apple','banana','apple','orange','banana','mango')
fruits = Counter(words)
print(fruits)

# temp = {}
# for i in words:
#     if i in temp:
#         temp[i] = temp[i] + 1
#     else:
#         temp[i] = 1
# print(temp)