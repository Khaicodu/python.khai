import random
import math
print('BÀI 4')
A = [random.randint(30, 150) for _ in range(10)]
B = [random.randint(30, 150) for _ in range(10)]
# In dãy số A và B
print("Dãy A:", A)
print("Dãy B:", B)
# Bước 2 và 3: Tính GCD và tạo dãy C
C = [math.gcd(A[i], B[i]) for i in range(10)]
# In dãy số C
print("Dãy C (Ước số chung lớn nhất của A và B):", C)
