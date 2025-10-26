def giaithua(x):
    if x == 0:
        return 1
    else:
        return x * giaithua(x - 1)

n = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", n, "là:", giaithua(n))
