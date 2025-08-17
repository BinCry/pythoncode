# Bài 1 biết viết hàm và sử dụng hàm , in ra màn hình kết quả, biết viết input 

# Hàm in ra số lớn hơn trong hai số a,b nếu bằng in số nào cũng được
def printMax(a,b): # Hàm so sánh hai số truyền vào hai tham số a,b
    if a > b:
        print (a)
    elif a < b:
        print (b)
    elif a == b:
        print (a)
#Phần chạy chương trình
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
printMax(a,b)



