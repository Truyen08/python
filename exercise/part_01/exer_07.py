import math


#nhap. canh. tam giac
a = float(input("nhap. do dai canh. so' 1 (a): "))

b = float(input("nhap. do dai canh. so' 2 (b): "))

c = float(input("nhap. do. dai` canh. so' 3 (c): "))

#nhap. 3 goc' cua? tam giac'
goc_C = float(input("Nhập số đo góc giữa a và b (đơn vị độ): "))
goc_B = float(input("Nhập số đo góc giữa a và c (đơn vị độ): "))
goc_A = float(input("Nhập số đo góc giữa b và c (đơn vị độ): "))


#in ra man hinh dien tich tamgiac 
dien_tich_S_cach_01 = (a * b * math.sin(math.radian(goc_C)))/2

dien_tich_S_cach_02 = (a * c * math.sin(math.radian(goc_B)))/2

dien_tich_S_cach_03 = (b * c * math.sin(math.radian(goc_A)))/2

print("dien tich tam giac cach 01 la: ", dien_tich_S_cach_01)

print("dien tich tam giac cach 02 la: ", dien_tich_S_cach_02)

print("dien tich tam giac cach 03 la: ", dien_tich_S_cach_03)