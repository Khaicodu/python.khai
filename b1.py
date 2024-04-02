import random
import math
import string
# Bài 1 :  Dùng mô hình biểu diễn Namespace để giải thích kết quả lệnh: x, y = y, x
# Nhập giá trị
print('BÀI 1')
x = int(input('Nhập giá trị của x : '))
y = int(input('Nhập giá trị của y : '))
# In ra giá trị ban đầu
print(f"Trước khi hoán đổi: x = {x}, y = {y}")
# Hoán đổi
x,y = y,x
#In ra giá trị sau khi hoán đổi
print(f"Sau khi hoán đổi: x = {x}, y = {y}")
