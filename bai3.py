# Viết hàm tính lũy thừa x mũ y (không được dùng toán tử **), với x,y nhập từ bàn phím và x,y phải lớn hơn 0 nếu x hoặc y nhỏ hơn 0 thì trả về 0
# or chỉ cần 1 trong 2 còn and là cả 2
def power(x,y):
    if x <= 0 or y <=0: # Kiểm tra điều kiện
        return 0 # Lưu kết quả trả về
    result = 1
    for i in range(y): # Ví dụ 3^2 thì máy tính hiểu là x=3, y=2 sẽ lấy 3 nhân 3 bấy nhiêu lần
        result = x * result
    return result
# Chương trình chính (hàm main c++)
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print(power(x,y))


#3
#3*3
#3*3*3