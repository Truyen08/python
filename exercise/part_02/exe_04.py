n = int(input("Nhập n (>0): "))
sum_value = 0.0

for i in range(1, n + 1):
    sum_value += i / (i + 1)

print("Kết quả là:", sum_value)
