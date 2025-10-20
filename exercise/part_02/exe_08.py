#xoa ki tu dac biet trong chuoi
chars_remove = """!()-[]{};:'"\\,<>./?@#$%^&*_~"""
my_str = input("Nhập chuỗi: ")

result = ""
for char in my_str:
    if char not in chars_remove:
        result += char

print("Chuỗi sau khi loại bỏ ký tự đặc biệt:")
print(result)
