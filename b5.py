import random
import string
print('BÀI 5')
def randomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
# Tạo Str1 và Str2
Str1 = randomString(2)
Str2 = randomString(30)

print("Str1:", Str1)
print("Str2:", Str2)

# a) Kiểm tra Str1 có trong Str2 không
if Str1 in Str2:
    print(f"Str1 '{Str1}' có nằm trong Str2.")
else:
    print(f"Str1 '{Str1}' không nằm trong Str2.")

# b) Đếm số lần xuất hiện của Str1 trong Str2
count = Str2.count(Str1)
print(f"Str1 xuất hiện trong Str2 {count} lần.")

# c) Chèn Str1 vào Str2 tại vị trí k
k = random.randint(1, len(Str1))  # Sinh số k ngẫu nhiên
print("Giá trị của k:", k)

# Chèn Str1 vào Str2
Str2_new = Str2[:k] + Str1 + Str2[k:]

print("Str2 sau khi chèn Str1:", Str2_new)
