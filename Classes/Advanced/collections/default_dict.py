from collections import defaultdict
#default dict is used assign some default values to the key, if it is
#not present inside the dictionary

# s = {'apples':10, 'banana':5, 'guava':3}

# print(s['apples'])
# print(s['banana'])

# print(s['mango'])

def_dict = defaultdict(str)
def_dict['apple'] = 10
def_dict['banana'] = 5
def_dict['guava'] = 3
print(def_dict)

print(def_dict['apple'])
print(def_dict['banana'])

print(def_dict['mango'])


