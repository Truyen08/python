#integer variable : it's represented using the int() funtion. 
#  in python 3.x.x, as long as you have enough memory, it don't have a limit
#eg: 
age = 25

#float variable: it's represented using the float() funtion
#eg: 
pi = 3.14  
pen = 25.7


#boolean variable: use to store either True or False values

my_num = 2+3 == 5   # True
my_bool = not True  # False
is_raining = True

#string  variable: use to store Text data
#eg: 
name = 'Truyen'
chat = "hello world!" 
var = '''
    hello world!
    welcome to my home!
    ThanhTruyen
'''
print("world: ", chat[6:11]) # print only 'world'
 # or update string 
print(chat[:6] + 'python')  # OUTPUT: hello python



#list variable : 
# using square brackets [] in statement
#   eg:
color = ['yellow', "red", "blue"]
number = [1, 2, 3, 4, 5, 6]


#tuple variable
'''
 it's similar to a list variable, BUT:
    -  it is immutable, which means it cannot be changed once created
    - using Parentheses () in statement
'''
coordinate = (10, 20)
fruit = ('mango', 'banana', 'strawberry')


#dictionary variable:
'''
    - it's used to store key-value pairs    
    - using curly braces {} in statement
'''
person = {'name' : 'Truyen', 'age' : 21, 'height' : 170 }
scores = {'math' : 10, 'physic' : 9, 'english' : 9}
# print(person)





#       -->     type conversion     <--


# 1. implicit type convertion : it means swiching during compilation
#   or during the runtime 

#eg: 
a = 5
b = 6.5
sum = a + b
print (sum) #output:  11.5
print (type(sum))   # output: float
# -->type funtion is used to display the datatype of a variable
# --> python always converts smaller datatypes into larger datetypes to prevent the loss of data


#2. explicit type convertion
a1 = 100
b1 = "200"
#   total_01 = a1 + b1      # error
b2 = int(b1)
total_02 = a1 + b2
print(total_02)     # output: 300


#-->? Summary:
'''
    + Implicit type conversion is performed by a Python interpreter only.
    + explicit ....  ...        is performed by user by  explicitly using type conversion functions
    + when performing implicit type casting, avoids the loss of data.
'''