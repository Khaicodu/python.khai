import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
print('Bai 14')
# a) Hàm vẽ đồ thị mặt yên ngựa
def vematyenngua():
    # Tạo dữ liệu x và y trong khoảng [-10, 10]
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)

    # Tạo lưới dữ liệu x, y
    x, y = np.meshgrid(x, y)

    # Tính giá trị z theo công thức mặt yên ngựa
    z = (x/4)**2 - (y/5)**2

    # Tạo một hình 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ đồ thị bề mặt
    ax.plot_surface(x, y, z, cmap='viridis')

    # Đặt nhãn cho các trục
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Đặt tiêu đề cho đồ thị
    ax.set_title('Đồ thị mặt yên ngựa')

    # Hiển thị đồ thị
    plt.show()

# b) Hàm vẽ đồ thị mặt hyperbolic 1 tầng
def vemathyperbolic1tang():
    # Tạo dữ liệu x và y trong khoảng [-10, 10]
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)

    # Tạo lưới dữ liệu x, y
    x, y = np.meshgrid(x, y)

    # Tính giá trị z theo công thức mặt hyperbolic 1 tầng
    z = np.sqrt((x/5)**2 + (y/3)**2 + 1)

    # Tạo một hình 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ đồ thị bề mặt
    ax.plot_surface(x, y, z, cmap='viridis')

    # Đặt nhãn cho các trục
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Đặt tiêu đề cho đồ thị
    ax.set_title('Đồ thị mặt hyperbolic 1 tầng')

    # Hiển thị đồ thị
    plt.show()

# c) Hàm vẽ đồ thị mặt cầu
def vematcau():
    # Tạo dữ liệu cho góc phi và theta
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)

    # Tạo lưới dữ liệu cho góc phi và theta
    phi, theta = np.meshgrid(phi, theta)

    # Tính toán tọa độ x, y, z cho mặt cầu
    x = 6 * np.sin(theta) * np.cos(phi) - 6
    y = 6 * np.sin(theta) * np.sin(phi) + 3
    z = 6 * np.cos(theta) + 8

    # Tạo một hình 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ đồ thị bề mặt
    ax.plot_surface(x, y, z, cmap='viridis')

    # Đặt nhãn cho các trục
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Đặt tiêu đề cho đồ thị
    ax.set_title('Đồ thị mặt cầu')

    # Hiển thị đồ thị
    plt.show()

# d) Chương trình chính
def main():
    # Gọi các hàm để vẽ các đồ thị
    vematyenngua()
    vemathyperbolic1tang()
    vematcau()
if __name__ == "__main__":
    main()

