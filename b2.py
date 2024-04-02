import random

# Bài 2. Viết chương trình nhập một số tự nhiên ngẫu nhiên n (n  (10, 100)) và
# tính các giá trị sau:
# a) Tính tổng và in ra các số nguyên tố nhỏ hơn n.
# b) Tính tổng của tất cả các ước số của n.
# c) Tính tổng các số lẻ từ 1 đến n bằng hai cách: sử dụng vòng lặp for và
# vòng lặp while.
print()
print("BÀI 2")
# Nhập N ngẫu nhiên từ 1 -> 100
n = random.randint(10, 100)
print(f'Số n sau khi chọn ngẫu nhiên là : {n}')

def tongvasoNguyento(n):
    tong = 0
    print("Các số nguyên tố nhỏ hơn", n, "là:")
    for num in range(2, n):
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            tong += num
            print(num, end=" ")
    print("\nTổng các số nguyên tố là:", tong)

def tongUocso(n):
    """Hàm này trả về tổng các ước số của n."""
    tong_uoc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc

def tongLefor(n):
    tong = 0
    for i in range(1, n + 1, 2):  # Bắt đầu từ 1, tăng mỗi lần 2 đơn vị (bỏ qua các số chẵn)
        tong += i
    return tong

def tongleWhile(n):
    tong = 0
    i = 1
    while i <= n:
        tong += i
        i += 2  # Tăng i lên 2 để luôn duy trì i là số lẻ
    return tong
tongvasoNguyento(n)
print("Tổng ước số của n là: ", tongUocso(n))
print("Tổng các số lẻ từ 1 đến", n, "sử dụng vòng lặp while là:", tongleWhile(n))
print("Tổng các số lẻ từ 1 đến", n, "sử dụng vòng lặp for là:", tongLefor(n))
print()
