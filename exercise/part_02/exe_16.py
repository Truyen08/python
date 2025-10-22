n = int(input("Nhập n: "))
d = {}

for i in range(1, n + 1):
    d[i] = i * i

print( f"Từ điển có {n} phần tử:", d)   
        
# f có nhiệm vụ nói rằng chuỗi trong "" hoặc ''
# có thể chứa các biểu thức bên trong dấu ngoặc nhọn {} và 
# cần được thay thế bằng giá trị thực khi in ra
