#Read the file
#open the file

#file_variable(object) = open(<filepath>,<typeofOperation>)
#r - read
#w - write
#a - append
#need to close the manually
f = open('E:/Git/FitaPython/Classes/file_handling/sample.txt','r')
data = f.read()
print(data)
f.close()
f = open('E:/Git/FitaPython/Classes/file_handling/sample.txt','r')
data = f.readlines()
print(data)
f.close()

#file close is done automatically
#with open(<filepath>,<typeOfOperation>) as <file_variable(object)>:
    #read or write
with open('E:/Git/FitaPython/Classes/file_handling/sample.txt','r') as f:
    data = f.read()
print('Done')

