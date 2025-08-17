# Nhập N từ bàn phím
N = int(input("Nhập vào N: "))
# Kiểu my_dict
my_dict = {}
for i in range(1, N+1):
    my_dict[i] = i * i
# In ra từ điển
print(my_dict)