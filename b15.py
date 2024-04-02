import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
print('Bai 15')
# a) Giải hệ phương trình
def giaihephuongtrinh():
    x, y, z = sp.symbols('x y z')
    eq1 = sp.Eq(2*x - 5*y + z, -5)
    eq2 = sp.Eq(4*x + 2*y - 2*z, 2)
    eq3 = sp.Eq(x + y - z, 0)
    nguyem = sp.solve((eq1, eq2, eq3), (x, y, z))
    return nguyem

# b) Tính giới hạn của hàm
def tinhgioihan():
    x = sp.Symbol('x')
    f = (x**3 - 3*x**2)**(1/3) + (x**2 - 2*x)**(1/2)
    lim = sp.limit(f, x, 5)
    return lim

# c) Tính đạo hàm của hàm
def tinhdaoham():
    x = sp.Symbol('x')
    f = (4*x - 1) / (3*x + 5)
    daoham = sp.diff(f, x)
    return daoham

# d) Tính nguyên hàm của hàm
def tinhnguyenham():
    x = sp.Symbol('x')
    f = 5*x / (x**2 + 2)
    nguyenham = sp.integrate(f, x)
    return nguyenham

# e) Tính tích phân của hàm
def tinhtichphan():
    x = sp.Symbol('x')
    f = (1 - x*sp.tan(x)) / (x**2*sp.cos(x) + x)
    tichphan = sp.integrate(f, (x, sp.pi, 3*sp.pi/2))
    return tichphan

# f) Chương trình chính
def main():
    print("a) Giải hệ phương trình:")
    print("   Giải hệ phương trình: ", giaihephuongtrinh())

    print("\nb) Tính giới hạn của hàm:")
    print("   Giới hạn của hàm: ", tinhgioihan())

    print("\nc) Tính đạo hàm của hàm:")
    print("   Đạo hàm của hàm: ", tinhdaoham())

    print("\nd) Tính nguyên hàm của hàm:")
    print("   Nguyên hàm của hàm: ", tinhnguyenham())

    print("\ne) Tính tích phân của hàm:")
    print("   Tích phân của hàm: ", tinhtichphan())

if __name__ == "__main__":
    main()
