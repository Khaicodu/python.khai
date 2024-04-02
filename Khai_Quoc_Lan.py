from math import *
def cong(a,b):
    tong = a+b
    return tong
def nhan(a,b):
    tich = a*b
    return tich
def binhphuong(a,b):
    muhai = pow(a,b)
    return muhai
def canbac2(a,):
    canbac = sqrt(a)
    return canbac
def a_coss(a):
    a_ss = acos(a)
    return a_ss
def giaiPT(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return "Phương trình có một nghiệm: x = {:.2f}".format(x)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            return "Phương trình có nghiệm kép: x = {:.2f}".format(x)
        else:
            x1 = (-b + sqrt(delta)) / (2*a)
            x2 = (-b - sqrt(delta)) / (2*a)
            return "Phương trình có hai nghiệm: x1 = {:.2f}, x2 = {:.2f}".format(x1, x2)

