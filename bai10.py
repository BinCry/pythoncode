# Hàm kiểm tra số nguyên tố
def is_prime(a):
    if a < 2:               # Số < 2 không phải nguyên tố
        return False
    for i in range(2, int(a**0.5) + 1):  # Kiểm tra ước từ 2 đến căn bậc 2 của n, cộng 1 để bao gồm căn bậc 2 nếu là số nguyên
        if a % i == 0:      # Nếu chia hết thì không phải nguyên tố
            return False
    return True             # Không chia hết cho số nào -> nguyên tố

# Nhập số từ bàn phím và kiểm tra
num = int(input("Nhập số cần kiểm tra: "))
if is_prime(num):
    print(f"{num} là số nguyên tố")
else:
    print(f"{num} không phải là số nguyên tố")

#i = 2 2,02 2,03 
# N=10 thì nó chỉ chạy đến căn bậc 2 của 10 là 3
# Số nguyên tố là số chỉ chia hết cho 1 và chính nó
# Số bé hơn 2 không phải số nguyên tố vì nó không có ước số nào