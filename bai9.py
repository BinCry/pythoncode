# Mở file input.txt để đọc
with open("input9.txt", "r", encoding="utf-8") as f: # utf-8 là chuẩn đọc file để không bị lỗi ký tự
    N = int(f.readline().strip())  # Đọc số lượng sinh viên
    students = []                  # Danh sách lưu thông tin sinh viên
    
    # Đọc N dòng thông tin sinh viên
    for i in range(N):
        line = f.readline().strip()   # Đọc 1 dòng, strip dùng để loại bỏ khoảng trắng đầu và cuối
        mssv, ten, lop = line.split()  # Tách thành 3 phần
        students.append((mssv, ten, lop))  # Thêm vào danh sách

# Xuất ra màn hình
print("Danh sách sinh viên:")
for mssv, ten, lop in students:
    print(f"MSSV: {mssv}, Tên: {ten}, Lớp: {lop}")
