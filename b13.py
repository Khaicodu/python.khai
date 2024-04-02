import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
print('Bai 13')
# Hàm số và các đạo hàm
x = sp.symbols('x')
y = 4*x**4 + 5*x**2 - 8
y_prime = sp.diff(y, x)
y_double_prime = sp.diff(y_prime, x)
y_triple_prime = sp.diff(y_double_prime, x)

# Biến đổi thành các hàm số có thể sử dụng
y_func = sp.lambdify(x, y, 'numpy')
y_prime_func = sp.lambdify(x, y_prime, 'numpy')
y_double_prime_func = sp.lambdify(x, y_double_prime, 'numpy')
y_triple_prime_func = sp.lambdify(x, y_triple_prime, 'numpy')

# Định nghĩa miền giá trị x
x_values = np.linspace(-15, 15, 400)

# Tính giá trị của hàm số và các đạo hàm tương ứng
y_values = y_func(x_values)
y_prime_values = y_prime_func(x_values)
y_double_prime_values = y_double_prime_func(x_values)
y_triple_prime_values = y_triple_prime_func(x_values)

# Vẽ đồ thị
plt.figure(figsize=(10, 6))

# Đồ thị của hàm số y
plt.plot(x_values, y_values, label='y', color='blue')

# Đồ thị của đạo hàm y'
plt.plot(x_values, y_prime_values, label="y'", color='red')

# Đồ thị của đạo hàm bậc hai y''
plt.plot(x_values, y_double_prime_values, label="y''", color='green')

# Đồ thị của đạo hàm bậc ba y'''
plt.plot(x_values, y_triple_prime_values, label="y'''", color='purple')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Đồ thị của hàm số và các đạo hàm')
plt.legend()
plt.grid(True)
plt.show()

# Mã vẽ hình mặt yên ngựa
def vematyenngua():
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    x, y = np.meshgrid(x, y)
    z = (x/4)**2 - (y/5)**2

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Đồ thị mặt yên ngựa')
    plt.show()

# Mã vẽ hình hyperbolic một tầng
def vemathyperbolic1tang():
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    x, y = np.meshgrid(x, y)
    z = np.sqrt((x/5)**2 + (y/3)**2 + 1)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Đồ thị mặt hyperbolic 1 tầng')
    plt.show()

# Mã vẽ mặt cầu
def vematcau():
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)
    x = 6 * np.sin(theta) * np.cos(phi) - 6
    y = 6 * np.sin(theta) * np.sin(phi) + 3
    z = 6 * np.cos(theta) + 8

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Đồ thị mặt cầu')
    plt.show()

# Gọi các hàm để vẽ các hình
vematyenngua()
vemathyperbolic1tang()
vematcau()
