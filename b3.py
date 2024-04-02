import random
print('BÀI 3')
# Kiểm tra số nguyên tố
def primes(m):
    if m < 2:
        return 0
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return 0
    return 1
# Ước số thực sự
def uocSots(m):
    count = 0
    for i in range(2, m):
        if m % i == 0:
            count += 1
    return count

# Ước số lẻ
def uocSole(m) :
    count = 0
    for i in range(1, m + 1, 2):  # Chỉ xét các số lẻ
        if m % i == 0:
            count += 1
    return count

# số nguyên tố nhỏ hơn m
def sntNhom(m) :
    count = 0
    for i in range(2, m):
        if primes(i):
            count += 1
    return count

# tổng ước số thực
def tongUSthuc(m) :
    tong = 0
    for i in range(2, m):
        if m % i == 0:
            tong += i
    return tong
def main():
    m = random.randint(5, 100)
    print(f'Số m sau khi chọn ngẫu nhiên là: {m}')
    print(f'm {"là" if primes(m) else "không phải là"} số nguyên tố.')
    print(f'Số ước số thực sự của m là: {uocSots(m)}')
    print(f'Số ước số lẻ của m là: {uocSole(m)}')
    print(f'Số số nguyên tố nhỏ hơn m là: {sntNhom(m)}')
    print(f'Tổng các ước số thực sự của m là: {tongUSthuc(m)}')
if __name__ == "__main__":
    main()
