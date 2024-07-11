# here is loop statement (for and while)

# first is for loop?
# with list

languages = ('python', 'c++', 'java')
for x in languages:
    print(x) 


#or
for n in range(4):
    print(n)



print('-----------')
# and with string:
name = 'Truyen'
for character in name:
    print(character)


# execise for For_Loop: calculate a factorial of non-negative number
# example: input:5 --> output: 120

num = 5
total = 1
for i in range(4):
    total *= num
    num = num - 1
print(total)
    
# or using factorial funtion