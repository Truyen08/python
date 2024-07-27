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

# in this eg, "return" keyword returns a value to the function after the function performs 
#   a calculation of logic. that value of Function can be stored for future use.
# !!! --> after 'return' keyword, any code after that not executed


# ------------------------

# the pass statement
# purpose: preventing errors from empty code blocks 

def future_code():
    pass

future_code()


# some python library functions 
import math # import math moldule

square_root = math.sqrt(9)

print('square root of 9 is', square_root)

power_num = math.pow(2, 3)

print('2 to the power 3 is',power_num)


# ---------------------

num1 = float(input("nhap so thu nhat: "))
num2 = float(input("nhap so thu hai: "))

result_of_sum = sum([num1, num2])   # sum() is used for list or tuple,. you need to add them to the list 
print("total is: ", result_of_sum)

result_of_sum = sum([num1, num2], 10)   # start the calculation with initial value of 10



# read more : https://www.programiz.com/python-programming/methods