#while loop statement
#example_01
count = 1
while count < 5:
    print(count)
    count +=1


# total statement:
'''
while <condition>:
    -->body of while loop <--
'''

# --> while loop is diffirent with For loop because it don't know number of repetition

#exercise: calculate total from 1 to n (n is number which user enter from keybo)
n = int(input("enter a number: "))
total = 0
count = 1
while count <= n:
    total +=count 
    count +=1
print(total)