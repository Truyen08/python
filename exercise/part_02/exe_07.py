num = int(input("Nhập số cần kiểm tra: "))
level = int(input("Nhập bậc (thường là 3): "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** level
    temp //= 10  # chia lấy phần nguyên

if total == num:
    print(num, "là số Amstrong")
else:
    print(num, "không phải số Amstrong")
