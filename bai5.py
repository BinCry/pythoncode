# Xóa hai phần tử trùng nhau của một tập hợp cho trước

# Nhập từ bàn phím
a = set (map (int, input ("Nhập các phần tử cho tập hợp (cách nhau bởi dấu cách): ").split ()))
b = set (map (int, input ("Nhập các phần tử cho tập hợp (cách nhau bởi dấu cách): ").split ()))

# Tìm hai phần tử trùng nhau
common = a & b # Trong tử & trả về giao của 2 tập hợp

# Xóa các phần tử trùng nhau
a = a - common # Trong toán tử -= sẽ xóa các phần tử trùng nhau trong tập hợp a
b = b - common # Trong toán tử -= sẽ xóa các phần tử trùng nhau trong tập hợp b
# a = a - common

# In kết quả
print ("Tập hợp a sau khi xóa các phần tử trùng nhau là: ", a)
print ("Tập hợp b sau khi xóa các phần tử trùng nhau là: ", b)
