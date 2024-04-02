# Bài 10 xử lý ngoại lệ
def kiemtra(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài cạnh phải là số dương và lớn hơn 0")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba cạnh không thể tạo thành một tam giác")
def nhapA():
    while True:
        try:
            a = int(input('Nhập số tự nhiên a: '))
            if a < 0:
                raise ValueError("Nhập số tự nhiên, vui lòng nhập lại!")
            return a
        except ValueError:
            print('a phải là số tự nhiên')

def nhapB():
    while True:
        try:
            b = int(input('Nhập số tự nhiên b: '))
            if b < 0:
                raise ValueError("Nhập số tự nhiên, vui lòng nhập lại!")
            return b
        except ValueError:
            print('b phải là số tự nhiên')

def nhapC():
    while True:
        try:
            c = int(input('Nhập số tự nhiên c: '))
            if c < 0:
                raise ValueError("Nhập số tự nhiên, vui lòng nhập lại!")
            return c
        except ValueError:
            print('c phải là số tự nhiên')

try:
    a = nhapA()
    b = nhapB()
    c = nhapC()
    kiemtra(a,b,c)
    print(f"Ba cạnh {a},{b},{c} có thể tạo thành một tam giác.")
except ValueError as ve:
    print("Lỗi", ve)
