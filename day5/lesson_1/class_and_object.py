#first step of OOP in python

'''
oop python:

- class(chỉ có sườn, nói chug chug, chưa có data cụ thể):
	+ phương thức (method)	(hàm mô tả hành vi dữ liệu)
	+ thuộc tính (biến lưu trữ các đặc điểm dữ liệu)

- object(ob là trường hợp cụ thể hơn của class):
	+ phương thức
	+ thuộc tính

'''
#----------------------------------------------------------------------
#định nghĩa lớp
class car:      # define class car
    def __init__(self, c, num):     #dùng def init để ta khai báo thuộc tính của class
        self.color = c
        self.numberWheels = num
    def start_car(self):                #nếu phương thức kh có tham số thì phải có "self" ở trong
        print("--> car is starting")

#định nghĩa lớp có 2 phương thức (2 def) và 2 thuộc tính (self.color, self.numberWheels)
# c và num là tham số á 

# hàm __init__ và tham số self là hàm khởi tạo (constructor) 

#--> bắt buộc phải có mỗi khi định nghĩa class



#----------------------------------------------------------------------
#muốn dùng class --> ta phải khởi tạo object(đối tượng) từ class đó
my_car = car("blue", 4)     # -> TẠO object tên my_car từ class car

print("màu xe của tôi là: ", my_car.color)        #truy cập thuộc tính color của object my_car

my_car.start_car()               # -> GỌI phương thức start_car của object my_car




