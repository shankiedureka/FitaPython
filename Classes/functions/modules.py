#Modules mean reusing or importing already present code

#three types
#user defined
#inbuilt
#external

#user defined ---> importing the function which is been developed or written
#by me or my teammates

#from <filename> import <function>
#* --> importing all functions from a file
#for specific function import by function name
from calculator_file import calculator
from contional_flow.if_else import *

result = calculator(1,2,'+')
print(result)