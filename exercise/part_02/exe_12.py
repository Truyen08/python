#tim cac so' trong khoang? 2000 den 3200 chia het cho 7 nhung khong chia het cho 5
numbers = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        numbers.append(str(i))

print(",".join(numbers))
