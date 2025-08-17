# Hàm tính đệ quy Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
# Phần chạy chương trình 
n =  float (input("Nhập số n: "))
print(fibonacci(n)) # In ra màn hình kết quả


