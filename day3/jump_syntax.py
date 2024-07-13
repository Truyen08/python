#fisrt is "Break statement"
#it use to immediately exit the loop block
count = 0
while count <= 10:
    print(count)
    if count == 5:
        break
    count +=1


#second is "continue statement"
#--> it will jump to the next command but it doesn't exit the loop block
n = 0
while n < 8:
    n +=1
    if n == 4 or n == 7:
        continue
    print(n)