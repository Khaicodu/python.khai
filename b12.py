import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
print('Bài 12')
def tich_vo_huong(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Số cột của ma trận A phải bằng số hàng của ma trận B để tính tích vô hướng.")
    return np.dot(A, B)

def tich_co_huong(A, B):
    return np.dot(A, B.T)

def main():
    while True:
        m = np.random.randint(3, 9)  # Số hàng của ma trận
        n = np.random.randint(3, 9)  # Số cột của ma trận
        p = np.random.randint(3, 9)  # Số cột của ma trận B

        A = np.random.rand(m, n)  # Tạo ma trận A với các phần tử ngẫu nhiên
        B = np.random.rand(n, p)  # Tạo ma trận B với các phần tử ngẫu nhiên

        try:
            D = tich_vo_huong(A, B)
            E = tich_co_huong(A, B)
            break
        except ValueError as e:
            print("ValueError:", e)
            print("Đồ thị không bằng nhau. Chạy lại...\n")

    print("Ma trận A:")
    print(A)
    print("\nMa trận B:")
    print(B)
    print("\nTích vô hướng của A và B:")
    print(D)
    print("\nTích có hướng của A và B^T:")
    print(E)

if __name__ == "__main__":
    main()
