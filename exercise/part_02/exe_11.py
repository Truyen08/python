#nhap nhieu so, luu chung' vao` danh sach'  va tinh trung binh
num_list = []

while True:
    inp = input("Nhập số (hoặc 'done' để kết thúc): ")
    if inp.lower() == "done":
        break
    num_list.append(float(inp))

if len(num_list) > 0:
    average = sum(num_list) / len(num_list)
    print("Trung bình:", average)
    print("Danh sách:", num_list)
else:
    print("Không có dữ liệu để tính.")
