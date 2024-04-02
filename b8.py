import random

# Bài 8
from Khai_Quoc_Lan import *
a = random.randint(1, 70)
b = random.randint(1, 5)
c = random.randint(1, 150)
print(f"Tổng của {a} + {b} = {cong(a, b):.2f}")
print(f"Tích của {a} * {b} = {nhan(a, b):.2f}")
print(f"Mũ {a} ^ {b} = {binhphuong(a, b):.2f}")
print(f"Căn bậc hai của {a} = {canbac2(a):.2f}")
if -1 <= a <= 1:
    print(f"acos của {a} = {round(a_coss(a), 2)}")  # Lấy 2 số sau dấu thập phân
else:
    print("Giá trị của a không hợp lệ. Phải nằm trong khoảng [-1, 1].")
print(f"Phương trình có nghiệm {giaiPT(a,b,c)}")
