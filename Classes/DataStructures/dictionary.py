a = ['bharath','kumar',25,'Male']

#Dictionary
#key and value
#File format json
a = {}
a = {"firstname":"Bharath",
     "middlename":"Kumar",
     "Age":25,
     "Gender":"male",
     1:20}
#Keys should be unique

#Dictionary is mutable(make alterations)
#Adding new key and value
#dictionary_variable[new_key] = new_value
a['Lastname'] = 'Kalaimani'
print(a)

#Change the value
#dictionary_variable[already_present_key] = new_value
a['firstname'] = 'Bha'
print(a)

#Delete the key value
#del dictionary_variable[already_present_key]
del a['middlename']
print(a)

#deleting dictionary and the variable
# del a
# print(a)


#Ordered(get based on key)
#Iterating
for i in a:
    print(i)
    #dictionary_variable[key]
    print(a[i])

for key,value in a.items():
    print(key,value)

dic = {
        "name":
            {
             "firstname":"Bharath",
             "lastname":"Kumar"
            },
        "Age":
            {
                "age_persin" : 25
            }
        }


# Frontend ---->API(json/dict)----> backend
