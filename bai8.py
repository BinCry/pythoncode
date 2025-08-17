# Mở file input.txt và đọc toàn bộ nội dung
with open("input8.txt", "r") as f:
    arr = list(map(int, f.read().split()))  # Đọc các số và chuyển sang list int

# Tính tổng các phần tử là số chẵn
tongcacsochan = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        tongcacsochan += arr[i]

# b. Đếm số phần tử âm
demsoam = 0
for i in range(len(arr)):
    if arr[i] < 0:
        demsoam += 1
# c. Tính tổng các phần tử là số lẻ
tongcacsole = 0
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        tongcacsole += arr[i]
# d. Đếm số phần tử dương
demsoduong = 0
for i in range(len(arr)):
    if arr[i] > 0:
        demsoduong += 1
# e. Tính trung bình cộng các số dương
if demsoduong > 0:
    tongduong = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            tongduong += arr[i]
    trungbinhcong = tongduong / demsoduong
else:
    trungbinhcong = 0

# In kết quả
print("Tổng các số chẵn:", tongcacsochan)
print("Số lượng phần tử âm:", demsoam)
print("Tổng các số lẻ:", tongcacsole)
print("Số lượng phần tử dương:", demsoduong)