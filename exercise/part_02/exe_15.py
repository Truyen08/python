data = input("Nhập các số, cách nhau bằng dấu phẩy: ")
list_data = data.split(",")     #ham` split de` tach chuoi~ thanh` list 
tuple_data = tuple(list_data)

print("Danh sách:", list_data)
print("Tuple:", tuple_data)
