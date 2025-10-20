st = input("Nhập chuỗi gốc: ")
st_search = input("Nhập chuỗi cần tìm: ")

if st_search in st:
    print("Đã tìm thấy tại vị trí:", st.find(st_search))
else:
    print("Không tìm thấy")
