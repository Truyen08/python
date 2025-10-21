#nhap ki' tu. or chuoi~ --> luu vao' list --> in ra moi~ chuoi~ 1 line
lines = []

while True:
    s = input("Nhập dòng (Enter trống để dừng): ")
    if not s:
        break
    lines.append(s.upper())

print("Kết quả:")
for line in lines:
    print(line)
