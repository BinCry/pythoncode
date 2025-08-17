 # Bài 2: Kiểm tra chuỗi Palindrome: Nhập một chuỗi từ bàn phím, kiểm tra xem chuỗi đó có phải là palindrome (đọc xuôi và ngược giống nhau) hay không.

def kiemtrachuoi(s):
    # Loại bỏ khoảng trắng và chuyển về chữ thường
    s = s.replace(" ", "").lower()  
    # Kiểm tra xem chuỗi có giống với chuỗi đảo ngược của nó không
    if s == s[::-1]:
        return True
    return False

# Nhập chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ")
if kiemtrachuoi(chuoi):
    print("Đây là chuỗi Palindrome.")
else:
    print("Đây không phải là chuỗi Palindrome.")