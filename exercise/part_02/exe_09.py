my_str = input("Nhập câu: ")
words = my_str.split()  # tách thành danh sách từ
words.sort()            # sắp xếp theo alphabet

print("Các từ sau khi sắp xếp:")
for w in words:
    print(w)
