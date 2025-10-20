#tinh' trung binh` cac' so' nhap vao
total = 0
count = 0

while True:
    inp = input("Nhập số (hoặc 'done' để kết thúc): ")
    if inp.lower() == "done":
        break
    value = float(inp)
    total += value
    count += 1

if count > 0:
    print("Giá trị trung bình:", total / count)
else:
    print("Chưa nhập số nào.")
