import random
print('BÀI 6')
# Tạo tập hợp A với 100 số tự nhiên ngẫu nhiên từ 1 đến 1000
A = set(random.randint(1, 1000) for _ in range(100))
print("Tập hợp A:", A)

# Để tạo tập hợp B từ A
if len(A) >= 20:
    B = set(random.sample(list(A), 20))
else:
    print("Tập A không đủ phần tử để tạo tập B")
print("Tập hợp B:", B)

# Tạo tập hợp C từ B
if len(B) >= 10:
    C = set(random.sample(list(B), 10))
else:
    print("Tập B không đủ phần tử để tạo tập C")
print("Tập hợp C:", C)
