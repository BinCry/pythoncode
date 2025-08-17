# Mở file input.txt để đọc dữ liệu
with open('input7.txt', 'r') as f:
 N = int(f.readline().strip()) # Đọc số nguyên N từ dòng đầu tiên, strip() loại bỏ khoảng trắng
 heso = list (map(int, f.readline().strip().split(","))) # Đọc hệ số từ dòng thứ hai, split(",") tách chuỗi thành danh sách

 # Tạo chuỗi để biểu diễn đa thức 
bieudien = "P(x) = "

# Giải thuật
for i in range (N,-1,-1):
       hesohientai = heso[i] # Duyệt từ bậc cao nhất đến bậc thấp nhất
       if hesohientai != 0:
            if i == 0:
                bieudien += f"{hesohientai}" # Số hạng tự do
            elif i == 1:
                bieudien += f"{hesohientai}x + "
            else:
                bieudien += f"{hesohientai}x^{i} + "
# Mở output.txt và ghi kết quả
with open('output7.txt', 'w') as f:
    f.write(bieudien)
# In ra màn hình
print(bieudien)
# Ví dụ
# Đầu vào:
# 3
# 1,2,3,4
# Đầu ra:
# P(x) = 1x^3 + 2x^2 + 3x + 4
