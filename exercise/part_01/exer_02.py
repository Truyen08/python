data = "truyennt.22ns@gmail.com"
position = data.find("@")
host = data[position + 1:]
print("Host name:", host)
