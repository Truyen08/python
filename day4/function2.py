# we will learn more about arguments in python
#eg_01:

def add_number(a = 2, b = 3):
    sum = a + b
    print('sum', sum)

#with 2 argument
add_number(7, 8)    #outp: 15

# with 1 argument
add_number(b = 8)   #outp: 10

# function call with no argument
add_number()        #outp: 5


print('------------------------------------')

#eg_02:

def full_info(first_name, last_name):
    print('first_name is ', first_name)
    print('last_name is ', last_name)

#function call
full_info(last_name = 'ThanhTruyen', first_name = 'Hello python')
# ---> the positon of arguments doesn't matter


print('------------------------------------')


# arbitrary argument
#eg_03
#calculate a sum of multiple number
def multi_num(*number):
    total = 0

    for num in number:
        total = total + num
    
    print('total is ', total)

multi_num(1, 2, 3, 4, 5)    

'''
    - in this kind of situation, argument in above eg has many number. you can understand that like a list and * help parameter name
        understand that list is also a type of argument

    - asterick(*) before parameter name is denote this kind of argument 
        and you are able to use 'for loop' to read each value 
'''


print('------------------------------------')

# recursive function
# simple like this --> a function that calls another functions or calls itself 
#                   ==> that is a recursive function

#eg:
'''

def recurs():
    # ...
    recurs()

recurs()

'''

# ex: factorial of number (input from user) using recurse
number = int(input('nhap so nguyen duong :'))

if number < 0:
    print('invalid number!')
elif number == 0:
    print('factorial of', number, 'is', 1)
else:
    
    def factorial(number):
        if number == 1:
            return 1
        else:
            return(number * factorial(number - 1))
    
    total = factorial(number)
    print('factorial of', number, 'is', total)


'''
logic: 
eg number = 3
factorial(3) = 
3 * fac(2)      -> call fac(2) == 2 * fac(1)
3 * 2 * fac(1)  -> call fac(1)  ==> number =1 --> return 1
3 * 2 * 1
3 * 2
6 

**: using return function --> store the value of function(x) --> for future use

'''