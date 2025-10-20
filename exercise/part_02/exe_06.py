st = input("Nhập câu của bạn: ")

sum_upper = 0
sum_lower = 0

for c in st:
    if c.isupper():
        sum_upper += 1
    elif c.islower():
        sum_lower += 1

print("Số chữ HOA:", sum_upper)
print("Số chữ thường:", sum_lower)
