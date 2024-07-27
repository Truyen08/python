# function? : simply is block of code that performs a specific tack.
# create a first function: 
def good():
    print("hello world!")

    '''
    - def : keyword to create function
    - good: name of function you want 
    - print ...: body of function
    ''' 

#   to use this function, we need to call the function
good()  #output: hello world

# -----------------------
def hello (name):
    print ('hello', name)

hello("ThanhTruyen")

# in above example, ThanhTruyen is passed as an argument to the hello() function
hello("VietNam") #output : hello VietNam


# -----------------------
#ex:
def add_twoNum(a, b):
    total = a + b
    print('total is ', total)

add_twoNum(4, 5)

# notice: 
'''
    - a, b: it's parameters: the actual value is not specified 
            ("gọi tắt là tham số - parameter")
    - 4, 5: it's arguments: the actual value which is passed to the function when it called
            ("gọi tắt là đối số - argument  ") 
'''

# ------------------------
# the return statement
#eg: 
def find_square(number):
    result = number * number
    return result

square = find_square(3)

print('square', square)

