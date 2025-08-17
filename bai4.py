# Nhập 2 chuỗi từ bàn phím, nối chuỗi và in kết quả
# Kiểu dữ liệu chuỗi là string viết tắt khai báo trong python là str

# Nhập từ bàn phím
a = str (input ("Nhập chuỗi thứ 1: "))
b = str (input ("Nhập chuỗi thứ 2: "))
# Nối chuỗi
result = a + " " + b
# In ra màn hình chuỗi
print ("Chuỗi sau khi nối là: ", result)

# In ra màn hình độ dài chuỗi
print ("Độ dài chuỗi là: ", len(result))    # Độ dài chuỗi viết tắt là length trong py ghi là len

# Mở rộng đảo chuỗi
result1 = result[::-1]
print ("Chuỗi sau khi đảo là: ", result1)

# " " là khoảng trắng
# result[::-1] chuỗi đảo
